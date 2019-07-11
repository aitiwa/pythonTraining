print("Section005 알고리즘-수열6의 합계")
print("Ex.) 1+1/1+1/2+1/3+1/4+....+1/10의 합계")
print("Section006_50.py")
print("m3_2_forloopTest")
print()
print("1. A, B, HAP 변수 선언과 초기화: ")
print('   A = 1     ')
print("   B = 1     ")
print("   HAP = 1   ")
A = 1
B = 1
HAP = 1
print()
print("2. 반복 실행하는 반복문: ")
print('   for i in range(1,11,1):  ')
print('       A = A * B            ')
print('       D = 1 / B            ')
print('       HAP = HAP + D        ')
print('       B = B + 1            ')
print()
for i in range(1,11,1):
    A = A * B
    D = 1 / B
    HAP = HAP + D
    # print(i, A, B, HAP)              #검증용
    B = B + 1
print("3. 결과값->")
print("   HAP = ", HAP)
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")