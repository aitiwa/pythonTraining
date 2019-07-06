print("caseStudy: 연산자 계산 - 조건문")
print('m3_1_ifTest_002.py\n')
print("1. result, op, num1, num2  변수 선언과 초기화:  ")
print('   result = 0 ')
print('   print("1.덧셈 2.뺄셈 3.곱셈 4.나눗셈") ')
print('   op = int(input("연산자 선택 :")) ')
print('   num1 = int(input("값1 :")) ')
print('   num2 = int(input("값2 :")) ')
print()
result = 0
print("1.덧셈 2.뺄셈 3.곱셈 4.나눗셈")
op = int(input("연산자 선택 :"))
num1 = int(input("값1 :"))
num2 = int(input("값2 :"))
print()
print("2. 여러 단계 조건을 실행하는 조건문 ")
print('   if op == 1:  ')
print('       result = num1 + num2  ')
print('   if op == 2:  ')
print('       result = num1 - num2  ')
print('   if op == 3:  ')
print('       result = num1 * num2  ')
print('   if op == 4:  ')
print('       result = num1 / num2  ')
print('   print("   결과 {}".format(result))  ')
print()
print("3. 결과값->")
if op == 1:
    result = num1 + num2
if op == 2:
    result = num1 - num2
if op == 3:
    result = num1 * num2
if op == 4:
    result = num1 / num2
print("   결과 {}".format(result))
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")

