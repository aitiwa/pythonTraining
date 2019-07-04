print("Section001 알고리즘-1에서 1000까지중 입력받은 수까지 합계")
print("m3_3_whileLoopIfBreakTest_001.py")
print()
print("1. count, sum, limit 변수 선언과 초기화: ")
print("   count = 0   ")
print("   sum = 0     ")
count = 0
sum = 0
print("2. 사용자로부터 limit 변수의 input값을 받는다.")
print('   limit = int(input("어디까지 더할까요? :"))')
limit = int(input("   어디까지 더할까요? : "))
print()
print("3. 반복문 내 조건문을 실행하는 반복 조건문: ")
print("   while count <= 1000:  ")
print("       sum = sum + count  ")
print("       if count == limit :  ")
print("           break   ")
print("       count = count + 1   ")
print()
while count <= 1000:
    sum = sum + count
    if count == limit :
        break
    count = count + 1

print("4. 결과값->")
print("   1부터 %d까지의 합은: %d"% (count,sum))
print()
print('5. 프로그램 종료')
print('   print("Program End")')
print("   Program End")