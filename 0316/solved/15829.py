l = int(input())
s = input()

r = 31
m = 1234567891
res = 0

for i in range(l):
    res += (ord(s[i]) - 96) * (r ** i)
print(res % m)