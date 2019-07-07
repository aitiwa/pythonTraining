print("caseStudy: 반복문과 Continue")
print("m3_3_continueTest_002.py")
print()
print("1. sum, i 변수 선언과 초기화")
print('   sum = 0 ')
sum = 0
print()
print("2. 중첩 for 반복문과 조건문")
print('    for i in range(10):       ')
print('        print("i1 = ", i)     ')
print('        if i % 3 == 0:        ')
print('            print("i2 = ",i)  ')
print('            continue          ')
print('        print("i3 = ", i)     ')
print('        sum += i              ')
print()
print("3. 결과값->")
for i in range(10):
    print("i1 = ", i)
    if i % 3 == 0:
        print("i2 = ",i)
        continue
    print("i3 = ", i)
    sum += i
print("조건에 맞는 전체 합 :",sum)    
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")
    
