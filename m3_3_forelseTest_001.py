print("caseStudy: 반복문과 Continue")
print("m3_3_continueTest_002.py")
print()
print("1. sum, i 변수 선언과 초기화")
print('   break_letter = input("   python중 중단할 문자를 입력하시오: ") ')
break_letter = input("   python중 중단할 문자를 입력하시오: ")
print()
print("2. 중첩 for 반복문과 조건문")
print('   for letter in "python":  ')
print('       if letter == break_letter:  ')
print('           break  ')
print('       print(letter)  ')
print('   else:  ')
print('       print("모든 문자 출력 완료!")  ')
print()
print("3. 결과값->")
for letter in "python":
    if letter == break_letter:
        break
    print(letter)
else:
    print("모든 문자 출력 완료!")
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")
    
