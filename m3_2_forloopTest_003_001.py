print("caseStudy: 반복문-문자열 읽어 오기")
print('m3_1_forloopTest_003_001.py\n')
print("1. str1  변수 선언과 초기화:  ")
print('   str1 = "HelloKOREA" ')
str1 = "HelloKOREA"
print()
print("2. 문자열 함수")
print('   size = len(str1)   ')
size = len(str1)
print()
print("2.1 결과값->")
print('   print("   문자열 길이:", size)  ')
print('   print()  ')
print("   문자열 길이:", size)
print()
print("3. 문자열 리스트로 선언")
print('   list1=list(str1)  ')
print("   print('\\n'.join(list1))  ")
print('   print()  ')
print()
print("3.1 결과값->")
list1=list(str1)
print('\n'.join(list1))
print()
print("4. 문자열 리스트를 반복문으로 출력")
print('   for i in range(size):  ')
print('       print("문자열 {}: {}".format(i,str1[i]))  ')
print()
print("4.1 결과값->")
for i in range(size):
    print("문자열 {}: {}".format(i,str1[i]))
print()
print('5. 프로그램 종료')
print('   print("Program End")')
print("   Program End")