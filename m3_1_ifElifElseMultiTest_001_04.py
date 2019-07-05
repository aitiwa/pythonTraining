print("caseStudy: 학점 계산 - 중첩 조건문 4단계 - 변수 입력 받기")
print('m3_1_ifElifElseMultiTest_001_04\n')
print("1. score 변수 선언과 입력 받기: # 변수 값을 키보드에서 입력 받는다.")
print('   score = int(input("   점수를 입력하세요: "))  ')
score = int(input("   점수를 입력하세요: "))
print()
print("2. 여러 조건에 따라 실행하는 조건문: ")
print('    if score == 100:                 ')
print('        print("   A+", end="")       ')
print('    elif score >= 90:                ')
print('        result = score % 10          ')
print('        if result < 5:               ')
print('            print("   A0", end="")   ')
print('        else:                        ')
print('            print("   A+", end="")   ')
print('    elif score >= 80:                ')
print('        result = score % 10          ')
print('        if result < 5:               ')
print('            print("   B0", end="")   ')
print('        else:                        ')
print('            print("   B+", end="")   ')
print('    elif score >= 70:                ')
print('        result = score % 10          ')
print('        if result < 5:               ')
print('            print("   C0", end="")   ')
print('        else:                        ')
print('            print("   C+", end="")   ')
print('    elif score >= 60:                ')
print('        result = score % 10          ')
print('        if result < 5:               ')
print('            print("   D0", end="")   ')
print('        else:                        ')
print('            print("   D+", end="")   ')
print('    else:                            ')
print('        print("   F", end="")        ')
print('    print("학점 입니다.")            ')
print()
print("3. 결과값->")
if score == 100:
    print("   A+", end="")
elif score >= 90:
    result = score % 10
    if result < 5:
        print("   A0", end="")
    else:
        print("   A+", end="")
elif score >= 80:
    result = score % 10
    if result < 5:
        print("   B0", end="")
    else:
        print("   B+", end="")
elif score >= 70:
    result = score % 10
    if result < 5:
        print("   C0", end="")
    else:
        print("   C+", end="")
elif score >= 60:
    result = score % 10
    if result < 5:
        print("   D0", end="")
    else:
        print("   D+", end="")
else:
    print("   F", end="")
print("학점 입니다.")
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")