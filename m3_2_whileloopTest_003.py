print("caseStudy: 점수 단순등급 계산")
print("m3_2_whileLoopTest_003.py")
print()
print("1. grade, score 변수 선언과 초기화")
print()
print("2. While 반복문")
print('    while True:  ')
print('         grade=""  ')
print('         score=int(input("   점수를 입력하세요 : "))  ')
print(' ')
print('         if 100 < score or score < 0 :  ')
print('             break  ')
print(' ')
print('         if score >= 90:    ')
print('             grade+="A"     ')
print('         elif score >= 80:  ')
print('             grade+="B"     ')
print('         elif score >= 70:  ')
print('             grade+="C"     ')
print('         elif score >= 60:  ')
print('             grade+="D"     ')
print('         else :     ')
print('             grade+="F"     ')
print(' ')
print('         print("   {0:2s}학점 입니다.".format(grade))  ')
print('         print()  ')
print()
print("3. 결과값->")
while True:
    grade=""
    score=int(input("   점수를 입력하세요 : "))

    if 100 < score or score < 0 :
        break

    if score >= 90:
        grade+="A"
    elif score >= 80:
        grade+="B"
    elif score >= 70:
        grade+="C"
    elif score >= 60:
        grade+="D"
    else :
        grade+="F"

    print("   {0:2s}학점 입니다.".format(grade))
    print()
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")