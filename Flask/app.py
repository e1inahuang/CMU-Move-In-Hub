import pandas as pd
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Load the CSV data
long_apart_df = pd.read_csv('data/long_term_housing.csv')
long_room_df = pd.read_csv('data/apartments_detail.csv')
hotel_df = pd.read_csv('data/hotel.csv')
airbnb_df = pd.read_csv('data/airbnb.csv')


@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/choice')
def choice():
    return render_template('choice.html')


def paginate(data, per_page, page):
    start = (page - 1) * per_page
    end = start + per_page
    page_count = len(data) // per_page + 1
    return data[start:end], page_count


@app.route('/short_term')
def short_term():
    hotel_page = request.args.get('page', 1, type=int)
    hotel_sliced_df, hotel_page_count = paginate(hotel_df, 20, hotel_page)
    hotel_data = hotel_sliced_df.to_dict(orient='records')

    airbnb_page = request.args.get('page', 1, type=int)
    airbnb_sliced_df, airbnb_page_count = paginate(airbnb_df, 20, airbnb_page)
    airbnb_data = airbnb_sliced_df.to_dict(orient='records')

    return render_template('short_term.html',
                           hotel_data=hotel_data,
                           airbnb_data=airbnb_data,
                           hotel_page=hotel_page,
                           airbnb_page=airbnb_page,
                           total_hotel_pages=hotel_page_count,
                           total_airbnb_pages=airbnb_page_count,
                           hotel_current_sort='Hotel Name',
                           airbnb_current_sort='Apartment Name')


@app.route('/load_hotel_page')
def load_hotel_page():
    hotel_sort_by = request.args.get('sort_by', default='Hotel Name')
    hotel_sort_order = request.args.get('sort_order', 'asc')
    hotel_sorted_df = hotel_df.sort_values(by=hotel_sort_by, ascending=hotel_sort_order == 'asc')

    hotel_page = request.args.get('page', 1, type=int)
    hotel_sliced_df, hotel_page_count = paginate(hotel_sorted_df, 20, hotel_page)
    hotel_data = hotel_sliced_df.to_dict(orient='records')
    return render_template('hotel.html',
                           hotel_data=hotel_data,
                           hotel_page=hotel_page,
                           total_hotel_pages=hotel_page_count,
                           hotel_current_sort=hotel_sort_by)


@app.route('/load_airbnb_page')
def load_airbnb_page():
    airbnb_sort_by = request.args.get('sort_by', default='Apartment Name')
    airbnb_sort_order = request.args.get('sort_order', 'asc')
    airbnb_sorted_df = airbnb_df.sort_values(by=airbnb_sort_by, ascending=airbnb_sort_order == 'asc')

    airbnb_page = request.args.get('page', 1, type=int)
    airbnb_sliced_df, airbnb_page_count = paginate(airbnb_sorted_df, 20, airbnb_page)
    airbnb_data = airbnb_sliced_df.to_dict(orient='records')
    return render_template('airbnb.html',
                           airbnb_data=airbnb_data,
                           airbnb_page=airbnb_page,
                           total_airbnb_pages=airbnb_page_count,
                           airbnb_current_sort=airbnb_sort_by)


@app.route('/long_term')
def long_term():
    page = request.args.get('page', default=1, type=int)
    sort_by = request.args.get('sort_by', default='Apartment Name')
    sort_order = request.args.get('sort_order', default='asc')
    long_sorted_df = long_apart_df.sort_values(by=sort_by, ascending=sort_order == 'asc')

    sliced_df, page_count = paginate(long_sorted_df, 10, page)
    merged_df = pd.merge(sliced_df, long_room_df, on='Apartment Name', how="left")
    merged_dict = merged_df.groupby('Apartment Name').apply(
        lambda group: group.drop(columns='Apartment Name').to_dict('records')
    ).to_dict()

    return render_template('long_term.html',
                           apartments=merged_dict,
                           enumerate=enumerate,
                           page=page,
                           num_pages=page_count)


if __name__ == '__main__':
    app.run()
