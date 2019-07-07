print("caseStudy: 학점 계산 - 반복 중첩 조건문 8단계 - 여러 점수 계산")
print("m3_1_forIfElifElseMultiTest_001_02")
print("1. score, score1 변수 선언")
print('   score = [100,95,90,85,80,75,70,65,60,55]')
print('   score1 = []')
score = [100,95,90,85,80,75,70,65,60,55]
score1 = []
print()
print("2. 여러 조건에 따라 실행하는 반복문: ")
print('    for i in score:  #range(len(score)-1)   ')
print(' ')
print('        print("   점수 {0:3d}점은 학점이 ".format(i), end="") ')
print(' ')
print('        score1 = i  ')
print(' ')
print('        if score1 >100 or score1 < 0 :  ')
print('            print("범위에 해당하지 않는 값입니다.")  ')
print('            continue        ')
print(' ')
print('        if score1 >= 90:    ')
print('            grade = "A"     ')
print('        elif score1 >= 80:  ')
print('            grade = "B"     ')
print('        elif score1 >= 70:  ')
print('            grade = "C"     ')
print('        elif score1 >= 60:  ')
print('            grade = "D"     ')
print('        else:               ')
print('            grade = "F"     ')
print(' ')
print('        result = score1 % 10  ')
print('        if score1 == 100:     ')
print('            grade += "+"      ')
print('        elif score1 < 60:     ')
print('            grade += ""       ')
print('        elif result >= 5:     ')
print('            grade += "+"      ')
print('        else:                 ')
print('            grade += "0"      ')
print(' ')
print('        print("{0:2s}학점 입니다.".format(grade))  ')
print()
print("3. 결과값->")
for i in score:  #range(len(score)-1)

    print("   점수 {0:3d}점은 학점이 ".format(i), end="")

    score1 = i

    if score1 >100 or score1 < 0 :
        print("범위에 해당하지 않는 값입니다.")
        continue

    if score1 >= 90:
        grade = "A"
    elif score1 >= 80:
        grade = "B"
    elif score1 >= 70:
        grade = "C"
    elif score1 >= 60:
        grade = "D"
    else:
        grade = "F"

    result = score1 % 10
    if score1 == 100:
        grade += "+"
    elif score1 < 60:
        grade += ""
    elif result >= 5:
        grade += "+"
    else:
        grade += "0"

    print("{0:2s}학점 입니다.".format(grade))

print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")