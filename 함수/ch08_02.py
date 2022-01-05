# 1. 내부함수
# 함수 안에 또다른 함수를 정의 할 수 있다.

def outer(name):
    def inner():
        print(name, "Hi")
    return inner

func = outer('startconding')
func()


def greeting(name, age, gender):
    def inner():
        print(name, "님 안녕하세요")
    return inner

clousure = greeting('nami', 'female', 27)
clousure()

print(dir(clousure.__closure__[0]))
print(clousure.__closure__[0].cell_contents)

# 이걸 왜 쓸까?
# 전역 변수를 사용해서 대체가 가능하다.
# 전역변수 사용을 최소화 하는 것이 좋다(네이밍 문제, 스코프 문제)

# but 클래스를 이용해서 대체가 가능하다.
