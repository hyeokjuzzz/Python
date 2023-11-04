#########
# # enumerate()함수
# # 순서 아 값을 순차적으로 반환하는 함수

# # 이부 변수를 이용하여 현재 루프의 순번 찾아내기
# lists = [10,20,30,40,50]
# iCnt = 0
# for num in lists:
#     iCnt += 1
#     print(iCnt, " 번째의 숫자는 ", num)
    

# # # enumerate(lists, 1) # lists를 인자로, 1부터 1씩 증가하는 값을 반환한다
# for no, value in enumerate(lists, 1):
#     print(no, " 번째의 숫자는 ", value)


# # n개의 컬렉션 합치기 Zip
# # 쌍이 밪는 개수만큼만 반환
# yoil = ["월", "화", "수", "목", "금", "토", "일"]
# food = ["짜장면", "볶음밥", "돈까스", "삼겹살"]
# menu = zip(yoil, food) # yoil 리스트와 food 리스트를 1:1로 매칭
# print(menu) # <zip object at 0x000002CCA1C82540>이 출력됨, 데이터를 출력하는 기능이 구현되어 있지 않다
# for y, f in menu:
#     print("%s 요일의 음식은 %s입니다" %(y,f))


# # zip 객체를 dict 객체로 변환하기
# yoil = ["월", "화", "수", "목", "금", "토", "일"]
# food = ["짜장면", "볶음밥", "돈까스", "삼겹살"]
# menu = dict(zip(yoil, food)) # zip의 결과를 dict 형태로 변환 가능
# print(menu) # dict 형태는 데이터 출력 기능이 구현되어 있다.
# 출력문 : {'월': '짜장면', '화': '볶음밥', '수': '돈까스', '목': '삼겹살'}



# # Any()와 All()
# # any() : 하나라도 True이면 True
# # all() : 모두 다 True여야 True
# lists = [True, True, False]
# print(any(lists)) # True
# print(all(lists)) # False


# # filter()
# # 함수와 리스트를 인자로 전달받아서 True인 결과만 리스트로 생성하여 반환
# # 함수의 return은 True/False이여야 한다
# def MyFunction(s):
#     return s < 60 # bool 반환 유형

# lists = [20,30,40,50,60,70,80]
# lists2 = filter(MyFunction, lists)
# print(lists2) # <filter object at 0x0000026F732CAD70>출력됨, 출력 기능이 구현되어 있지 않다
# for value in lists2:
#     print(value, end = ",")


# # map()
# # 함수와 리스트를 인자로 받아서 연산의 결과를 리스트로 생성
# def half(s) :
#     return s/2

# score = [45,46,47,48,48,60]
# for value in map(half, score):
#     print(value, end = ",")


# # map을 이용한 연산처리 예제
# def f_sum(v1,v2) :
#     return v1 + v2

# score1 = [45,46,47,48,48,60]
# score2 = [22,33,44,55] # 원소의 쌍이 같은 데이터만 처리하여 반환(score2의 개수만큼 반환됨)
# for value in map(f_sum,score1,score2):
#     print(value, end = ",")


# # f_sum : 함수의 이름
# # 함수 이름을 제외한 함수의 기능만 설명하는 것을 메서드(함수)의 시그니처
# # (v1,v2) 인자
# # return v1 + v2 반환하는 식
# def f_sum(v1, v2):
#     return v1 + v2

# def (v1, v2): # 무명 메서드 / 빨간 줄 뜸!
#     return v1 + v2
# # 람다 : 함수의 이름을 제외한 메서드 시그니처만 가지고 기능을 할 수 있도록 도와주는 기능



#################################################################################################
# # Lambda
# # 이름이 없는 메서드(무명메서드)를 간결하게 작성해서 사용할 수 있도록 하는 문법(기능)
# # 재사용을 하지 않는 로직일 경우(2번 이상 사용하지 않는다) 메서드를 굳이 작성할 필요가 없다
# # 함수를 전달받는 인자가 있을 경우 재사용을 하지 않는 메서드는 람다로 간결하게 구성하여 전달할 수 있다
#################################################################################################
# # 메서드의 시그니처
# # 메서드의 이름을 제외한 인자유형, 반환 유형을 메서드의 시그니처라고 한다
# # 람다는 함수의 이름을 제외하고 함수를 전달 받는 인자에게 메서드의 시그니처만 전달하는 유형


