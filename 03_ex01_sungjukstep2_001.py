print("caseStudy: 알고리즘-성적표 학점 계산: 입력받아 계산 1단계 ")
print("03_ex01_sungjukstep2_003")
print("03_ex01_ifElifElseTest")
print()
print("1. score 변수 선언과 초기화: ")
print('   score=int(input("   점수를 입력하세요 : "))')
score=int(input("   점수를 입력하세요 : "))
print()
print("2. 여러 단계 조건을 실행하는 조건문: ")
print('   if  score == 100 :                    ')
print('       print("   A+", end = "")          ')
print('   elif score >=  90:                    ')
print('       remainder = score % 10               ')
print('       if remainder < 5 :                   ')
print('           print("   A0", end="")        ')
print('       else :                            ')
print('           print("   A+", end="")        ')
print('   elif score >= 80:                     ')
print('       remainder = score % 10               ')
print('       if remainder < 5 :                   ')
print('           print("   B0", end="")        ')
print('       else:                             ')
print('           print("   B+", end="")        ')
print('   elif score >= 70:                     ')
print('       remainder = score % 10               ')
print('       if remainder < 5 :                   ')
print('           print("   C0", end="")        ')
print('       else:                             ')
print('           print("   C+", end="")        ')
print('   elif score >= 60:                     ')
print('       remainder = score % 10               ')
print('       if remainder < 5 :                   ')
print('           print("   D0", end="")        ')
print('       else:                             ')
print('           print("   D+", end="")        ')
print('   else :                                ')
print('       print("   F", end="")             ')
print(' ')
print("3. 결과값->")
if  score == 100 :
    print("   A+", end = "")
elif score >=  90:
    remainder = score % 10
    if remainder < 5 :
        print("   A0", end="")
    else :
        print("   A+", end="")
elif score >= 80:
    remainder = score % 10
    if remainder < 5 :
        print("   B0", end="")
    else:
        print("   B+", end="")
elif score >= 70:
    remainder = score % 10
    if remainder < 5 :
        print("   C0", end="")
    else:
        print("   C+", end="")
elif score >= 60:
    remainder = score % 10
    if remainder < 5 :
        print("   D0", end="")
    else:
        print("   D+", end="")
else :
    print("   F", end="")
print("학점 입니다.")
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")