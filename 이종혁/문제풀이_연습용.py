s = input()
for i in range(97, 123):
    x = chr(i) 
    result = s.find(x)
    print(result, end=' ')