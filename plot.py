import os
import pandas as pd
import matplotlib.pyplot as plt

long_apart_df = pd.read_csv('data/long_term_housing.csv')
long_room_df = pd.read_csv('data/apartments_detail.csv')
hotel_df = pd.read_csv('data/hotel.csv')
airbnb_df = pd.read_csv('data/airbnb.csv')

static_folder = 'static'
if not os.path.exists(static_folder):
    os.makedirs(static_folder)

long_room_df_copy = long_room_df.copy(deep=True)

# Turn price from "$1,395" to 1395, turn "Call for Rent" to 0
long_room_df_copy['Unit Price'] = pd.to_numeric(long_room_df_copy['Unit Price'].replace('$', '').replace(',', ''), errors='coerce')
long_room_df_copy['Unit Price'] = long_room_df_copy['Unit Price'].fillna(0).astype(int)

# Visualize the price distribution of Long Term Room, save as long_price.png in static folder
plt.figure(figsize=(10, 6))
plt.hist(long_room_df_copy['Unit Price'], bins=30, edgecolor='black')
plt.xlabel('Price($/month)')
plt.ylabel('Frequency')

plt.savefig(os.path.join(static_folder, 'long_price.png'))
plt.close()


