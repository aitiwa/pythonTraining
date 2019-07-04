print("SECTION002_30 알고리즘-수열2: 1에서 100까지 부호 교차의 분수합계")
print("forloopIfelseTest_003\n")
print("1. i, sum 변수 선언과 초기화: ")
print("   i, sum = 0, 0  #j 대신에 이해를 위해 sum 변수 사용")
i, sum = 0, 0
print()
print("2. 반복문 내 조건문을 실행하는 반복 조건문: ")
print("   for i in range(1, 101, 1) :")
print("       if i%2 != 0 :  #홀수")
print("          sum = sum + i")
print("        else:         #짝수")
print("          sum = sum - i")
print('   print(" 결과값->")')
print('   print(" sum = ", sum)')
print()
for i in range(1, 101, 1) :
    if i%2 != 0 :                     #홀수
        sum = sum + i
        # print("   sum = ", sum)               # 검증용
    else:                             #짝수
        sum = sum - i
        # print("   sum = ", sum)              # 검증용
print("3. 결과값->")
print("   sum = ", sum)
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")