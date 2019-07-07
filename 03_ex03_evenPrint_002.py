print("caseStudy: 알고리즘2-20부터 0까지 짝수를 출력")
print("03_ex03_evenPrint_002.py")
print("forloopIfTest1")
print()
print("1. n, i, j 변수 선언과 초기화")
print('   n = 20 ')
print('   m = 20 ')
n = 20
m = 20
print()
print("2. 조건을 실행하는 반복문: ")
print('    for i in range(n,-1,-1):  ')
print('        if n%2 == 0:  ')
print('            print(n, end=" ")  ')
print('        n = n - 1  ')
print('    print()  ')
print('    for j in range(m, 0, -1):  ')
print('        if m % 2 == 0:  ')
print('            print(m, end=" ")  ')
print(' ')
print('        m = m - 1  ')
print(' ')
print('        if m == 0:  ')
print('            print(m, end=" ")  ')
print()
print("3. 결과값->")
for i in range(n,-1,-1):
    if n%2 == 0:
        print(n, end=" ")
    n = n - 1
print()
for j in range(m, 0, -1):
    if m % 2 == 0:
        print(m, end=" ")

    m = m - 1

    if m == 0:
        print(m, end=" ")
print()
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")