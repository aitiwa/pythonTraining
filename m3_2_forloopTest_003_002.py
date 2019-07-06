print("caseStudy: 반복문-문자열 읽어 오기")
print('study m3_1_forloopTest_003_002: 문자열 읽어 오기\n')
print("1. str1,result 변수 선언과 초기화:  ")
print('   str1 = "HelloKOREA" ')
print('   result = "" ')
str1 = "HelloKOREA"
result = ""
print("2. 문자열 함수와 반복 실행하는 반복문 ")
print('    size = len(str1)  ')
print('    print("   문자열 길이: ",size)  ')
print('    print(str1)  ')
print(' ')
print('    for i in str1:  ')
print('        result  +=  i  ')
print('    print(result)  ')
print(' ')
print('    list1=list(str1)  ')
print('    for i in list1:  ')
print('        print(i, end = "")  ')
print()
print("3. 결과값->")
size = len(str1)
print("   문자열 길이: ",size)
print(str1)

for i in str1:
    result  +=  i
print(result)

list1=list(str1)
for i in list1:
    print(i, end = "")
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")