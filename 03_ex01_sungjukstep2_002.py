print("caseStudy: 알고리즘-성적표 학점 계산: 입력받아 계산 2단계 ")
print("03_ex01_sungjukstep2_001")
print("m3_2_whileLoopifElifElseTest")
print()
print("1. grade 변수 선언과 초기화:  #멈추려면 0을 입력한다.")
print('   grade = "" ')
grade = ""
print()
print("2. 여러 단계 조건을 실행하는 while 반복문: ")
print('   while True:')
print('       score =int(input("점수를 입력하세요 : "))')
print('       if score <= 0 :')
print('           break')
print('')
print('       if score >= 90:')
print('           grade +="A"')
print('       elif score >= 80:')
print('           grade +="B"')
print('       elif score >= 70:')
print('           grade +="C"')
print('       elif score >= 60:')
print('           grade +="D"')
print('       else :')
print('           grade +="F"')
print('  ')
print('       print("입력 점수는 {}학점 입니다.".format(grade)) ')
print('       print()   ')
print("3. 결과값->")
while True:
    score =int(input("점수를 입력하세요 : "))
    if score <= 0 :
        break

    if score >= 90:
        grade +="A"
    elif score >= 80:
        grade +="B"
    elif score >= 70:
        grade +="C"
    elif score >= 60:
        grade +="D"
    else :
        grade +="F"

    print("입력 점수는 {}학점 입니다.".format(grade))
    print()
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")