print("caseStudy: 난수이용 숫자 맞추기 게임")
print("m3_3_breakContinueTest_001.py")
print()
print("1. correct_answer, count 변수 선언과 초기화")
print('   correct_answer = random.randint(0, 100) ')
print('   count = 0 ')
import random    # 난수를 만드는 random 모듈 사용
correct_answer = random.randint(0, 100)    # 0~100 난수 발생
count = 0
print()
print("2. While 반복문")
print('    while True:  ')
print('        number = int(input("숫자를 입력하세요: "))  ')
print('        if number < 0 or number > 100:  ')
print('            continue  ')
print(' ')
print('        count += 1  ')
print(' ')
print('        if correct_answer == number:  # 정답이면 break  ')
print('            break  ')
print('        elif correct_answer > number:  ')
print('            print(number, "보다 큽니다!")  ')
print('        else:  ')
print('            print(number, "보다 작습니다!")  ')
# while 무한 루프
while True :
    number = int(input("숫자를 입력하세요: "))
    if number < 0 or number > 100:
        continue
    
    count += 1

    if correct_answer == number :    # 정답이면 break
        break
    elif correct_answer > number :
        print(number, "보다 큽니다!")
    else :
        print(number, "보다 작습니다!")

# 평가 출력
print()
print("3. 결과값->")
print("   정답입니다!")
if count <= 2 :
    print(count, "번만에 맞춘 당신은 천재!")
elif count <= 4 :
    print(count, "번만에 맞추셨네요. 잘했어요.")
else :
    print(count, "번만에 맞추다니 아쉽습니다.")
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")