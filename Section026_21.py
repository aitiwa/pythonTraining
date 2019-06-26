print("Section026_21 기본5행5열 알고리즘2: 행 변화 열 고정\n")
print("m3_2_nestedloopTest")
print("1. 2차원 배열 선언: ")
print("   a = [[0 for i in range(6)] for j in range(6)]")
a = [[0 for i in range(6)] for j in range(6)]
print()
print("2. 행 i, 열 j, 값 k의 변수 선언과 초기화: ")
print("   i, j, k = 0, 0, 0")
i, j, k = 0, 0, 0
print()
print("3. 행과 열을 반복 실행하는 반복문: ")
print("   for j in range(1, 6, 1) :")
print("       for i in range(1, 6, 1) :")
print("           k = k + 1")
print("           a[j][i] = k")
print('  #     print(" [%d][%d] = %2d " % (j, i, a[i][j]), end="\t")')
print('  # print(" ") // 결과 출력에 미표시가 나타남으로 실행과 출력 구분 표시')
print('   print(" 결과값->")')
print("   for j in range(1, 6, 1) :")
print("       for i in range(1, 6, 1) :")
print('           print(" [%d][%d] = %2d " % (j,i,a[i][j]), end = "\\t")')
print('        print(" ")')
print()
for j in range(1, 6, 1) :
    for i in range(1, 6, 1) :
        k = k + 1
        a[j][i] = k
    #     print(" [%d][%d] = %2d " % (j, i, a[i][j]), end="\t")
    # print(" ") # 결과 출력에 일부 0표시가 나타남으로 실행과 출력 구분 표시
print(" 결과값->")
for j in range(1, 6, 1) :
    for i in range(1, 6, 1) :
        print(" [%d][%d] = %2d " % (j, i, a[i][j]), end="\t")
    print(" ")
