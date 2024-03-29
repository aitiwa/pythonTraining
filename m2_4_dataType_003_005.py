print("caseStudy: 리스트 길이, 읽기")
print("m2_4_dataType_003_005.py\n")

import random as rnd

print("1. 리스트 변수 정의 : " )
print("   list1 = []; " )
list1 = [];
print()
print("2. 리스트 변수 생성하는 반복문 : " )
print("   for i in range(1,10):                  " )
print("       list1.append(rnd.randrange(1,100)) " )
for i in range(1,10):
    list1.append(rnd.randrange(1,100))
print()
print("3. 리스트 변수 생성 결과 값: ")
print('   print("  ",list1) ')
print("  ",list1)
print()
print("3.1 리스트의 길이 계산: ")
print('    len(list1) ')
print('    print("   ",len(list1)) ')
len(list1)
print("   ",len(list1))
print()
print('3.2 0번째부터 1번째까지 값 가져오기 : ')
print('    list1[0:2] ')
print('    print("   ",list1[0:2]) ')
list1[0:2]
print("   ",list1[0:2])
print()
print('3.3 2번째부터 4번째까지 값 가져오기 : ')
print('    list1[2:5] ')
print('    print("   ",list1[2:5]) ')
list1[2:5]
print("   ",list1[2:5])
print()
print("3.4 리스트 값 수정하기")
print('    list1[0] = 99     ')
print('    print("   ", list1[0])     ')
list1[0] = 99
print("   ", list1[0])
print()
print("3.5 리스트 값이 50이상이면 제거하기: ")
print("    ----------------------------")
print("    for index in range(len(list1)-1, -1, -1): ")
print("        if list1[index] > 50:                 ")
print("            list1.remove(list1[index])        ")
print('    print("    list1 = ",list1)               ')
for index in range(len(list1)-1, -1, -1):
    if list1[index] > 50:
        list1.remove(list1[index])
print("    list1 = ",list1)
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")
