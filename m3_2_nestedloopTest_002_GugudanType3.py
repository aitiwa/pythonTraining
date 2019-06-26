print("Python Case Study\n")
print("m3_2_nestedloop_002_GugudanType3")
print("1. Variable Declaration: 변수 선언")
i, j = 0, 0
print("2. Nested Loop: 중첩 반복문")
print("   for i in range(2, 10, 1) : ")
print("       for j in range(1, 10, 1) : ")
print('           print(" %d x %d = %2d" % (i, j, i*j), end="\\t") ')
print("       print("") ")
print("Result->")
for i in range(2, 10, 1) :
    for j in range(1, 10, 1) :
        print(" %d x %d = %2d" % (i, j, i*j), end="\t")
    print("")
print("Program end")