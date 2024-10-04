X = int(input())

if (X < 0):
    print(X, " está no intervalo 1")
elif (X > 0 and X < 1000):
    print(X, " está no intervalo 2")
elif (X > 1001 and X < 10000):
    print(X, " está no intervalo 3")
elif (X > 10001):
    print(X, " está no intervalo 4")