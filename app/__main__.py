from fastapi import FastAPI, HTTPException, Query, status
import math

app = FastAPI()

currencies = {
    "TWD": {
        "TWD": 1,
        "JPY": 3.669,
        "USD": 0.03281
    },
    "JPY": {
        "TWD": 0.26956,
        "JPY": 1,
        "USD": 0.00885
    },
    "USD": {
        "TWD": 30.444,
        "JPY": 111.801,
        "USD": 1
    }
}

def round_up(n, m):
    """
    解決四捨五入問題
    """
    n = str(n)
    if len(n) - n.index(".") - 1 == m + 1:
        n += "1"
    n = float(n)
    return round(n, m)

def verify_currency(currency: str) -> bool:
    """
    驗證是否有支援此貨幣
    """
    return currency in currencies

def exchange(target: str, source: str, amount: str) -> float:
    """
    計算貨幣匯率
    """
    amount = float(amount.replace("$","").replace(",",""))
    result = round_up(currencies[target][source] * amount, 2)
    return result

def add_thousand_comma(amount: float, m: int) -> str:
    """
    增加逗點分隔做為千分位表示
    """
    result = "{:,}".format(amount)
    number, decimal = result.split(".")
    if len(decimal) < m:
        decimal += ("0" * (m - len(decimal)))
    return number + "." + decimal


@app.get("/")
async def exchange_api(
    source: str = Query(min_length=3 ,max_length=3),
    target: str = Query(min_length=3 ,max_length=3),
    amount: str = Query(str ,pattern="^\$[0-9]{1,3}(?:,[0-9]{3})*(?:\.[0-9]{1,2})?$")
):
    """
    轉換匯率
    """
    if not verify_currency(source) or not verify_currency(target):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="不支援輸入貨幣"
        )
    result = add_thousand_comma(exchange(source, target, amount),2)
    return {
        "msg": "success",
        "amount": f"${result}"
    }
