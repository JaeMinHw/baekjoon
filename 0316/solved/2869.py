A, B, V = map(int, input().split())

day =  (V-1-B) / (A-B)


# x > (V-1-B) / A-B

print(int(day + 1))