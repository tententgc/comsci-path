MaxValue = 10
MinValue = 5
for i in range(1, MaxValue+1):
    k = MaxValue + 1 if i <= MinValue else MinValue + 1
    print(f"Multiplication table of {i}")
    print(*[i*j for j in range(1, k)])
