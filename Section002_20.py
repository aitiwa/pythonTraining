print("SECTION002_20 알고리즘-수열2: 1에서 100까지 부호 교차의 분수합계")
print("forloopTest_003\n")
print("1. i, sum 변수 선언과 초기화: ")
print("   i, sum = 0, 0  #j 대신에 이해를 위해 sum 변수 사용")
i, sum = 0, 0
print()
print("2. 반복문 내 조건문을 실행하는 반복 조건문: ")
print("   for i in range(1, 101, 2) : # 2개를 하나의 단위로")
print("       sum = sum + i")
print("       i = i + 1    ")
print("       sum = sum - i")
print('   print(" 결과값->")')
print('   print(" sum = ", sum)')
print()
for i in range(1, 101, 2) :    # 2개를 하나의 단위로 첫번째 항
    # print(i)                 # 검증용
    sum = sum + i
    # print("   sum = ", sum)  # 검증용
    i = i + 1                  # 두번째 항을 만들어준다.
    # print(i)                 # 검증용
    sum = sum - i
    # print("   sum = ", sum)  # 검증용
print("3. 결과값->")
print("   sum = ", sum)
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")