def lower_triangular(n):
    for i in range(1, n + 1):
        print('* ' * i)

def upper_triangular(n):
    for i in range(n, 0, -1):
        print('* ' * i)

def pyramid(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '* ' * (i + 1))

n = int(input("Enter size of pattern: "))

print("This one is lower triangular pattern")
lower_triangular(n)
print("This one is upper triangular pattern:")
upper_triangular(n)
print(" This one isPyramid Pattern:")
pyramid(n)