# # 람다의 구현 예제
# def Myfunchion_anClass(func, v1, v2) : # 외부에서 작성한 개발자가 접근할 수 없는 메서드(함수)
#     return func(v1, v2)


# # # Myfunction_anClass를 사용하는 개발자가 호출할 때
# # # 사용하는 형식 : Myfunchion_anClass(함수, 값, 값)
# def mf(v,s):
#     return v + s

# # print(Myfunchion_anClass(mf, 10, 20))
# print(Myfunchion_anClass(lambda x,y : x + y, 10, 20)) # 위 코드와 같은 결과
# # 함수를 만들 필요 없이 람다로 생성하여 호출한다

# # filter 함수의 lambda
# # 함수를 받기로 약속되어 있는 클래스
# score = [10,20,30,40,50]
# for num in filter(lambda x : x == 20, score):
#     print(num)
# for num in filter(lambda x : x % 8 == 0, score):
#     print(num)



############################################
# # 실습
# # 아래 map 클래스의 기능을 f_sum 기능을 사용하지 않고 lambda를 통해 간략히 구현해보세요
#####################################################################################
# def f_sum(v1,v2) :
#     return v1 + v2

# score1 = [45,46,47,48,48,60]
# score2 = [22,33,44,55] # 원소의 쌍이 같은 데이터만 처리하여 반환(score2의 개수만큼 반환됨)
# for value in map(f_sum,score1,score2):
#     print(value, end = ",")
# score1 = [45,46,47,48,48,60]
# score2 = [22,33,44,55]

# for num in map(lambda x, y : x + y, score1, score2):
#     print(num)



#######리스트의 얕은 복사
# # 리스트를 직접 변수에 할당할 경우 참조 형식으로 데이터 주소를 전달한다.
# # 원본과 데이터를 공유한다
# score = [45,50,4,5,6,7,9]
# score_back = score
# score_back[0] = 10
# print(score_back)
# print(score) # 얕은 복사로 인해 데이터가 변질된 것을 확인할 수 있다

####### 리스트의 깊은 복사 1
# score = [45,50,4,5,6,7,9]
# score_back = score.copy() # 원본 리스트의 깊은 복사
# print(score) # 깊은 복사로 인해 원본 데이터의 변질을 막을 수 있다


######깊은 복사 2
# score = [45,50,4,5,6,7,9]
# score_back = score.copy[:] # 범위 지정을 통한 원본 리스트의 깊은 복사
# score_back[0]
# print(score_back)
# print(score)


######중첩 리스트의 깊은 복사
# import copy # 복사를 위한 상세한 기능이 모여있는 외부 모듈

# score = [45,[10,20,30],50,4,5,6,7,9]
# score_back = score.copy() # 중첩 리스트의 경우 copy 메서드로는 깊은 복사를 할 수 없다
# score_back = copy.deepcopy(score)
# score_back[1][1] = 0
# print(score_back)
# print(score)


####### 같은 메모리를 참조하고 있는지(같은 메모리 주소를 공유하고 있는지) 확인
# # is 연산자
# list1 = [10,20,30]
# list2 = list1 # 얕은 복사
# list3 = list1.copy() # 깊은 복사
# print("list1과 list2는 같은 주소를 바라보고 있나요? :", list1 is list2)
# print("list2와 list3은 같은 주소를 바라보고 있나요? :", list2 is list3)
# print("list1과 list3은 같은 주소를 바라보고 있나요? :", list1 is list3)



################3변수의 참조 변경
# # str, int 유형의 데이터는 값형식
# # 파이썬의 경우 값형식이라도 데이터 주소를 공유
# a = "가"
# b = a
# print("a 와 b는 같은 주소를 바라보고 있나요? :", a is b) # True
# b = "나"
# print(a)
# print(b)


##########
# # 실습
# # 1. 1 ~ 10 정수의 리스트 a 와 각 정수의 제곱 리스트 b 를 만든 후
# # 두 리스트 를 합쳐 사전으로 만들어 사전에서 6의 제곱값을 검색해 출력하는 로직을 구현
##################################################################################
a = [1,2,3,4,5,6,7,8,9,10]
b = []
num = 1
for i in range(10):
    b.append(int(num ** 2))
    num += 1
print(b)
