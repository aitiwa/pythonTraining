print("Section004 알고리즘-수열4의 합계")
print("Ex.) 1+3+6+10+15+21+28+...의 합계")
print("Section004_30.py")
print("m3_2_forloopIfElseTest")
print()
print("1. i, j, k, l, sum 변수 선언과 초기화: ")
print('   i = 0     ')
print("   j = 0     ")
print("   l = -1    ")
print("   k = 0    ")
print("   sum = 0   # m 대신에 이해를 위해 sum 변수 사용")
i = 0
j = 1
l = -1
k = 0
sum = 0
print()
print("2. 반복 실행하는 반복문: ")
print('   for i in range(0,20,1):  ')
print('       j = j + i            ')
print('       if i%2 == 0 :        ')
print('           k = j * l        ')
print('       else:                ')
print('           k = j            ')
print('       sum = sum + k        ')
print()
for i in range(0,20,1):
    j = j + i
    if i%2 == 0 :
        k = j * l
    else:
        k = j
    sum = sum + k
    # print(i+1, j, k, sum)              #검증용
print("3. 결과값->")
print("   sum = ", sum)
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")