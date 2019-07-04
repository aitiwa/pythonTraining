print("SECTION002 알고리즘-수열2: 1에서 100까지 부호 교차의 분수합계")
print("forloopIfelseTest_003\n")
print("1. i, sum, sw 변수 선언과 초기화: ")
print("   i, sum, sw = 0, 0, 0")
i, sum, sw = 0, 0, 0      #j 대신에 sum 변수 사용
print()
print("2. 반복문 내 조건문을 실행하는 반복 조건문: ")
print("   for i in range(1, 101, 1) :")
print("       if sw == 0 :")
print("          sum = sum + i")
print("          sw = 1")
print("        else:")
print("          sum = sum - i")
print("          sw = 0")
print('   print(" 결과값->")')
print('   print(" sum = ", sum)')
print()
for i in range(1, 101, 1) :
    if sw == 0 :
        sum = sum + i
        # print("   sum = ", sum)               # 검증용
        sw = 1           # 최초 0에서 1로 변경
    else:
        sum = sum - i
        # print("   sum = ", sum)              # 검증용
        sw = 0           # 1에서 0로 변경
print("3. 결과값->")
print("   sum = ", sum)