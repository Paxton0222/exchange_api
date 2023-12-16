from app.__main__ import add_thousand_comma, exchange, round_up

def test_exchange():
    """
    測試計算貨幣匯率

    轉換金額請四捨五入到小數點第二位
    且轉換後的金額顯示格式請增加逗點分隔做為千分位表示
    如 123,456.78
    """
    data = exchange("USD","TWD","$25,845.5")
    assert data == 786840.4

def test_thousand_comma():
    """
    測試每千分位加入逗號
    """
    assert add_thousand_comma(17.52,2) == "17.52"
    assert add_thousand_comma(17523.55,2) == "17,523.55"
    assert add_thousand_comma(5555.55,2) == "5,555.55"
    assert add_thousand_comma(5555.5,2) == "5,555.50"

def test_python_round_five_problem():
    """
    測試四捨五入五進位
    """
    assert round_up(17.555,2) == 17.56
    assert round_up(5.444, 2) == 5.44
