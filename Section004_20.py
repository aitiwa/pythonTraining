print("Section004 알고리즘-수열4의 합계")
print("Ex.) 1+3+6+10+15+21+28+...의 합계")
print("m3_2_forloopTest_004_20")
print()
print("1. i, j, sum 변수 선언과 초기화: ")
print('   i = 0     ')
print("   j = 0     ")
print("   sum = 0   # k 대신에 이해를 위해 sum 변수 사용")
i = 0
j = 0
sum = 0
print()
print("2. 반복 실행하는 반복문: ")
print('    for i in range(1,21,1):  ')
print('        j = j + i            ')
print('        sum = sum + j        ')
print()
for i in range(1,21,1):
    j = j + i
    sum = sum + j
    # print(i, j, sum)              #검증용
print("3. 결과값->")
print("   sum = ", sum)
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")