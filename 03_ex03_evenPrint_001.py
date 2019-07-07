print("caseStudy: 알고리즘-20부터 0까지 짝수를 출력")
print("03_ex03_evenPrint_001.py")
print("whileloopIfTest")
print()
print("1. n 변수 선언과 초기화")
print('   n = 20 ')
"""
[실습]
for 문과 while 문을 이용하여 20부터 0까지 짝수를 출력하는 프로그램을
작성하시오.
<요구사항>
- 시작값은 20으로 시작하여 반복할 때 마다 출력값이 줄어 들 수 있도록 작성하시오.
- 한 라인에 모든 출력결과가 출력되도록 print()에 end='' 추가하는 방법 이용하시오.
<출력결과>
while 문 출력 결과
20 18 16 14 12 10 8 6 4 2 0
for 문 출력 결과
20 18 16 14 12 10 8 6 4 2 0
"""
n = 20
print()
print("2. 조건을 실행하는 반복문: ")
print('    while n > 0 :  ')
print('        if n%2 == 0:  ')
print('            print(n, end=" ")  ')
print(' ')
print('        n = n - 1  ')
print(' ')
print('        if n == 0:  ')
print('            print(n, end=" ")  ')
print('            break  ')
print()
print("3. 결과값->")
while n > 0 :
    if n%2 == 0:
        print(n, end=" ")

    n = n - 1

    if n == 0:
        print(n, end=" ")
        break
print()
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")


