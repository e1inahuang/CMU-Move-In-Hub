import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import json

cookies = {
    'bev': '1727204960_EANmUwMWVlZGYzZG',
    'everest_cookie': '1727204960.EAYjA3NjljZWFlOGUwYT.XFzrZb5pXNvPKcfjKCVbq6E_jADzYED-oBef5Ke6zF4',
    'cdn_exp_0752821c603ff621a': 'control',
    'cdn_exp_6de452700098fbf87': 'control',
    '_gcl_au': '1.1.948044704.1727204959',
    '_ga': 'GA1.1.633418654.1727204958',
    '_ccv': 'cban%3A0_183215%3D1%2C0_200000%3D1%2C0_183345%3D1%2C0_183243%3D1%2C0_183216%3D1%2C0_179751%3D1%2C0_200003%3D1%2C0_200005%3D1%2C0_179754%3D1%2C0_179750%3D1%2C0_179737%3D1%2C0_179744%3D1%2C0_179739%3D1%2C0_179743%3D1%2C0_179749%3D1%2C0_200012%3D1%2C0_200011%3D1%2C0_183217%3D1%2C0_183219%3D1%2C0_183096%3D1%2C0_179747%3D1%2C0_179740%3D1%2C0_179752%3D1%2C0_183241%3D1%2C0_200007%3D1%2C0_183346%3D1%2C0_183095%3D1%2C0_210000%3D1%2C0_210001%3D1%2C0_210002%3D1%2C0_210003%3D1%2C0_210004%3D1%2C0_210010%3D1',
    'FPID': 'FPID2.2.ssSLzDgls9QfnG5UhcSUrVo16Z0OlAbSqhe9gzAJX%2BY%3D.1727204958',
    'FPAU': '1.1.948044704.1727204959',
    '_scid': 'dc2a8ddb-e7e4-4cfd-4dcb-cf1bebede994',
    '_gtmeec': 'eyJleHRlcm5hbF9pZCI6IjE3MjcyMDQ5NjBfRUFObVV3TVdWbFpHWXpaRyJ9',
    'tzo': '-240',
    'previousTab': '%7B%22id%22%3A%222da1f136-6999-4f33-9cb3-9bfdb991c093%22%7D',
    'frmfctr': 'wide',
    '_user_attributes': '%7B%22device_profiling_session_id%22%3A%221727204960--2800b6d421c227d2abc4305c%22%2C%22giftcard_profiling_session_id%22%3A%221727321159--45769bb6738b15e859c6e0d3%22%2C%22reservation_profiling_session_id%22%3A%221727321159--feff6a8cd7d55ec4f243a8a2%22%2C%22curr%22%3A%22USD%22%7D',
    'country': 'US',
    'ak_bmsc': 'F5EE6FBB4ECF9B0A6DDD513EDCC969F2~000000000000000000000000000000~YAAQtHTZFzh9WCuSAQAAcjddLBl5BooViHaoohUdLWgTW2Y4jRn8diNFVmgEqCNpLy7JUtp8iSIYxOy+5rI8D/6SSB9f0pmlE1W007cYEMiFSBv08S+ppo7CQGyuMIutO0scuUHpZJGt52NscbDeqa+k+ahWUfOoo/tOmTR4sJZDoJqnNZit8vqF6I7QFbjqyg3KFlVa2I9K82jIJ4ByiAjmqDjdAVCle05AdYJrAN2xC+Ri2Yl84UyxwGKZr2Zh9ytBpFNq/U/sndK6ihtx62KMgN2y/9vsDX3NOENzqBQfZ0fYhRCpF5sxjUWSByWggf9EG2M1lgvahazzR6j3pCsJ2lTjWFWwrsSwNNrwdxB3AadqgpaqRLmYEFLdwwH+Pkf6qUWtTg==',
    'previousTab': '%7B%22id%22%3A%222ea455d4-e931-44b1-917b-adff4ea0ad5d%22%7D',
    'jitney_client_session_id': 'e7d3e7c4-a82a-4a44-8fc2-85e67c82085b',
    'jitney_client_session_created_at': '1727321151.858',
    'FPGSID': '1.1727321161.1727321161.G-2P6Q8PGG16.mqiCHRTsmtZlY6eJKF7Hhw',
    'FPLC': 'Okx%2Bvqw%2BcDwcEQGMQlcf4vKHUrNQE%2F6T%2F0n9FYRZrxgAmoeXB8CESuq3c%2ByMBVERym6QLEN%2BlNcMgwrsnd2LAXlMZx3NNLj8HBftYXjE6ySrFJNggwgAPRXYHnXgew%3D%3D',
    'cfrmfctr': 'MOBILE',
    'cbkp': '2',
    'OptanonConsent': '0_179750%3A1%2C0_183095%3A1%2C0_183241%3A1%2C0_179754%3A1%2C0_183346%3A1%2C0_200000%3A1%2C0_210000%3A1%2C0_210010%3A1%2C0_183215%3A1%2C0_210004%3A1%2C0_179737%3A1%2C0_179752%3A1%2C0_179751%3A1%2C0_179749%3A1%2C0_200007%3A1%2C0_210001%3A1%2C0_200005%3A1%2C0_179740%3A1%2C0_179743%3A1%2C0_179744%3A1%2C0_183243%3A1%2C0_183096%3A1%2C0_179747%3A1%2C0_183216%3A1%2C0_200012%3A1%2C0_183219%3A1%2C0_200003%3A1%2C0_179739%3A1%2C0_210002%3A1%2C0_183217%3A1%2C0_183345%3A1%2C0_210003%3A1%2C0_200011%3A1',
    '_cci': 'cban%3Aac-bf3dacf2-ed59-44ff-bc70-07d0b7880947',
    'jitney_client_session_updated_at': '1727321211',
    'jitney_client_session_updated_at': '1727321201.848',
    '_ga_2P6Q8PGG16': 'GS1.1.1727321153.3.1.1727321206.0.0.1512290996',
    'bm_sv': '486BB71FA156C1EE95A8DE56858B3FAD~YAAQ7CQwF6tezCqSAQAAAyNeLBkVkRWeL8JNIG3UHxkm80fmWQPmP5J9IuzlWzCaTYQ8P9hVErXlaW6+WTCdzyeLKWUk5aKvNICGqxOzwdkGvpM51u2u0jc2mz5J7E4hEMhlpZEnva0XeBC0TBijdJGFvM1RDKHXMha6jkwg8wi4Pmd1rr9gS+sFlx5HHH0B0xwkmY7uYJeMGlDQPVUz9K4QuM64sKV+l/4UUhQ01Sz8SP1fO2CelG0by3X/cMIN5w==~1',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'device-memory': '8',
    'dpr': '1.875',
    'ect': '4g',
    'priority': 'u=0, i',
    'referer': 'https://www.bing.com/',
    'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    'viewport-width': '803',
}



