# Examples 👨🏼‍💻

Here are some examples to get you started.

**Covered topics:** 


## Example 1 - Hello, Python! Printing: 

**Problem:** Print the message "Hello, Python!" on the screen `n` times (where `n` is an integer entered by the user).

| No. | Inputs | Outputs                         |
| --- | ------ | ------------------------------- |
| 1   | 3      | Hello, Python!<br>Hello, Python!<br>Hello, Python! |
| 2   | 5      | Hello, Python!<br>Hello, Python!<br>Hello, Python!<br>Hello, Python!<br>Hello, Python! |
| 3   | 1      | Hello, Python! |
    
```python
n = int(input("Enter the number of times to print the message: "))
for _ in range(n):
    print("Hello, Python!")
```

## Example 2: Number Range Printing
**Problem:** Given two integers `a` and `b` (`a ≤ b`). Print all numbers from `a` to `b` inclusive.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 1<br>12 | 1 2 3 4 5 6 7 8 9 10 11 12 |
| 2   | 5<br>10 | 5 6 7 8 9 10 |
| 3   | 0<br>0  | 0 |

```python
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a <= b:
    for i in range(a, b + 1):
        print(i, end=" ")
else:
    for i in range(a, b - 1, -1):
        print(i, end=" ")
```

## Example 3: Average Grade Calculation

**Problem:** A user enters the number of subjects `n`, and then, accordingly, the student's grades in `n` subjects. Determine the average grade.

| No. | Inputs | Outputs                |
| --- | ------ | ---------------------- |
| 1   | 5<br>10<br>11<br>9<br>8<br>10 | 9.60 |
| 2   | 3<br>5<br>5<br>5              | 5.00 |
| 3   | 1<br>10                        | 10.00 |

```python

n = int(input("Enter the number of subjects: "))

total = 0

for _ in range(n):
    grade = int(input("Enter the grade: "))
    total += grade

average = total / n

print(f"The average grade is: {average:.2f}")
```


## Example 4: Number of # Characters Printing

**Problem:** Write a program to print integers from `n` to `0` with the number of `#` characters equal to the value of the number.

| No. | Inputs | Outputs                               |
| --- | ------ | ------------------------------------- |
| 1   | 6      | 6 ######<br>5 #####<br>4 ####<br>3 ###<br>2 ##<br>1 # |
| 2   | 3      | 3 ###<br>2 ##<br>1 # |
| 3   | 1      | 1 # |

```python

n = int(input("Enter the number: "))

for i in range(n, -1, -1):
    print(i, "#" * i)
```


## Example 5: Triangle of Numbers Printing

**Problem:** Given an integer `n` (1 ≤ `n` ≤ 9). Print a triangle of numbers from `1` to `n` as shown in the example.

| No. | Inputs | Outputs             |
| --- | ------ | ------------------- |
| 1   | 9      | 1<br>22<br>333<br>4444<br>55555<br>666666<br>7777777<br>88888888<br>999999999 |
| 2   | 5      | 1<br>22<br>333<br>4444<br>55555 |
| 3   | 1      | 1 |

```python
n = int(input("Enter the number: "))
for i in range(1, n + 1):
    print(str(i) * i)
```

## Example 6: Positive, Negative, and Zero Numbers Counting

**Problem:** Write a program that counts the positive and negative numbers, as well as zeros entered by the user, and outputs their quantity in one line with one space between them.

| No. | Inputs | Outputs                      |
| --- | ------ | ---------------------------- |
| 1   | 5<br>12<br>-45<br>0<br>14<br>0 | 2 1 2 |
| 2   | 1<br>2<br>3<br>4<br>5<br>6 | 6 0 0 |
| 3   | -1<br>-2<br>-3<br>-4<br>-5<br>-6 | 0 6 0 |

```python
positive = 0
negative = 0
zeros = 0

n = int(input("Enter the number of integers: "))

for _ in range(n):
    number = int(input("Enter the number: "))
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        zeros += 1

print(positive, negative, zeros)
```

## Example 7: Two-Digit Odd Numbers Printing

**Problem:** Print all two-digit odd numbers whose last digit is `n` - an integer entered by the user.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 5      | 15 25 35 45 55 65 75 85 95 |
| 2   | 1      | 11 21 31 41 51 61 71 81 91 |
| 3   | 0      | 10 20 30 40 50 60 70 80 90 |

```python
n = int(input("Enter the number: "))

for i in range(10, 100):
    if i % 2 != 0 and i % 10 == n:
        print(i, end=" ")
```


## Example 8: Number of Digits Counting

**Problem:** Given a natural number `n`. Determine the number of digits in it.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 12367832 | 8       |
| 2   | 142      | 3       |
| 3   | 0        | 1       |
    
```python

n = int(input("Enter the number: "))

count = 0

while n > 0:
    n //= 10 # Decrease the number by one digit
    count += 1 # Increase the count by one

print(count)
```

## Example 9: Printing Numbers with Conditions

**Problem:** Write a program that prints integers from `1` to `n` (1 < `n` ≤ 1000) with the following condition: for numbers divisible by 3, it prints `*3*` instead of the number, for numbers divisible by 5, it prints `*5*`, and for numbers divisible by 3 and 5 simultaneously, the message will be `*35*`.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 15     | 1<br>2<br>*3*<br>4<br>*5*<br>*3*<br>7<br>8<br>*3*<br>*5*<br>11<br>*3*<br>13<br>14<br>*35* |
| 2   | 20     | 1<br>2<br>*3*<br>4<br>*5*<br>*3*<br>7<br>8<br>*3*<br>*5*<br>11<br>*3*<br>13<br>14<br>*35*<br>16<br>17<br>*3*<br>19<br>*5* |
| 3   | 10     | 1<br>2<br>*3*<br>4<br>*5*<br>*3*<br>7<br>8<br>*3*<br>*5* |

```python
n = int(input("Enter the number: "))
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("*35*")
    elif i % 3 == 0:
        print("*3*")
    elif i % 5 == 0:
        print("*5*")
    else:
        print(i)
```

## Example 10:  Multiplication Table Printing
**Problem:** Write a program to create a multiplication table (from 1 to 10) for the entered integer `n`.

| No. | Inputs | Outputs | 
| --- | ------ | ------- |
| 1   | 3      | 3 x 1 = 3<br>3 x 2 = 6<br>3 x 3 = 9<br>3 x 4 = 12<br>3 x 5 = 15<br>3 x 6 = 18<br>3 x 7 = 21<br>3 x 8 = 24<br>3 x 9 = 27<br>3 x 10 = 30 |
| 2   | 5      | 5 x 1 = 5<br>5 x 2 = 10<br>5 x 3 = 15<br>5 x 4 = 20<br>5 x 5 = 25<br>5 x 6 = 30<br>5 x 7 = 35<br>5 x 8 = 40<br>5 x 9 = 45<br>5 x 10 = 50 |
| 3   | 7      | 7 x 1 = 7<br>7 x 2 = 14<br>7 x 3 = 21<br>7 x 4 = 28<br>7 x 5 = 35<br>7 x 6 = 42<br>7 x 7 = 49<br>7 x 8 = 56<br>7 x 9 = 63<br>7 x 10 = 70 |

```python
n = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```


**Notes:** All the examples above are solved using Python. You can find the solutions in the [examples](./examples) folder. Covered with explanations and comments, these examples will help you understand the practical implementation of the concepts covered in this module. Python tests are also included to verify the correctness of the solutions.