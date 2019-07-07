print("caseStudy: 알고리즘-성적표 학점 계산: 입력받아 계산 3단계 0+와 부여")
print("03_ex01_sungjukstep2_003")
print("ifElifElseTest")
print()
"""
# [실습]
# 성적처리 구현 - 방법 2
# 성적을 입력받아 학점을 부여한는데 각 학점에 +와 0학점을 부여하고자 합니다.
# 예를 들어 A+, A0 학점을 95점부터 100점까지는 A+학점을 부여하고
# 90점부터 94점까지는 A0학점을 부여하고 같은 방법으로 B+, B0, C+, C0, D+, D0, F 학점을
# 부여하고자 할 때 각 if 구문에 +와 0학점을 부여하는 코드로 작성하시오.
# 
# 03_02_whileloopTest_003의 코드에서 각 레벨의 '+'와 '0'학점을 결정하는 코드가 중복
# 코딩되어 있다. A, B, C, D 학점마다 같은 로직이 중복해서 이용되는 것을 피할 수 있도록
# 수정하는 코드를 작성하시오.
# 
# <요구사항>
# - 점수는 0 ~ 100 사이의 점수만 입력되었다고 가정하고 코딩하세요.
# - 입력된 점수가 100점인 경우 A+ 학점으로 출력되는지 확인하세요.
# - 다음과 같은 구조로 코딩하시오.
#     if 조건1:   
#     elif   
#     elif...
# 
#     if 조건2
#     else
"""
print("1. score 변수 선언과 초기화:  ")
print('   grade = "" ')
print('   score=int(input("   점수를 입력하세요 : "))')
grade = ""
score=int(input("   점수를 입력하세요 : "))
print()
print("2. 여러 단계 조건을 실행하는 중첩 조건문 ")
print('   if  score == 100 :       ')
print('       grade="   A+"        ')
print('   elif score >=  90:       ')
print('       remainder = score % 10     ')
print('       if remainder < 5 :         ')
print('            grade="   A0"   ')
print('       else :               ')
print('            grade="   A+"   ')
print('   elif score >= 80:        ')
print('       remainder = score % 10     ')
print('       if remainder < 5 :         ')
print('            grade="   B0"      ')
print('   else :                   ')
print('        grade="   B+"       ')
print('   elif score >= 70:        ')
print('       remainder = score % 10        ')
print('       if remainder < 5 :            ')
print('            grade="   C0"      ')
print('   else :                   ')
print('        grade="   C+"       ')
print('   elif score >= 60:        ')
print('       remainder = score % 10     ')
print('       if remainder < 5 :         ')
print('            grade="   D0"   ')
print('       else :               ')
print('            grade="   D+"   ')
print('   else :                   ')
print('       grade="   F"            ')
print('                            ')
print('   print("{}학점 입니다.".format(grade))    ')
print('   print()                                  ')
print()
print("3. 결과값->")
if  score == 100 :
    grade="   A+"
elif score >=  90:
    remainder = score % 10
    if remainder < 5 :
         grade="   A0"
    else :
        grade="   A+"
elif score >= 80:
    remainder = score % 10
    if remainder < 5 :
         grade="   B0"
    else :
        grade="   B+"
elif score >= 70:
    remainder = score % 10
    if remainder < 5 :
         grade="   C0"
    else :
        grade="   C+"
elif score >= 60:
    remainder = score % 10
    if remainder < 5 :
         grade="   D0"
    else :
        grade="   D+"
else :
    grade="   F"

print("{}학점 입니다.".format(grade))
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")