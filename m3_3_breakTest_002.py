print("caseStudy: 반복문과 Break")
print("m3_3_breakTest_002.py")
print()
print("1. val 변수 선언과 초기화")
print()
print("2. for 반복문")
print('   for val in range(1,100,1):  ')
print('       print("순서값: ", val)  ')
print('       if val % 3 == 0:  ')
print('           print("결과값: ", val)  ')
print('           break  ')
print()
print("3. 결과값->")
for val in range(1,100,1):
    print("   순서값: ", val)
    if val % 3 == 0: 
        print("   결과값: ", val)
        break
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")