var = int(input("Enter a number: "))

for i in range(1, 10):
    var = var * i

if var > 100:
    print(f'{var} is greater than 100')
else:
    print(f'{var} is less than 100')

print(var)
