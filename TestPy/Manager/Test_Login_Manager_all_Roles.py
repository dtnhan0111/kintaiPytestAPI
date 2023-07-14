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
def test_login_headers_body_json(staff_id, company_code, password):
    url = "https://kintai.stg.jinjer.net/v1/manager/sign_in"

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
    with open("../Manager/token_manager.csv", "a", newline='') as outfile:
        write = csv.writer(outfile)
        write.writerow([staff_id, token_])
    assert resp_body['code'] == 200
    assert resp_body['message'] == 'ログインしました'


