from datetime import datetime

from pykrx import stock
import controlExcel

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
        controlExcel.delete_stock(stockName)

    # 코스닥 티커
    for ticker in KOSDAQStockNumber:
        stockName = stock.get_market_ticker_name(ticker)
        controlExcel.delete_stock(stockName)


# 오늘 날짜 가져오기
today = datetime.today().strftime("%Y%m%d")  # YYYYmmddHHMMSS 형태의 시간 출력
print(today)

# 공매도 "거래 비중" top50을 가져와서 종목코드를 리스트 형태로 담는다
KOSPIShortVolume = stock.get_shorting_volume_top50("20201104", "KOSPI")
KOSDAQShortVolume = stock.get_shorting_volume_top50("20201104", "KOSDAQ")
# 종목 코드를 바탕으로 종목명을 알아내고 엑셀에서 해당 종목이 있을 경우 삭제
check(KOSPIShortVolume, KOSDAQShortVolume)

# 공매도 "잔고" top50을 가져와서 종목코드를 리스트 형태로 담는다
KOSPIShortBalance = stock.get_shorting_balance_top50("20201104", "KOSPI")
KOSDAQShortBalance = stock.get_shorting_balance_top50("20201104", "KOSDAQ")
check(KOSPIShortBalance, KOSDAQShortBalance)
