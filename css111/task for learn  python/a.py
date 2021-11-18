def goodness_string():
    N, K = map(int, input().split())
    S = input().strip()

    return abs(sum(int(S[i] != S[N-1-i]) for i in range(N//2))-K)


for case in range(int(input())):
    print('Case #{}: {}'.format(case + 1, goodness_string()))
