from test import client
from typing import List

def test_exchange_api_input_missing():
    """
    測試沒有或缺少輸入
    """
    response = client.get("/", params={})
    assert response.status_code == 422


def test_exchange_api_input_source_or_target_not_support():
    """
    測試輸入沒有支援的貨幣
    """
    response = client.get("/", params={
        "source": "CNY",  # CNY 沒有支援
        "target": "TWD",
        "amount": "$1,525"
    })
    assert response.status_code == 422
    response = client.get("/", params={
        "source": "USD",
        "target": "CNY",  # CNY 沒有支援
        "amount": "$1,525"
    })
    assert response.status_code == 422

def test_exchange_api_input_amount_dollar_sign():
    """
    測試輸入 amount 是否缺少 dollar_sign
    """
    response = client.get("/", params={
        "source": "USD",
        "target": "TWD",
        "amount": "1,525"
    })
    assert response.status_code == 422

def test_exchange_api_input_amount_wrong_comma():
    """
    測試輸入的 amount 千分位不正確
    """
    response = client.get("/", params={
        "source": "USD",
        "target": "JPY",
        "amount": "$15,25"
    })
    assert response.status_code == 422

def test_exchange_api_output_usd_to_jpy():
    """
    測試輸出範例 (應該為正確)
    """
    response = client.get("/", params={
        "source": "USD",
        "target": "JPY",
        "amount": "$1,525"
    })
    data = response.json()
    assert data == {
        "msg": "success",
        "amount": "$170,496.53"
    }

def test_exchange_api_output_amount_float():
    """
    測試輸出的 amount 是否有取到小數點第二位
    """
    response = client.get("/", params={
        "source": "USD",
        "target": "TWD",
        "amount": "$25,845.5"
    })
    data = response.json()
    assert "amount" in data and data['amount'] == "$786,840.40"
    amount: List[str] = data["amount"].replace("$", "").replace(",", "").split(".")
    assert len(amount) == 2
    assert len(amount[1]) == 2 and amount[1] == "40" # 測試小數點位數

def test_exchange_api_output_amount_comma():
    """
    測試輸出的逗點做千分位表示
    """
    response = client.get("/", params={
        "source": "USD",
        "target": "JPY",
        "amount": "$1,525"
    })
    data = response.json()
    assert "amount" in data and data['amount'] == "$170,496.53"
    amount: List[str] = data["amount"].replace("$", "").split(".")
    assert len(amount) == 2
    assert len(amount[0]) == 7
    assert len(amount[0].replace(",","")) == 6
