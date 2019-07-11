print("Section006 알고리즘-수열6의 합계")
print("Ex.) 2!+3!+4!+5!+..+20!의 합계")
print("Section006_40.py")
print("m3_2_forloopTest")
print()
print("1. i, j, sum 변수 선언과 초기화: ")
print('   i = 1     ')
print("   j = 1     ")
print("   sum = 0   # k 대신에 이해를 위해 sum 변수 사용")
i = 0
j = 1
sum = 0
print()
print("2. 반복 실행하는 반복문: ")
print('   for i in range(2,21,1):  ')
print('       j = j * i            ')
print('       sum = sum + j        ')
print()
for i in range(2,21,1):
    j = j * i
    sum = sum + j
    # print(i, j, sum)              #검증용
print("3. 결과값->")
print("   sum = ", sum)
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")