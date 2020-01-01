"""fibs = {0: 1, 1: 2}
def fib(n):
    if n in fibs: return fibs[n]
    if n % 2 == 0:
        fibs[n] = ((2 * fib((n / 2) - 1)) + fib(n / 2)) * fib(n / 2)
        return fibs[n]
    else:
        fibs[n] = (fib((n - 1) / 2) ** 2) + (fib((n+1) / 2) ** 2)
        return fibs[n]

"""
"""for T in range(int(raw_input())):
    N, M = list(map(int, raw_input().strip().split()))
    a, b = 1, 2
    for i in range(1, M):
        a, b = b, a + b

    print(pow(N, a, 1000000009))

"""
for T in range(int(raw_input())):
    N, M = list(map(int, raw_input().strip().split()))

    F1, F2 = 1, 2
    if M == 1:
        print(pow(N, F1, 1000000009))
    elif M == 2:
        print(pow(N, F2, 1000000009))
    else:
        for i in range(2, M):
            F1, F2 = F2, (F1 + F2)

        print(pow(N, F2, 1000000009))
   
"""
def matrix_mul(A, B):
     return ([A[0][0] * B[0][0] + A[0][1] * B[1][0],
              A[0][0] * B[0][1] + A[0][1] * B[1][1]],
             [A[1][0] * B[0][0] + A[1][1] * B[1][0],
              A[1][0] * B[0][1] + A[1][1] * B[1][1]])
 
def matrix_exp(A, e):
     if not e:
             return [[1,0],[0,1]]
     elif e % 2:
             return matrix_mul(A, matrix_exp(A, e-1))
     else:
             sq= matrix_exp(A, e//2)
             return matrix_mul(sq, sq)
 
def fibo(n):
     M = [[1,1],[1,0]]
     return matrix_exp(M, n)[0][0]

print((1515615619919 % (1000000009)) ** fibo(67))"""