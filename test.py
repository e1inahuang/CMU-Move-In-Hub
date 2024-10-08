# Load the CSV data
import pandas as pd

long_term_housing = pd.read_csv('data/long_term_housing.csv')
apartments_detail = pd.read_csv('data/apartments_detail.csv')


def paginate(data, per_page, page):
    start = (page - 1) * per_page
    end = start + per_page
    page_count = len(data) // per_page + 1
    return data[start:end], page_count


sliced_df, page_count = paginate(long_term_housing, 10, 1)

merged_df = pd.merge(sliced_df, apartments_detail, on='Apartment Name', how="left")

merged_dict = merged_df.groupby('Apartment Name').apply(
    lambda group: group.drop(columns='Apartment Name').to_dict('records')
).to_dict()

for name, rows in merged_dict.items():
    for i, row in enumerate(rows):
        print(name, i, row)
