import sys
numbers = [int(num) for num in sys.stdin]
lst = []
for number in numbers :
    a = number % 42 
    lst.append(a)
print(len(set(lst)))
