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
