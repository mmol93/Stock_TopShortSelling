import datetime
from pykrx import stock
import controlExcel

# 참조 https://github.com/sharebook-kr/pykrx

# DataFrame의 티커에서 종목이름으로 변경하기
def check(KOSPIShort, KOSDAQShort):
    # DataFrame의 인덱스 자체가 종목 코드임
    KOSPIStockNumber = KOSPIShort.index
    KOSDAQStockNumber = KOSDAQShort.index

    # 코스피 부분 처리
    for ticker in KOSPIStockNumber:
        # 티커를 종목명으로 출력
        stockName = stock.get_market_ticker_name(ticker)
        # 해당 종목을 엑셀에서 검색하여 일치하는거 있으면 삭제하기
        controlExcel.delete_stock(stockName)
        print(stockName)
    print("---------------------------------------------")

    # 코스닥 부분 처리
    for ticker in KOSDAQStockNumber:
        # 티커를 종목명으로 출력
        stockName = stock.get_market_ticker_name(ticker)
        # 해당 종목을 엑셀에서 검색하여 일치하는거 있으면 삭제하기
        controlExcel.delete_stock(stockName)
        print(stockName)
    print("---------------------------------------------")


# 오늘 날짜 가져오기(연,월,일)
todayInput = datetime.date.today().strftime("%Y%m%d")  # YYYYmmddHHMMSS 형태의 시간 출력

# 공매도 "거래 비중" top50을 가져와서 종목코드를 리스트 형태로 담는다
KOSPIShortVolume = stock.get_shorting_volume_top50(todayInput, "KOSPI")

# KOSPIShortVolume에 아무것도 안들어 있을 경우 계산을 위해 today 재정의
today = datetime.date.today()
# 뭔가 값이 있는 날짜로 선정될 때까지 하루씩 뒤로 가면서 반복한다(휴일이 있을 경우 대비)
while KOSPIShortVolume.size == 0:
    # 계속 하루씩 뒤로 가면서 검색한다
    today = today - datetime.timedelta(1)
    todayInput = today.strftime("%Y%m%d")
    KOSPIShortVolume = stock.get_shorting_volume_top50(todayInput, "KOSPI")

KOSDAQShortVolume = stock.get_shorting_volume_top50(todayInput, "KOSDAQ")
# 종목 코드를 바탕으로 종목명을 알아내고 엑셀에서 해당 종목이 있을 경우 삭제
print("****<거래 비중 기준>****")
check(KOSPIShortVolume, KOSDAQShortVolume)
print("거래 비중 기준 삭제 끝")
print("\n **검색 날짜 : " + todayInput + "***")

# volume에 데이터가 기록되는 날짜가 balance보다 빠르다
# 에: 20211011에는 volume에 데이터가 있을 수 있지만 balance에는 없을 수 있다
# 그래서 또다시 todayInput을 조절해줘야한다

# 공매도 "잔고" top50을 가져와서 종목코드를 리스트 형태로 담는다
KOSPIShortBalance = stock.get_shorting_balance_top50(todayInput, "KOSPI")
while KOSPIShortBalance.size == 0:
    # 계속 하루씩 뒤로 가면서 검색한다
    today = today - datetime.timedelta(1)
    todayInput = today.strftime("%Y%m%d")
    KOSPIShortBalance = stock.get_shorting_balance_top50(todayInput, "KOSPI")

KOSDAQShortBalance = stock.get_shorting_balance_top50(todayInput, "KOSDAQ")
print("****<잔고 기준>****")
check(KOSPIShortBalance, KOSDAQShortBalance)
print("잔고 기준 삭제 끝")
print("\n **검색 날짜 : " + todayInput + "***")