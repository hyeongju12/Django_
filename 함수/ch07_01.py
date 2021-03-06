# threading

import threading

# 스레드에서 실행할 함수
def work():
    print('[sub] start')
    keyword = input('[sub] 검색어를 입력하세요 >>>')
    print(f'[sub] {keyword}로 검색을 시작합니다..')
    print("[sub] end")


# 메인스레드 실행되는 부분
worker = threading.Thread(target = work)

#wprler.daemon = True이면 메인스레드 종료시 서브 스레드도 같이 종료된다.
worker.daemon = True
worker.start()

print("[main] 메인 스레드는 자기 할일을 합니다.")
print("[main] end")