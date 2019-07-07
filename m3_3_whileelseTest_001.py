print("Section001 알고리즘-1에서 100까지 합계")
print("m3_3_whileLoopElseTest_001.py")
print()
print("1. count, sum, limit 변수 선언과 초기화: ")
print('   count = 0   ')
print('   sum = 0     ')
count = 1
sum = 0
print()
print("3. 반복문 내 조건문을 실행하는 반복 조건문: ")
print('    while count <= 100:  ')
print('        sum = sum + count  ')
print('        count = count + 1  ')
print('        if count == 101:   ')
print('            break  ')
print('    else:  ')
print('         print("덧셈 작업이 완료되었습니다.")  ')
print('    print("1부터 100까지의 합은:", sum)  ')
print()
print("4. 결과값->")
while count <= 100:
    # print(count)      #중간 검증용
    sum = sum + count
    count = count + 1
    if count == 101:
        break
else:
     print("덧셈 작업이 완료되었습니다.")
print("   1부터 100까지의 합은:", sum)
print()
print('5. 프로그램 종료')
print('   print("Program End")')
print("   Program End")