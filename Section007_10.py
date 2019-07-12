print("Section007 알고리즘-소수 판별")
print("Section007_10.py")
print("m3_2_forloopIfTest")
print()
print("1. N, SUM 변수 선언과 초기화: ")
print('   A = int(input("   소수를 판별할 숫자 입력: "))     ')
print("   i = A - 1   ")
print("   j = 2   ")
A = int(input("   소수를 판별할 숫자 입력: "))
i = A - 1
j = 2
print()
print("2. 조건을 포함한 반복 실행하는 반복문: ")
print('   for j in range(2,A,1) :           ')
print('       if j < i :                    ')
print('           if A%j == 0 :             ')
print('               decimal = False       ')
print('               break                 ')
print('           else:                     ')
print('               decimal = True        ')
print('       else:                         ')
print('           decimal = True            ')
for j in range(2,A,1) :
    # print(j,A,(A%j))    #검증용
    if j < i :
        if A%j == 0 :
            decimal = False
            break
        else:
            decimal = True
    else:
        decimal = True
print("3. 결과값->")
print("   decimal = ", decimal)
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")