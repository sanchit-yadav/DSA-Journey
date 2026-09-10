n = int(input("Enter a number: "))
def func(N):
    if N == 0:
        return
    func(N - 1)
    print(N)

func(n)