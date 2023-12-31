###########################################################
# # 반복문 
# # 로직을 반복하여 수행한다.
# # FOR
# # 타 프로그래밍 언어의 foreach 와 구동원리가 똑같음
###########################################################
# # 1씩 증가하는 수를 표현할때
# print(1)
# print(2)
# print(3)
# print(4)
# # .....
# print(100)

# # print() 함수를 반복적으로 호출 하는 로직 을 반복문을 통하여 줄일수 있다. 
# # 파이썬 For 문의 range() : 정수 숫자의 범위 를 지정해 주는 기능.
# # range(1,101) : 1 ~ 100      1 이상 101 미만
# # range(101)   : 0 ~ 100
# for num in range(1,101) :
#     print(num,',',end='')
# print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# for num in range(101) :
#     print(num,',',end="")




# # 리스트 (컬렉션 : 특정 데이터 들을 열거하여 관리하는 데이터 유형)
# lists = [1,2,7,5,6]
# for i in lists :
#     print(i)

# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# for i in [1,2,3,4,5] :
#     print(i)



###################################################################
# 실습 1 : 1 ~ 100 사이의 수 중 짝수만 표현
###################################################################
# for i in range(2,101,2) :
#     print(i,',',end = '')






###################################################################
# 실습 2 : 1 ~ 100 사이의 수 중 3의 배수인 숫자의 모든 합을 구하시오.
###################################################################
#        [1,2,3,4,5,6,------ 100]
# sum = 0 # 모든 합을 누적 저장해 둘수 있는 외부 변수
# for i in range(1,101) :
#     if i % 3 == 0 :
#         print(i , " 는 3의 배수입니다.")
#         sum += i
# print(sum)         

 







 ##########################################################################
 # # 반복문 강제 종료 Break 
 # # 다음순번 처리 Continue
 # # 특정 조건에 따라 반복문을 제어 할 수 있다.
 ##########################################################################
# sum = 0 # 정수값 을 누적 변수 
# for num in range(0,101) :
#     if 30 < num < 40 :
#         print(num, ' 은 합산 되지 않고 다음 for 의 값을 처리합니다.')
#         continue
#     elif num % 3 == 0 : 
#         sum += num
#     elif num == 77 :
#         break
# print(sum)







#######################################################################
# # 이중루프 ( For in For)
# # 메인 For 에서 받아온 값을 기준으로 반복적으로 수행하는 로직을 구현 할 수 있다.
#######################################################################
# # 구구단 만들기
# # > 단수 (dan) 변수 를 2 ~ 9 까지 반복하고 
# #   행수 (hang) 변수 를 1 ~ 9 까지 반복해서
# #   각 단 수 별로 행 을 반복하여 곱한 값을 표현
# for dan in range(2,10) :
#     print('\n',dan, ' 단 입니다.')
#     for hang in range(1,10) : 
#         print(dan , ' * ' , hang, ' = ', dan*hang)



# # tringle 표현하기 
# # . 이중 루프를 이용한 * 삼각형 그리기 


# y : 피라미드의 행 을 변화,표현하는 변수 
# for y in range(1,10) :
#     for x in range(y) : 
#         print('*',end="")
#     print()



# # 위 로직은 아래 처럼 간단히 구현 할 수 있다.
# for y in range(1,10) :
#     print('*' * y)







########################################################################
# # While 
# # 특정 조건 을 만족 시킬때 로직을 수행한다.
########################################################################
# # 증가한 번호 가 5 이하일 경우만 로직을 실행 
# student = 1 
# while student <= 5 :
#     print(student, ' 번 학생입니다.')
#     student += 1 # 반드시 루프를 종료 시킬수 있는 조건 의 변화가 필요하다.

    

# # # while 의 continue 와 break 
# student = 0
# while student <= 20 :
#     student += 1 # 반드시 루프를 종료 시킬수 있는 조건 의 변화가 필요하다.
#     if 10 < student < 15 : 
#         student = 15
#         continue
#     elif student == 18 : 
#         break
#     print(student, ' 번 학생입니다.')
    
    








############################################################
# # 무한 루프 
# # 특정한 조건 없이는 끝나지 않고 반복하는 루프
############################################################
# # 프로그램이 구동되고 있는동안 현재 시간을 지속하여 1초 단위로 표현하는 예제
# from datetime import datetime
# import time

# while True :
#     print(datetime.now())
#     time.sleep(1) # 1초  



# # 특정 조건을 만족할 경우 무한 루프를 빠져나오는 로직을 구현
# # 종료해야 하는 범위가 지정되어있지 않는 프로세스의 종료를 구현하고자 할때
# print('3 + 7 = ? ')
# while True:
#     result = input("정답은 ? ")
#     if (int(result) == 10) : break 
# print("Good")



####################################################
# # 실습 1 
# # While , 1 ~ 200 , 3의배수 표현, 누적 합계. 
####################################################
# num = 1 # 1 ~ 200 을 반복할 숫자.
# sum = 0 # 누적 합계.
# while num <= 200 :
#     # num += 1 # num 이 0 부터 시작하는경우 
#     if num % 3 == 0 :
#         print(num,end=',')
#         sum += num
#     num += 1



##############################################################
# # 실습 : 오른쪽에서 일정한 별의 개수를 채우는 피라미드를 만드세요
##############################################################

# # y : 공백과 별을 나타낼 행의 번호. 
# for y in range(1,11) :
#     # 현재 행 공백의 개수
#     print(' ' * (10 - y),end='')
#     # 현재 행 별의 개수
#     print("*" * y)







##########################################################
# # 실습 3 
# # 중간에서 부터 일정한 패턴만큼 증가하는 별의 피라미드 만들기 
##########################################################

# # y : 피라미드를 나타낼 행의 번호 
# for y in range(1,11) : 
#     # 공백의 개수 표현
#     print(' ' * (10 - y), end = '')
#     # 별의 개수 표현
#     print("*" * (y * 2 -1)) 







################################################################
# # 실습 4 
# # 0 부터 9999 까지 수중 6이 들어있지 않은 수의 개수를 구하세요.
################################################################
# 6이 포함되어있지 않은 정수의 개수 누적
# count = 0 

# for num in range(0,10000) :
#     f = str(num)
#     if '6' not in f :
#         count += 1

# print(count)
