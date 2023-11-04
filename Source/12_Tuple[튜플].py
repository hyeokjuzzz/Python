###################################################################################
# # 튜플
# # 값이 한 번 초기화된 후 임의의 데이터를 할당할 수 없는 자료구조(자료집합, 상수)
# # 값의 변경을 하고 재배치하는 프로세스의 메모리를 소비하지 않으므로 리스트보다는 가볍다
# # 데이터가 변질되면 안되는 경우상수 형태의 튜플로 작성해 두면 오류를 방지할 수 있다
###################################################################################
# # 튜플의 선언
# score = 10,20,30,40,50
# print(type(score), score)

# score = (10,20,30,40,50) # 개발자들 사이에서 튜플은 ()를 통해 선언하는 것이 보편적이다
# print(type(score), score)

# score = 20 # 상수 형태로 생성이 가능
# print(type(score), score)


# # # 함수(메서드)의 반환 결과 : 튜플
# def DoSomething() :
#     return "첫번째 반환값", "튜플", 100, True

# result = DoSomething()
# # result[0] = "aaaa" 튜플로 전달받은 값은 변경할 수 없다



# # 함수 결과 반환 두번째
# def DoSomething() :
#     return "첫번째 반환값", "튜플", 100, True

# re1,re2,re3,re4 = DoSomething()
# print(type(re1), re1) # str
# print(type(re2), re2) # str
# print(type(re3), re3) # int
# print(type(re4), re4) # bool



# # # 리스트 => 튜플
# score = [10,20,30,40,50]
# tu = tuple(score)
# print(type(tu), tu)
# # # 튜플 => 리스트
# lists = list(tu)
# print(type(lists), lists)
