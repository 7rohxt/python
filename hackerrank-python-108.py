# 1. Say "Hello, World!"
print("Hello, World!")

# 2. Python If-Else
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")

# 3. Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)

# 4. Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)

# 5. Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i * i)

# 6. Write a Function
def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            leap = True
    return leap

year = int(input())
print(is_leap(year))

# 7. Print Function
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i + 1, end='')

# 8. List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    final = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(final)

# 9. Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lis = list(arr)
    max_score = -float('inf')
    for i in lis:
        if i > max_score:
            max_score = i
    second_max = -float('inf')
    for i in lis:
        if i < max_score and i > second_max:
            second_max = i
    print(second_max)