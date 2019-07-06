print('caseStudy: 반복문-문자열 읽어 오기-문자열을 "HelloKOREA" 이용한 사례')
print("m3_2_forloopTest_003_003.py")

import operator

print("1. 문자열 변수선언 ")
print("   str1 = 'HelloKOREA'")
str1 = "HelloKOREA"
print()
print("2. 문자열 변수를 리스트 변수로 선언 ")
print("   list1 = list(str1)")
list1 = list(str1)
print()
print("2.1 리스트 index 값 출력(위치확인)")
print("   print(list1)")
print("   결과->",list1)
print()
print("2.2 특정 문자열 값 출력: print(list1[0])")
print("   print(list1[0])")
print("   결과-> ",list1[0])
print()
print("2.3 특정 문자열 값 출력: print(list1[5])")
print("   print(list1[5])")
print("   결과-> ",list1[5])
print()
print("3. 리스트 변수의 딕셔너리 변수 선언 ")
print("   dic1 = dict(zip(range(len(list1)),list1))")
dic1 = dict(zip(range(len(list1)),list1))
print()
print("3.1 딕셔너리에서 index 값 출력(위치확인)")
print("   print(dic1)")
print("   결과->",dic1)
print()
print("4. 리스트에서 딕셔너리를 이용해 문자열 Key로 반복 숫자 계산")
print("4.1 문자열 반복횟수용 딕셔너리 변수선언")
print("   dic1_count = {}")
dic1_count = {}
print()
print("4.2 문자열 반복횟수 계산하는 반복문 정의")
print("   for i in list1: //리스트를 순차로 반복해서 실행")
print("       if i not in dic1_count: //카운트에 문자열 Key값이 없으면")
print("             dic1_count[i] = 1 //카운트 문자열 Key의 Value에 1을 지정하고")
print("       else: //카운트에 문자열 Key값이 존재하면")
print("             dic1_count[i] += 1 //카운트 문자열 Key의 Value에 1을 더한다.")
print()
for i in list1:
     if i not in dic1_count:
        dic1_count[i] = 1
     else:
        dic1_count[i] += 1
print("4.3 결과값->")
print("4.3.1 딕셔너리 카운트 기본 Key, Value 출력")
print("   print(dic1_count)")
print("   결과->", dic1_count)
print()
print("4.3.2 딕셔너리 카운트 Key, Value 출력 ")
print("   print(dic1_count.items())")
print("   결과->",dic1_count.items())
print()
print("4.3.3 변수 유형 확인하기 ")
print("   type(dic1_count)")
print("   결과->",type(dic1_count))
print()
print('5. 프로그램 종료')
print('   print("Program End")')
print("   Program End")
