﻿print('CaseStudy: 획득한 점수가 60점 이상이면 "통과 하였습니다" 라는 메시지 출력한다.')
print("m3_1_ifElseTest_001.py\n")
print("1. baseScore, score 변수 선언과 초기화: ")
print("   baseScore = 60")
baseScore = 60
print("   score = 0")
score = 0
print()
print("2. 사용자로부터 점수를 키보드를 통해 input 변수 값을 받는다.")
print('   score = int(input("  획득점수를 입력하세요:"))')
score = int(input("   획득점수를 입력하세요: "))
print()
print("3. 조건에 따라 분기하는 조건문")
print('   if score >= baseScore: ')
print('       print("4. 결과값->")')
print('       print("   통과 하였습니다.")')
print('   else: ')
print('       print("4. 결과값->")')
print('       print("   통과하지 못했습니다.")')
print('       print()')
print()
if score >= baseScore:
    print("4. 결과값->")
    print("   통과 하였습니다.")
else:
    print("4. 결과값->")
    print("   통과하지 못했습니다.")
print()
print('5. 프로그램 종료)')
print('   print("Program End")')
print("   Program End")