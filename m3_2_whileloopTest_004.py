print("caseStudy: 메뉴 선택")
print("m3_2_whileLoopTest_004.py")
print()
print("1. choice 변수 선언과 초기화")
print('   choice = None ')
choice = None
print()
print("2. While 반복문")
print('    while True:  ')
print('        print("1. 원 그리기")  ')
print('        print("2. 사각형 그리기")  ')
print('        print("3. 선 그리기")  ')
print(' ')
print('        choice = input("메뉴를 선택하시오: ")  ')
print(' ')
print('        if choice == "1":  ')
print('            print("원 그리기를 선택했습니다.")  ')
print('        elif choice == "2":  ')
print('            print("사각형 그리기를 선택했습니다.")  ')
print('        elif choice == "3":  ')
print('            print("선 그리기를 선택했습니다.")  ')
print('        else:  ')
print('            print("잘못된 선택을 했습니다.")  ')
print('            break  ')
print('        print()  ')
print()
print("3. 결과값->")
while True:
    print("1. 원 그리기")
    print("2. 사각형 그리기")
    print("3. 선 그리기")
    
    choice = input("메뉴를 선택하시오: ")

    if choice == "1":
        print("원 그리기를 선택했습니다.")
    elif choice == "2":
        print("사각형 그리기를 선택했습니다.")
    elif choice == "3":
        print("선 그리기를 선택했습니다.")        
    else:
        print("잘못된 선택을 했습니다.")
        break
    print()
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")