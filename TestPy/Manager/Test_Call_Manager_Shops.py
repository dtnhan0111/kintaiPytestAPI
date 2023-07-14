import csv

import requests
from pytest_csv_params.decorator import csv_params


@csv_params(
    data_file="../Manager/token_manager.csv",
    data_casts={
        "staff_id": str,
        "token": str,
    },
)
def test_manager_shops(staff_id, token):
    url = "https://kintai.stg.jinjer.net/v1/manager/shops"
    payload = {}
    headers = {
        'Api-Token': token,
        'User-Agent': 'iPhone'
    }
    # Get data to verify
    resp = requests.request("GET", url, headers=headers, data=payload)
    resp_body = resp.json()
    assert resp_body['code'] == 200
    assert resp_body['message'] == '事業所をリストアップしました'
