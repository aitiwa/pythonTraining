print("caseStudy: 반복문과 Break")
print("m3_3_breakTest_003.py")
print()
print("1. a, i 변수 선언과 초기화")
print('   a = 0 ')
a = 0
print()
print("2. 중첩 for 반복문과 조건문")
print('    for i in range(10):   ')
print('        print("i = ", i)   ')
print('        for j in range(10):  ')
print('            a = j  ')
print('            print(a)  ')
print(' ')
print('            if(a == 5):  ')
print('                break  ')
print('    print("a = ", a)   ')
print()
print("3. 결과값->")
for i in range(10):
    print("i = ", i)
    for j in range(10):
        a = j
        print(a)

        if(a == 5):
            break

    # if (a == 5):
    #     break
print("a = ", a)    
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")