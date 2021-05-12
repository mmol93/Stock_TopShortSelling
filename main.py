from pykrx import stock

# 참조 https://github.com/sharebook-kr/pykrx

# DataFrame의 티커에서 종목이름으로 변경하기
def check(KOSPIShort, KOSDAQShort):
    # DataFrame의 인덱스 자체가 종목 코드임
    KOSPIStockNumber = KOSPIShort.index
    KOSDAQStockNumber = KOSDAQShort.index

    # 티커를 종목명으로 출력
    # 코스피 티커
    for ticker in KOSPIStockNumber:
        stockName = stock.get_market_ticker_name(ticker)
        print(stockName)

    # 코스닥 티커
    for ticker in KOSDAQStockNumber:
        stockName = stock.get_market_ticker_name(ticker)
        print(stockName)

# 공매도 거래 비중 top50
KOSPIShortVolume = stock.get_shorting_volume_top50("20201104", "KOSPI")
KOSDAQShortVolume = stock.get_shorting_volume_top50("20201104", "KOSDAQ")
check(KOSPIShortVolume, KOSDAQShortVolume)

# 공매도 잔고 top50
KOSPIShortBalance = stock.get_shorting_balance_top50("20201104", "KOSPI")
KOSDAQShortBalance = stock.get_shorting_balance_top50("20201104", "KOSDAQ")
check(KOSPIShortBalance, KOSDAQShortBalance)





