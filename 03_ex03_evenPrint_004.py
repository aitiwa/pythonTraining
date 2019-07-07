print("caseStudy: 알고리즘-20부터 0까지 짝수를 출력")
print("03_ex03_evenPrint_004.py")
print("whileloopIfTest")
print()
print("1. coffee, money 변수 선언과 초기화")
print('   coffee = 10 ')
print('   money = 300 ')
coffee = 10
money = 300
print()
print("2. 문자열 함수와 반복 실행하는 반복문 ")
print('    while money:  ')
print('        print("   돈을 받고 커피를 줍니다.")  ')
print('        coffee = coffee -1  ')
print('        print("   남은 커피의 양은 %d개입니다." % coffee)  ')
print('        if coffee == 0:  ')
print('            print("   커피가 다 떨어졌습니다. 판매를 중지합니다.")  ')
print('            break  ')
print()
print("3. 결과값->")
while money:
    print("   돈을 받고 커피를 줍니다.")
    coffee = coffee -1
    print("   남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("   커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")