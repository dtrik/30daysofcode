n = int(input())
for i in range(n):
    S = input()
    print("".join(i for i in S[::2]), "".join(j for j in S[1::2]))