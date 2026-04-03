data = [
    ["apple banana cherry", "dog cat"],
    ["red blue", "sunny rainy"]
]

# Split -> Reverse -> Join back into a string
result = [
    [" ".join(s.split()[::-1]) for s in row] 
    for row in data
]

print(result)