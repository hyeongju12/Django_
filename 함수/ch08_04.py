#제너레이터

# 1. 이터레이터를 만드는 함수

def seasons_generator(*args):
    for arg in args:
        yield arg # arg라는 값을 밖으로 리턴, 함수 실행을 지연시키고 다음 yield값을 리턴.. 전달 받은 인자 갯수 까지..

g = seasons_generator('spring', 'summer', 'autumn', 'winter')

print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
# print(g.__next__())

def func():
    print("첫번째 작업 중...")
    yield 1

    print("두번째 작업 중...")
    yield 2

    print("두번째 작업 중...")
    yield 3

ge = func()
data = ge.__next__()
print(data)

data = ge.__next__()
print(data)

data = ge.__next__()
print(data)
