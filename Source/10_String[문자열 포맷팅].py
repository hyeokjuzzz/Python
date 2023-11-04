##################################################################
# # 포맷팅 : 문자열 안에 세부 정보를 포함하여 출력하도록 명령하는 기능
# # 문자열 사이에 특정 정보를 삽입하여 하나의 문자열을 만들어내는 기능
##################################################################
# # 표식의 사용 예제
# station = "구로"
# direction = False

# print("이번역은 %s 역 입니다. 내리실 문은 %s 입니다." %(station, '왼쪽' if direction else "오른쪽"))


# # 문자열의 서식
# # 정렬을 지정
# value = 123
# print("###%d###" %value) # 출력 : ###123###
# print("###%5d###" %value) # 출력 : ###  123###(#을 포함해서 앞에 5글자)
# print("###%3d###" %value) # 출력 : ###123###(이미 #으로 3칸을 차지하므로 공백 표현X)


# # 숫자의 경우 오른쪽 정렬이 기본
# price = [30,13500,2000]
# for p in price:
#     print("가격 : %10d원" %p)
# for p in price:
#     print("가격 : %-10d원" %p)


# # 실수의 포맷
# pie = 3.14159265
# print("%8f" %pie)
# print("%8.3f" %pie) # 총 8개의 실수를 표현하는데 소수점 4자리에서 반올림
# print("%-8.3f" %pie) # 총 8개의 실수를 표현하는데 소수점 4자리에서 반올림(왼쪽정렬)

#######################3
# # 신형 포맷팅(문자열의 보간 : 누락/빈곳을 채워넣음)
##########3
# # { } 중괄호 내의 문자열 가공
# Id          = "ADMIN"
# MailAddress = "gubean9@gmail.com"
# Name        = "관리자"

# print("이름 : {}, ID : {}, 메일 주소 : {}".format(Name, Id, MailAddress))

# # index를 통해 인수의 순서를 배치할 수 있다
# Id          = "ADMIN"
# MailAddress = "gubean9@gmail.com"
# Name        = "관리자"

# print("이름 : {2}, ID : {0}, 메일 주소 : {1}".format(Id, MailAddress, Name))

# # {} 중괄호 안에 변수 이름을 적어두고 키워드로 값을 나열할 수 있다
# print("이름 : {Name}, ID : {Id}, 메일 주소 : {MailAddress}".format(Id          = "ADMIN",
# MailAddress = "gubean9@gmail.com",
# Name        = "관리자"))

# # Key와 Value를 가지는 자료형(Dic)을 생성하여 매핑할 수 있다
# # ID, Name, MailAddress를 관리하는 3개의 요소가 등록된 사전
# User = {"ID" : "ADMIN",
#         "Name" : "관리자",
#         "MailAddress" : "gubean9@gmail.com"} # 붙여서 써도 괜찮은데 가독성을 위해서 띄워둠
# print("이름 : {0[Name]}, 아이디 : {0[ID]}, 메일 주소 : {0[MailAddress]}".format(User))

# # 서식 지정
# Age = 24
# Name = "관리자"
# Height = 177.12

# print("이름 : {2:10s}, 아이디 : {0:5d}, 메일 주소 : {1:8.2f}".format(Age, Height, Name))



####################3
# # 실습
# # 1. "차종 : 코란도C, 제조사 : 쌍용, 배기량 : 1998" 문자열에서 제조사만 추출하여 출력하세요
#####################
# 차종 = "코란도C"
# 제조사 = "쌍용"
# 배기량 = 1998

# print("{}".format(제조사))

# 풀이
# value = "차종 : 코란도C, 제조사 : 쌍용, 배기량 : 1998"
# print(value[16:19])



##############
# # 실습
# # 2. 임의의 주민등록번호 13자리를 입력받아 현재 나이와 성별을 출력하는 프로그램을 작성해보세요
#############33
# number = input("주민등록번호를 입력하세요 : ")

# if (number != 13):
#     print("주민등록번호는 13자리로 입력하세요")

# 풀이
# while True:
#     identity = input("주민등록번호를 입력하세요 : ").replace("-", "").replace(" ", "")

#     ########33 벨리데이션 : 검증 로직 먼저 수행 ############################
#     if not identity.isnumeric(): # 숫자를 입력하지 않은 경우 리턴
#         print("숫자만 입력하세요")
#         continue
#     ## 숫자만 입력되어 있는 상태
#     elif len(identity) != 13:
#         print("주민등록번호는 13자리로 입력하세요")
#         continue
#     #################3
#     # 정상적으로 데이터를 받았기 때문에 비교하는 로직
#     result = "성별 : "
#     gender = identity[6] #0007314444444
#     if gender == "1" or gender == "3" : result += "남자"
#     elif gender == "2" or gender == "4" : result += "여자"
#     else :
#         print("성별을 확인할 수 없습니다.")
#         continue
#     age = int(identity[:2])
#     result += "%d살입니다" %  (23 + (100 - age))   if age > 23 else    (23 - age)
#     print(result)
#     break
