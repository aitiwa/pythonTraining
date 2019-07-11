print("Section006 알고리즘-수열6의 합계")
print("Ex.) (77*1)+(76*2)+(75*3)+..+(2*76)+(1*77)의 합계")
print("Section006_20.py")
print("m3_2_forloopIfElseTest")
print()
print("1. P, H, M, Q 변수 선언과 초기화: ")
print('   P = 0     ')
print("   j = 0     ")
print("   l = -1    ")
print("   sum = 0   # k 대신에 이해를 위해 sum 변수 사용")
P = 0
H = 0
M = 0
print()
print("2. 반복 실행하는 반복문: ")
print('   for P in range(1,78,1):  ')
print('       Q = 78 - P           ')
print('       M = (Q * P)          ')
print('       H = H + M            ')
print()
for P in range(1,78,1):
    Q = 78 - P
    M = (Q * P)
    H = H + M
    # print(P, Q, M, H)              #검증용
print("3. 결과값->")
print("   H = ", H)
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")