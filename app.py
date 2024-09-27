import pandas as pd
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/choice')
def choice():
    return render_template('choice.html')


@app.route('/short_term')
def short_term():
    # 从CSV文件读取数据
    hotel_data = pd.read_csv('data/hotel.csv').to_dict(orient='records')
    airbnb_data = pd.read_csv('data/airbnb.csv').to_dict(orient='records')

    return render_template('short_term.html', hotel_data=hotel_data, airbnb_data=airbnb_data)


@app.route('/long_term')
def long_term():
    long_term_df = pd.read_csv('data/long_term_housing.csv').to_dict(orient='records')
    print(long_term_df)
    # apartments = long_term_df.groupby('Apartment Name').apply(lambda x: x.to_dict(orient='records')).to_dict()
    return render_template('long_term.html', apartments=long_term_df)


if __name__ == '__main__':
    app.run(debug=True)
