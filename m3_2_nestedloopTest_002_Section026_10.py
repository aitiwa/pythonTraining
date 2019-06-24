print("Section026_10 기본5행5열 알고리즘: 행 고정 열 변화형\n")

print("1. 2차원 배열 선언: ")
print("   a = [[0 for i in range(6)] for j in range(6)] #0~5중 1~5를 사용\n")
print("   만약 a = [[0 for i in range(5)] for j in range(5)]로 선언하면 0부터 사용해 ")
print("   에러 발생->IndexError: list assignment index out of range")
a = [[0 for i in range(6)] for j in range(6)]
print()
print("2. 행 i, 열 j, 값 k의 변수 선언과 초기화: ")
print("   i, j, k = 0, 0, 0")
i, j, k = 0, 0, 0
print()
print("3. 행과 열을 반복 실행하는 반복문: ")
print("   for i in range(1, 6, 1) :")
print("       for j in range(1, 6, 1) :")
print("           k = k + 1")
print("           a[i][j] = k")
print()
print('   print(" 결과값->")')
print("   for i in range(1, 6, 1) :")
print("       for j in range(1, 6, 1) :")
print('           print(" [%d][%d] = %2d " % (i,j,a[i][j]), end = "\\t")')
print('       print(" ")')
print()
for i in range(1, 6, 1) :
    for j in range(1, 6, 1) :
         k = k + 1
         a[i][j] = k
print("4. 결과값->")
for i in range(1, 6, 1) :
    for j in range(1, 6, 1) :
         print(" [%d][%d] = %2d " % (i,j,a[i][j]), end = "\t")
    print(" ")