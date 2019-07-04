print("Section003 알고리즘-1에서 10까지 부호 교차의 분수합계")
print("Ex.) -(1/2)+2/3)-3/4)+4/5)...(10/10)합계")
print("m3_2_forloopIfElseTest_003")
print()
print("1. i, sum 변수 선언과 초기화: ")
print("   i = 1     ")
print("   sum = 0   #j 대신에 이해를 위해 sum 변수 사용")
i = 1
sum = 0
print()
print("2. 반복문 내 조건문을 실행하는 반복 조건문: ")
print("   for i in range(1,11,1):       ")
print("       if ((i//2) == i/2) : ")
print("           sum = sum + (i/(i+1))")
print("        else:   ")
print("           sum = sum - (i/(i+1)) ")
print()
for i in range(1,11,1):
    # print(i)                        # 검증용
    if ((i//2) == i/2) :
        sum = sum + (i/(i+1))
        # print("if:",i//2,i/2)        # 검증용
    else:
        sum = sum - (i/(i+1))
        # print("else:",i//2,i/2)       # 검증용
print("3. 결과값->")
print("   sum = ", sum)
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")