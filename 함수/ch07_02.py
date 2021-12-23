import threading
import time

# 주식 자동매매
# 매수, 매도


# 매수 스레드
def buyer():
    for i in range(5):
        print("[매수] 데이터 요청 중...")
        time.sleep(1)
        print("[매수] 데이터 분석 중...")
        time.sleep(1)
        print("[매수] 지금이 매수타이밍!...")
        time.sleep(1)
        print("[매수] 풀매수!..")
        time.sleep(1)

# 매도 스레드
def seller():
    for i in range(5):
        print("[매도] 데이터 요청 중...")
        time.sleep(1)
        print("[매도] 데이터 분석 중...")
        time.sleep(1)
        print("[매도] 지금이 매도 타이밍!...")
        time.sleep(1)
        print("[매도] 풀 매도!..")
        time.sleep(1)

# 메인 스레드
print("[메인] start")
buyer = threading.Thread(target=buyer)
seller = threading.Thread(target=seller)
buyer.start()
seller.start()

buyer.join() # 매수 스레드가 종료될떄까지 메인 스레드가 기다림
seller.join() # 매수 스레드가 종료될떄까지 메인 스레드가 기다림
print("[메인] 장이 종료 되었습니다.")

# 동시성 처리에 대한 추가 공부 필요