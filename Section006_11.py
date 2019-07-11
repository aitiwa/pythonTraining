print("Section006 알고리즘-수열6의 합계")
print("Ex.) 1-2+3-4+5-6+7...-98+99-100의 합계")
print("Section006_11.py")
print("m3_2_forloopIfElseTest")
print()
print("1. n, y, s 변수 선언과 초기화: ")
print('   n = 0     ')
print("   y = 0     ")
print("   s = 1    ")
n = 0
y = 0
s = 1
print()
print("2. 반복 실행하는 반복문: ")
print('   for n in range(1,101,1):  ')
print('       y = y + n * l        ')
print('       s = s + (-1)        ')
print()
for n in range(1,101,1):
    y = y + (n * s)
    # print(n, n*s, y)              #검증용
    s = s * (-1)
print("3. 결과값->")
print("   y = ", y)
print()
print('4. 프로그램 종료')
print('   print("Program End")')
print("   Program End")