print("caseStudy: 알고리즘-성적표 학점 계산: 입력받는 계산 3단계 0+와 부여 중복제거")
print("03_ex01_sungjukstep2_004.py")
print("ifElifElseTest")
print()
print("1. grade 변수 선언과 초기화")
print('   grade = "" ')
print('   score=int(input("   점수를 입력하세요 : "))  ')
grade=""
score=int(input("   점수를 입력하세요 : "))
print()
print("2. 여러 단계 조건을 실행하는 조건문: ")
print('    if  score >=  90:  ')
print('        grade="A"  ')
print('    elif score >= 80:  ')
print('        grade="B"  ')
print('    elif score >= 70:  ')
print('        grade="C"  ')
print('    elif score >= 60:  ')
print('        grade="D"  ')
print('    else :  ')
print('        grade="F"  ')
print(' ')
print('    remainder = score % 10  ')
print('    if score == 100:  ')
print('        grade += "+"  ')
print('    elif score < 60:  ')
print('        grade += ""   ')
print('    elif remainder >= 5 :  ')
print('        grade += "+"  ')
print('    else:  ')
print('        grade += "0"  ')
print(' ')
print('    print("   {0:2s}학점 입니다.".format(grade))  ')
print()
print("3. 결과값->")
if  score >=  90:
    grade="A"
elif score >= 80:
    grade="B"
elif score >= 70:
    grade="C"
elif score >= 60:
    grade="D"
else :
    grade="F"

remainder = score % 10
if score == 100:
    grade += "+"
elif score < 60:
    grade += ""
elif remainder >= 5 :
    grade += "+"
else:
    grade += "0"
print("   {0:2s}학점 입니다.".format(grade))
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")