base_url = 'https://www.airbnb.com/s/Pittsburgh--PA--United-States/homes'

params = {
    'tab_id': 'home_tab',
    'refinement_paths[]': '/homes',
    'query': 'Pittsburgh, PA, United States',
    'place_id': 'ChIJA4UGSG_xNIgRNBuiWqEV-Y0',
    'flexible_trip_lengths[]': 'one_week',
    'monthly_start_date': '2024-10-01',
    'monthly_length': '3',
    'monthly_end_date': '2025-01-01',
    'search_mode': 'regular_search',
    'disable_auto_translation': 'true',
    'price_filter_input_type': '0',
    'channel': 'EXPLORE',
    'search_type': 'unknown',
    'price_filter_num_nights': '5',
    'federated_search_session_id': '12002f46-fea3-43f1-bf88-e2090b6ceaea',
    'pagination_search': 'true',
    'cursor': 'eyJzZWN0aW9uX29mZnNldCI6MCwiaXRlbXNfb2Zmc2V0IjowLCJ2ZXJzaW9uIjoxfQ==',
    'locale': 'en',
    '_set_bev_on_new_domain': '1727192984_EANmQwODBiNjJlND'
}

def result_to_all_apartments(apartments,result):
    for item in result:
        try:
            apartment_name = item['listing']['title'] if item['listing']['title'] else ' '
            # address = item['listing']['location']['address']
            latitude = item['listing']['coordinate']['latitude'] if item['listing']['coordinate']['latitude'] else ' '
            longtitude = item['listing'].get('coordinate', {}).get('longitude', ' ')

            if 'price' in item['pricingQuote']['structuredStayDisplayPrice']['primaryLine']:
                price = item['pricingQuote']['structuredStayDisplayPrice']['primaryLine']['price']
                discount = 'No'
                save_money = 0
            else:
                price = item['pricingQuote']['structuredStayDisplayPrice']['primaryLine']['discountedPrice']
                discount = 'Yes'
                save_money = int(item['pricingQuote']['structuredStayDisplayPrice']['primaryLine']['originalPrice'].split('$')[1]) - int(item['pricingQuote']['structuredStayDisplayPrice']['primaryLine']['discountedPrice'].split('$')[1])

            avg_rating = item['listing'].get('avgRatingLocalized', ' ')
            pets_allowed = 'No' if item['listingParamOverrides']['pets'] == 0 else 'Yes'
            free_cancellation = 'Yes' if (
                    item.get('listing', {}).get('structuredContent', {}).get('primaryLine') and
                    item['listing']['structuredContent']['primaryLine'][0].get('body') == 'Free cancellation'
            ) else "No"

            room_type = item['listing'].get('roomTypeCategory', ' ')

            character = item['listing'].get('name', ' ')

            amenities = ', '.join(item['listing'].get('listingParamOverrides', {}).get('amenities', []))

            apartment_url = "https://airbnb.com/rooms/" + str(item['listing'].get('id', ' '))

            apartment_info = {
                'Apartment Name': apartment_name,
                'Average Rating': avg_rating,
                'latitude': latitude,
                'longtitude': longtitude,
                'Price': price,
                'Discount': discount,
                'Save money': save_money,
                'Character': character,
                'Room Type': room_type,
                'Pets_allowed': pets_allowed,
                'Free canceled': free_cancellation,
                'Amenities': amenities,
                'URL': apartment_url
            }

            apartments.append(apartment_info)

        except KeyError as e:
            print(f"Missing field {e} in item {item}")


    # for apt in apartments:
    #     print(apt)



response = requests.get(base_url, params=params, cookies=cookies, headers=headers)
soup = BeautifulSoup(response.content,'html.parser')
text1 = soup.find('script', {'id': 'data-deferred-state-0'}).text
data = json.loads(text1)
result = data['niobeMinimalClientData'][0][1]['data']['presentation']['staysSearch']['results']['searchResults']
pagination_info = data['niobeMinimalClientData'][0][1]['data']['presentation']['staysSearch']['results']['paginationInfo']['pageCursors']
apartments = []
#result_to_all_apartments(apartments, result)
for cursor in pagination_info:

    params["cursor"] = cursor

    response = requests.get(base_url, params=params, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    text1 = soup.find('script', {'id': 'data-deferred-state-0'}).text
    data = json.loads(text1)
    result = data['niobeMinimalClientData'][0][1]['data']['presentation']['staysSearch']['results']['searchResults']

    result_to_all_apartments(apartments, result)
    print(f'page.........................................{len(apartments)}')
csv_file = 'apartments.csv'

with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=apartments[0].keys())

    writer.writeheader()
    for apartment in apartments:
        writer.writerow(apartment)

print(f"write to {csv_file}")

