print("Section006 알고리즘-수열6의 합계")
print("Ex.) 1+1+2+3+5+8+13+21+34의 합계")
print("Section006_30.py")
print("m3_2_forloopTest")
print()
print("1. A, B, H, T 변수 선언과 초기화: ")
print('   A = 1     ')
print("   B = 1     ")
print("   H = 0     ")
print("   T = 0     ")
A = 1
B = 1
H = 0
T = 0
print()
print("2. 반복 실행하는 반복문: ")
print('   for i in range(1,10,1):  ')
print('       H = A + B            ')
print('       T = T + H            ')
print('       A = B                ')
print('       B = H                ')
print()
for i in range(1,10,1):
    H = A + B
    T = T + H
    # print(i, A, B, H, T)              #검증용
    A = B
    B = H
print("3. 결과값->")
print("   T = ", T)
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")