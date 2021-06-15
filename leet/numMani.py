def subtractProductAndSum(n: int):
        r = []
        while n:
            r.append(n % 10)
            n = n // 10
        print(r)
        r = r[::-1]
        print(r)
        

a = 1234
subtractProductAndSum(a)
