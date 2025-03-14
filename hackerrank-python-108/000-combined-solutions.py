# 1. Say "Hello, World!"
print("Hello, World!")

#--------------------------------------------------------------------------------------------------------
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

#--------------------------------------------------------------------------------------------------------
# 3. Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)

#--------------------------------------------------------------------------------------------------------
# 4. Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)

#--------------------------------------------------------------------------------------------------------
# 5. Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i * i)

#--------------------------------------------------------------------------------------------------------
# 6. Write a Function
def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            leap = True
    return leap

#--------------------------------------------------------------------------------------------------------
year = int(input())
print(is_leap(year))

#--------------------------------------------------------------------------------------------------------
# 7. Print Function
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i + 1, end='')

#--------------------------------------------------------------------------------------------------------
# 8. List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    final = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(final)

#--------------------------------------------------------------------------------------------------------
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

#--------------------------------------------------------------------------------------------------------
# 10. Nested Lists
if __name__ == '__main__':
    records= []
    scores=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        i = [name,score]
        records.append(i)
        scores.append(i[1])
    
    # min_score = float('inf')
    # for j in scores:
    #     if j < min_score:
    #         min_score = j
    min_score = min(scores)
    
    second_min = min([k for k in scores if k > min_score])
    # second_min = float('inf')
    # for k in scores:
    #     if k > min_score and k<second_min:
    #         second_min = k
    
    second_lowest_students = sorted([n for n,s in records if s == second_min]) 
    
    for student in second_lowest_students:
        print(student)

#--------------------------------------------------------------------------------------------------------
# 11. Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    total = 0
    for name,marks in student_marks.items():
        if name==query_name:
            for i in marks:
                total += i
    

    print(f"{total/3:.2f}") 

#--------------------------------------------------------------------------------------------------------
# 12. Lists

if __name__ == '__main__':
    N = int(input())
    list1 = []
    for _ in range(N):
        cmd = input().split()   
        if cmd[0] =='insert':
            i=int(cmd[1])
            e=int(cmd[2])
            list1.insert(i,e)
        elif cmd[0] == 'print':
            print(list1)
        elif cmd[0] == 'remove':
            e = int(cmd[1])
            list1.remove(e)
        elif cmd[0] == 'append':
            e = int(cmd[1])
            list1.append(e)
        elif cmd[0] == 'sort':
            list1.sort()
        elif cmd[0] == 'pop':
            list1.pop()
        elif cmd[0] == 'reverse':
            list1.reverse()

#--------------------------------------------------------------------------------------------------------
# 13. Tuples

#python 2 
if __name__ == '__main__':
    n = int(raw_input()) # type: ignore
    integer_list = map(int, raw_input().split()) # type: ignore
    print(hash(tuple(integer_list)))

#--------------------------------------------------------------------------------------------------------
# 14. sWAP cASE

def swap_case(s):
    string_list = list(s)
    
    new_list = []
    for i in string_list:
        if i ==  i.lower():
            new_list.append(i.upper())            
        elif i == i.upper():
            new_list.append(i.lower())  
        else:
            new_list.append(i)  

    result = "".join(new_list)           
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#--------------------------------------------------------------------------------------------------------
# 15. String split and join

def split_and_join(line):
    input_list = line.split() 
    join = "-".join(input_list)
    return join
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#--------------------------------------------------------------------------------------------------------
# 16.
