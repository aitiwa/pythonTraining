print("caseStudy: 학점 계산 - 중첩 조건문 6단계 - print를 grade변수화")
print('m3_1_ifelifelsemultiTest_001_06\n')
print("1. grade, score 변수 선언과 초기화:  ")
print('   grade = "" ')
print('   score=int(input("   점수를 입력하세요 : "))')
grade = ""
score=int(input("   점수를 입력하세요 : "))
print()
print("2. 여러 단계 조건을 실행하는 중첩 조건문 ")
print('   if  score == 100 :       ')
print('       grade="   A+"        ')
print('   elif score >=  90:       ')
print('       result = score % 10  ')
print('       if result < 5 :      ')
print('            grade="   A0"   ')
print('       else :               ')
print('            grade="   A+"   ')
print('   elif score >= 80:        ')
print('       result = score % 10  ')
print('       if result < 5 :      ')
print('            grade="   B0"   ')
print('   else :                   ')
print('        grade="   B+"       ')
print('   elif score >= 70:        ')
print('       result = score % 10  ')
print('       if result < 5 :      ')
print('            grade="   C0"   ')
print('   else :                   ')
print('        grade="   C+"       ')
print('   elif score >= 60:        ')
print('       result = score % 10  ')
print('       if result < 5 :      ')
print('            grade="   D0"   ')
print('       else :               ')
print('            grade="   D+"   ')
print('   else :                   ')
print('       grade="   F"         ')
print('                            ')
print('   print("{}학점 입니다.".format(grade))    ')
print('   print()                                  ')
print()
print("3. 결과값->")
if  score == 100 :
    grade="   A+"
elif score >=  90:
    result = score % 10
    if result < 5 :
         grade="   A0"
    else :
        grade="   A+"
elif score >= 80:
    result = score % 10
    if result < 5 :
         grade="   B0"
    else :
        grade="   B+"
elif score >= 70:
    result = score % 10
    if result < 5 :
         grade="   C0"
    else :
        grade="   C+"
elif score >= 60:
    result = score % 10
    if result < 5 :
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