print("Section006 알고리즘-수열6의 합계")
print("Ex.) 1/2+2/3+3/4+4/5+5/6-....+49/50의 합계")
print("Section006_60.py")
print("m3_2_forloopIfElseTest")
print()
print("1. K, S, SW 변수 선언과 초기화: ")
print('   K = 0     ')
print("   S = 0     ")
print("   SW = 0   ")
K = 0
S = 0
SW = 0
print()
print("2. 반복 실행하는 반복문: ")
print('   for K in range(1,50,1):        ')
print('       if SW == 0 :               ')
print('           S = S + ( K / (K + 1)) ')
print('           SW = 1                 ')
print('       else:                      ')
print('           S = S - ( K / (K + 1)) ')
print('           SW = 0                 ')
print()
for K in range(1,50,1):
    if SW == 0 :
        S = S + ( K / (K + 1))
        # print(K, K+1, S, SW)  # 검증용
        SW = 1
    else:
        S = S - ( K / (K + 1))
        SW = 0
        # print(K, K+1, S, SW)  # 검증용
print("3. 결과값->")
print("   S = ", S)
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")