#제너레이터 표현식
#소괄호를 사용하면 된다.
double_generator =(i * 2 for i in range(1, 10))

for i in double_generator:
    print(i)


# 3. 메모리 사용을 효율적으로 하기 위해서 사용
# ex) 숫자 1 - 10000 3배로 만든 결과 리스트 vs 제너레이터

import sys

list_data = [i * 3 for i in range(1, 10000 + 1 )]
generator_data = (i * 3 for i in range(1, 10000 + 1 ))

print(sys.getsizeof(list_data))
print(sys.getsizeof(generator_data))
# 리스트는 결과값을 메모리에 저장하고, 제너레이터는 결과값을 저장하지 않고, __next__호출 될떄마다 만들어 놓기 떄문.
# 대용량 처리는 제너레이터 

# 리스트 : 데이터 저장에 필요한 메모리를 모두 사용
# 제너레이터 : 나중에 필요할 때 값을 만들어 사용(메모리가 리스트 보다 적게 필요)