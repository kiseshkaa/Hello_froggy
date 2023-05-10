slovar = {'one': 1,
          'two': 2}
a = input()
a = a.split()
numbers = []

for i in a:
    numbers.append(slovar[i])

print(a)
print(numbers)
