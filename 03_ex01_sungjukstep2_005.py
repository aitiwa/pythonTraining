print("caseStudy: 알고리즘-여러 명의 성적표 학점 계산")
print("03_ex01_forloopIfElseTest")
print()
print("1. i, grade, score, score1 변수 선언과 초기화")
print('   grade = "" ')
print('   score = [100,95,90,85,80,75,70,65,60,55] ')
print('   score1 = [] ')
grade = ""
score = [100,95,90,85,80,75,70,65,60,55]
score1 = []
print()
print("2. 여러 단계 조건을 실행하는 반복문: ")
print('   for i in range(0, 10, 1):  ')
print('       score1 = score[i]  ')
print('       if  score1 >= 90:  ')
print('           grade ="A"     ')
print('       elif score1 >= 80: ')
print('           grade ="B"     ')
print('       elif score1 >= 70: ')
print('           grade ="C"     ')
print('       elif score1 >= 60: ')
print('           grade ="D"     ')
print('       else :             ')
print('           grade ="F"     ')
print(' ')
print('       remainder = score1 % 10 ')
print('       if score1 == 100:  ')
print('           grade += "+"   ')
print('       elif score1 < 60:  ')
print('           grade += ""    ')
print('       elif remainder >= 5 :  ')
print('           grade += "+"   ')
print('       else:  ')
print('           grade += "0"   ')
print(' ')
print('       print("{0:2d}번 학생은 {1:3d}점수이고 {2:2s}학점 입니다.".format(i + 1,score1, grade)) ')
print()
print("3. 결과값->")
for i in range(0, 10, 1):   #range(len(score)) : #
    # score = int(input("점수를 입력하세요 : "))
    score1 = score[i]
    if  score1 >= 90:
        grade ="A"
    elif score1 >= 80:
        grade ="B"
    elif score1 >= 70:
        grade ="C"
    elif score1 >= 60:
        grade ="D"
    else :
        grade ="F"

    remainder = score1 % 10
    if score1 == 100:
        grade += "+"
    elif score1 < 60:
        grade += ""
    elif remainder >= 5 :
        grade += "+"
    else:
        grade += "0"

    print("{0:2d}번 학생은 {1:3d}점수이고 {2:2s}학점 입니다.".format(i + 1,score1, grade))
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")