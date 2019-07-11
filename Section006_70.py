print("Section006 알고리즘-수열6의 합계")
print("Ex.) -1+2-3+4.........-99의 합계")
print("Section006_70.py")
print("m3_2_forloopIfTest")
print()
print("1. N, SUM 변수 선언과 초기화: ")
print('   N = 0     ')
print("   SUM = 0   ")
N = 0
SUM = 0
print()
print("2. 반복 실행하는 반복문: ")
print('   for N in range(1,50,1):        ')
print('       if SW == 0 :               ')
print('           S = S + ( K / (K + 1)) ')
print('           SW = 1                 ')
print('       else:                      ')
print('           S = S - ( K / (K + 1)) ')
print('           SW = 0                 ')
print()
for N in range(1,100,2):
    SUM = SUM - N
    # print(N, SUM)  # 검증용
    if N < 99 :
        N = N + 1
        SUM = SUM + N
        # print(N, SUM)  # 검증용
print("3. 결과값->")
print("   SUM = ", SUM)
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")