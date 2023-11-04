#########################################################
# # 문자열 (문자가 열거 된 형태)
# # . 문자들을 일렬로 나열시켜 순서에 맞게 index 를 부여한 형태
##########################################################
# svalue = 'Python'
# print(svalue[4])
# print(svalue[-2])

# for char in svalue :
#     print(char,end="")


# # 문자열을 나타내는 범위 를 지정하여 문자를 추출 
# # len() : 열거형 데이터 의 개수 를 구할 수 있는 함수.
# for index in range(1,len(svalue)) :
#     print(svalue[index], end = '')



# # 문자열의 index 로 문자를 변경 할수 없다. 
# svalue[1] = 'p'

###############################################################################
# # 불변 객체 (immuteable)
# # 데이터를 새로 갱신하여 재 배치 하는 프로세스 보다 메모리 손실을 감안 하더라도
# # 새로운 메모리 영역에 데이터를 할당하는것이 더 효율적이기 때문에 사용
###############################################################################
# svalue = "안녕하세요"    # "안녕하세요"  메모리 등록
# svalue += " 반갑습니다." #  "안녕하세요 반갑습니다" 메모리 등록
# print(svalue)

# # stringIO 모듈 
# # 불변객체인 str 의 메모리 손실을 효율적으로 동작할수있도록 해주는 모듈
# # 다소 코딩이 복잡하지만 대용량 의 데이터를 관리할때는 필수(중요)
# from io import StringIO
# bf = StringIO()
# bf.write("안녕하세요")
# bf.write("반갑습니다.")
# result = bf.getvalue()
# bf.close()
# print(result)



########################################################################
# # 문자열 슬라이스 (범위 지정)
########################################################################
# svalue = 'Python.py'
# print(svalue[2:5])  # 2~ 4 인덱스 문자 추출  tho
# print(svalue[3:])  # 3 ~ 마지막 까지 hon.py
# print(svalue[:4]) # 0 ~ 3 index 까지  Pyth
# print(svalue[2:-3]) # 2 ~ (-3 -1 ) = -4 index 까지표현   thon
# print(svalue[-3:])  # -3 문자열 부터 끝까지 표현 (확장자 추출) .py


# # 건너뛰면서 문자를 추출하는 기능
# print(svalue[::2])  # 0 부터 2step : Pto.y
# print(svalue[::-2]) #  마지막 index 무터 -2 칸씩 들여서 표현 y.otP
# print(svalue[2::2]) # 2 부터 2step
# print(svalue[-2::-2])  # -2 index 로부터 2칸씩 들여서 표현
# print(svalue[::-1])  # 문자열 반전
# print(svalue[2:8:2])  # 2 ~ 7 까지 2step




#########################################################################
# # 문자열 메서드
# # 문자열을 다룰 수 있도록 만들어 둔 클래스에서 제공하는 문자열 클래스 의 기능(Function)
########################################################################
# svalue = "Python Programming"
# print(svalue.find('o')) # 0 index 부터 가장 가까운 o 의 index 를 반환 (없으면 -1)
# print(svalue.rfind('og')) # 마지막 index 부터 처음 나타나는 'og' 의 o index 를 반환
# print(svalue.index('o')) # 왼쪽에서 찾는다 없으면 오류
# print(svalue.count('n')) # n 문자열의 개수를 반환한다.

# # 메서드가 반환하는 데이터 타입은 int
# print(svalue.count('n') , type(svalue.count('n')))

# # 2023.01 ~ 현재까지 안동시 연령별 성비 확인
# # 통계 데이터 에서 '남자' 데이터 의 개수를 확인할때.
# if svalue.count('남자') > svalue.count('여자') :
#     pass







# # 문자열을 포함하는지 확인.
# svalue = "Python Programming"
# if 'P' in svalue :   
#     print("대문자 P는 포함되어있습니다.")
# if 'p' not in  svalue : 
#     print("소문자 p 는 포함되어있지 않습니다.")




# # 삼항 연산자 ( 조건의 참 / 거짓의 로직을 한줄로 표현 )
# # [참 인경우의 로직 ]  if 조건 else [거짓인경우 로직]
# svalue = "Python Programming"
# print('m이 있습니다.'  if 'm' in svalue  else 'm이없습니다.'  )





# # 해당 문자열로 시작 / 종료 하는지 확인.
# svalue = "Python Programming.jpg"

# # startwith 시작 하는지 확인. 
# print('Python 관련 데이터 입니다.'  # 참
#       if svalue.startswith("Python")  # 조건
#       else "Python 데이터가 아닙니다.") # 거짓


# # # endwith 종료 하는지 확인 (프로그램의 확장자 찾을때 용이.)
# print('jpg 형식입니다.'  # 참
#       if svalue.endswith(".jpg")  # 조건
#       else "jpg 형식이 아닙니다.") # 거짓
