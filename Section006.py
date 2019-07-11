print("Section006 알고리즘-수열6 피보나치")
print("Ex.) 1+1+2+3+5+8+13+...의 합계")
print("Section006.py")
print("m3_2_forloopTest")
print()
print("1. i, a, b, c, sum 변수 선언과 초기화: ")
print('   a = 0     ')
print("   b = 0     ")
print("   sum = 2   # k 대신에 이해를 위해 sum 변수 사용")
a = 1
b = 1
sum = 2
print()
print("2. 반복 실행하는 반복문: ")
print('   for i in range(1,21,1):  ')
print('       c = a + b            ')
print('       sum = sum + c        ')
print('       a = b                ')
print('       b = c                ')
print()
for i in range(1,21,1):
    c = a + b
    sum = sum + c
    a = b
    b = c
    # print(i, a, b , sum)              #검증용
print("3. 결과값->")
print("   sum = ", sum)
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")