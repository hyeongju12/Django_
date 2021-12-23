# 이터레이터
# 1. 이터러블 객체
# 순서가 있는 자료형
# 문자열, 리스트, 튜플, 딕셔너리, range 객체

iter_obj = [10, 20, 30].__iter__()

print(dir(iter_obj))
print(iter_obj.__next__())
print(iter_obj.__next__())

# 이터레이터 객체 생성방법

class Seasons:
    def __init__(self):
        self.season_list = ['Spring', 'summer', 'autumn', 'winter']
        self.idx = 0
        self.max_num = 4

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.idx < self.max_num:
            curr_idx = self.idx
            self.idx += 1
            return self.season_list[curr_idx]
        else:
            raise StopIteration


# for i in Seasons():
#     print(i)

iter_obj = Seasons().__iter__()

print(dir(iter_obj.__next__))

print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())