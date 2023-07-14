import csv

import requests


def get_shop_id():
    token = get_csv_value(csv_file_path)
    url_dashboard_shops = "https://kintai.stg.jinjer.net/v1//dashboard/shops?is_latest_tc_shop=true"

    payload = {}
    headers = {
        'User-Agent': 'iPhone',
        'Api-Token': token,
    }

    resp_dashboard_shop = requests.request("GET", url_dashboard_shops, headers=headers, data=payload)
    resp_dashboard_shop = resp_dashboard_shop.json()
    shop_id = resp_dashboard_shop['data']['shops'][0]['id']
    print(shop_id)
    shop_name = resp_dashboard_shop['data']['shops'][0]['name']
    print(shop_name)

    with open("shop_id.csv", "a", newline='') as outfile:
        write = csv.writer(outfile)
        write.writerow([shop_id, shop_name])


def get_csv_value(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Bỏ qua tiêu đề cột

        for row in reader:
            value = row[1]  # Lấy giá trị từ cột thích hợp trong tệp CSV
            return value  # Trả về giá trị đầu tiên trong tệp CSV


# Gọi hàm và gán giá trị cho biến
csv_file_path = 'C:/Users/Nhan.dt/PycharmProjects/TestPy/Staff/token_staff.csv'
variable = get_csv_value(csv_file_path)
print(variable)

get_shop_id()
print('Check file CSV to get Shop ID')
