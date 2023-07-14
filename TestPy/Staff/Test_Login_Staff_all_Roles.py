import csv
import linecache
import string

import pytest
import requests
import json
from pytest_csv_params.decorator import csv_params


@csv_params(
    data_file="../Account/STG_account_role.csv",
    # id_col="ID",
    data_casts={
        "staff_id": str,
        "company_code": str,
        "password": str,
    },
)
def test_login_staff_all_roles(staff_id, company_code, password):
    url = "https://kintai.stg.jinjer.net/v1/sign_in"

    payload = json.dumps({
        "company_code": company_code,
        "email": staff_id,
        "password": password,
        "site_type": 2,
        "version": "5.0.6"
    })
    headers = {
        'User-Agent': 'iPhone',
        'Content-Type': 'application/json'
    }

    resp = requests.request("POST", url, headers=headers, data=payload)

    # Validate response headers and body contents, e.g. status code.
    resp_body = resp.json()
    token_ = resp_body['data']['token']
    with open("token_staff.csv", "a", newline='') as outfile:
        write = csv.writer(outfile)
        write.writerow([staff_id, token_])
    assert resp_body['code'] == 200
    assert resp_body['message'] == 'ログインしました'

    # Call API dashboard/shops
    url_dashboard_shops = "https://kintai.stg.jinjer.net/v1//dashboard/shops?is_latest_tc_shop=true"

    payload = {}
    headers = {
        'User-Agent': 'iPhone',
        'Api-Token': token_,
    }

    resp_dashboard_shop = requests.request("GET", url_dashboard_shops, headers=headers, data=payload)
    resp_dashboard_shop = resp_dashboard_shop.json()
    shop_id = resp_dashboard_shop['data']['shops'][0]['id']

    assert resp_dashboard_shop['code'] == 200
    assert resp_dashboard_shop['message'] == '支社の一覧を作成しました'

    # Call API dashboard/shops/{shop_id}
    url_dashboard_shops_id = f"https://kintai.stg.jinjer.net/v1/dashboard/shops/{shop_id}"

    payload = {}
    headers = {
        'User-Agent': 'iPhone',
        'Api-Token': token_,
    }

    resp_dashboard_shops_id = requests.request("GET", url_dashboard_shops_id, headers=headers, data=payload)
    resp_dashboard_shops_id = resp_dashboard_shops_id.json()

    assert resp_dashboard_shops_id['code'] == 200
    # assert resp_dashboard_shops_id['message'] == '支社の一覧を作成しました'
