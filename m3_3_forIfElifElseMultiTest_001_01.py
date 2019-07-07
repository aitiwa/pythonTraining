print("caseStudy: 학점 계산 - 반복 중첩 조건문 7단계 - 여러 점수 계산")
print("m3_1_forIfElifElseMultiTest_001_01_for")
print("1. score, score1 변수 선언과 초기화")
print('   score = [100,95,90,85,80,75,70,65,60,55]')
print('   score1 = []')
score = [100,95,90,85,80,75,70,65,60,55]
score1 = []
print()
print("2. 여러 조건에 따라 실행하는 반복문: ")
print('   for i in score:  #range(len(score)-1)                      ')
print(' ')
print('       print("   점수 {0:3d}점은 학점이 ".format(i), end="")  ')
print(' ')
print('       score1 = i   ')
print(' ')
print('       if score1 >100 or score1 < 0 :  ')
print('           print("범위에 해당하지 않는 값입니다.")  ')
print('           continue  ')
print(' ')
print('       if score1 == 100:  ')
print('           print("A+", end="")  ')
print('       elif score1 >= 90:  ')
print('           print("A", end="")  ')
print('       elif 90> score1 >= 80:  ')
print('           print("B", end="")  ')
print('       elif score1 >= 70:  ')
print('           print("C", end="")  ')
print('       elif score1 >= 60:  ')
print('           print("D", end="")  ')
print('       else:  ')
print('           print("F", end=" ")  ')
print(' ')
print('       if score1 == 100:  ')
print('           print("", end="")  ')
print('       elif (100 > score1 >= 60) and ((score1 % 10) >= 5) :  ')
print('           print("+", end="")  ')
print('       elif score1 < 60:  ')
print('           print("", end="")  ')
print('       else:  ')
print('           print("0", end="")  ')
print(' ')
print('       print("입니다.")  ')
print()
print("3. 결과값->")
for i in score:   #for i in score:   #
    print("   점수 {0:3d}점은 학점이 ".format(i), end="")

    score1 = i

    if score1 >100 or score1 < 0 :
        print("범위에 해당하지 않는 값입니다.")
        continue

    if score1 == 100:
        print("A+", end="")
    elif score1 >= 90:
        print("A", end="")
    elif 90> score1 >= 80:
        print("B", end="")
    elif score1 >= 70:
        print("C", end="")
    elif score1 >= 60:
        print("D", end="")
    else:
        print("F", end=" ")

    if score1 == 100:
        print("", end="")
    elif (100 > score1 >= 60) and ((score1 % 10) >= 5) :
        print("+", end="")
    elif score1 < 60:
        print("", end="")
    else:
        print("0", end="")

    print("입니다.")

print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")