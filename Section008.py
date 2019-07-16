print("Section007 알고리즘-소수 판별-제곱근 이용")
print("Section007_30.py")
print("m3_2_forloopIfTest")
print()
import math
print("1. A, i 변수 선언과 초기화: ")
print('   A = int(input("   소수를 판별할 숫자 입력: "))     ')
print("   i = 2                             ")
print("   decimal = True                    ")
A = int(input("   소수를 판별할 숫자 입력: "))
i = 2
decimal = True
print()
print("2. 조건을 포함한 반복 실행하는 반복문: ")
print('   for j in range(2,A,1) :             ')
print('       if i <= math.sqrt(A):           ')
print('           if A%i == 0:                ')
print('               decimal = False         ')
print('               break                   ')
print('           else:                       ')
print('               decimal = True          ')
for i in range(2,A,1) :
    if i <= math.sqrt(A):
        if A%i == 0:
            decimal = False
            break
        else:
            decimal = True
print()
print("3. 결과값->")
print("   decimal = ", i, A, decimal)
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")