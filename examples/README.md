# Examples 👨🏼‍💻

Here are some examples to get you started.

<details open>
<summary><b>Covered topics</b></summary>

| Topic Covered                                           | Code with explanations                           |
| ------------------------------------------------------- | ------------------------------------------------- |
| - Hello, Python! Printing                     | [Detailed code](./example_1.py)      |
|  Number Range Printing                        | [Detailed code](./example_2.py)      |
|  Average Grade Calculation                    | [Detailed code](./example_3.py)      |
|  Number of # Characters Printing              | [Detailed code](./example_4.py)      |
|  Triangle of Numbers Printing                 | [Detailed code](./example_5.py)      |
|  Positive, Negative, and Zero Numbers Counting | [Detailed code](./example_6.py)      |
|  Two-Digit Odd Numbers Printing                | [Detailed code](./example_7.py)      |
|  Number of Digits Counting                     | [Detailed code](./example_8.py)      |
|  Printing Numbers with Conditions             | [Detailed code](./example_9.py)      |
| Multiplication Table Printing                | [Detailed code](./example_10.py)    |
| Sum of Products Calculation                  | [Detailed code](./example_11.py)    |
| Number Entry and Exit                        | [Detailed code](./example_12.py)    |
| Sum of Integers Calculation                  | [Detailed code](./example_13.py)    |
| Pattern Printing                             | [Detailed code](./example_14.py)    |
| Factorial Calculation                        | [Detailed code](./example_15.py)    |
| Sum of Sequence Elements Calculation         | [Detailed code](./example_16.py)    |
| Sum of Digits Calculation                    | [Detailed code](./example_17.py)    |
| Power Calculation                            | [Detailed code](./example_18.py)    |
| Power Calculation                            | [Detailed code](./example_19.py)    |
| Quiz Winner Determination                    | [Detailed code](./example_20.py)    |
| Average Speed Calculation                    | [Detailed code](./example_21.py)    |
| Automorphic Number Determination             | [Detailed code](./example_22.py)    |
| Least Common Multiple Calculation            | [Detailed code](./example_23.py)    |
| Monotonous Sequence Printing                 | [Detailed code](./example_24.py)    |
| Fibonacci Number Determination               | [Detailed code](./example_25.py)    |
| Sequence Element Comparison                  | [Detailed code](./example_26.py)    |
| Sequence Element Comparison                  | [Detailed code](./example_27.py)    |
| Fibonacci Number Determination               | [Detailed code](./example_28.py)    |
| Sequence Element Comparison                  | [Detailed code](./example_29.py)    |
| Sequence Element Comparison                  | [Detailed code](./example_30.py)    |
| Sequence Element Comparison                  | [Detailed code](./example_31.py)    |

</details>

## Example 1 - Hello, Python! Printing

**Problem:** Print the message "Hello, Python!" on the screen `n` times (where `n` is an integer entered by the user).

| No. | Inputs | Outputs                         |
| --- | ------ | ------------------------------- |
| 1   | 3      | Hello, Python!<br>Hello, Python!<br>Hello, Python! |
| 2   | 5      | Hello, Python!<br>Hello, Python!<br>Hello, Python!<br>Hello, Python!<br>Hello, Python! |
| 3   | 1      | Hello, Python! |


<details open>
<summary><b>Python Solution</b></summary>

```python 
n = int(input("Enter the number of times to print the message: "))
for _ in range(n):
    print("Hello, Python!")
```

</details>

## Example 2: Number Range Printing

**Problem:** Given two integers `a` and `b` (`a ≤ b`). Print all numbers from `a` to `b` inclusive.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 1<br>12 | 1 2 3 4 5 6 7 8 9 10 11 12 |
| 2   | 5<br>10 | 5 6 7 8 9 10 |
| 3   | 0<br>0  | 0 |


<details open>
<summary><b>Python Solution</b></summary>

```python {.line-numbers}
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a <= b:
    for i in range(a, b + 1):
        print(i, end=" ")
else:
    for i in range(a, b - 1, -1):
        print(i, end=" ")
```
</details>

## Example 3: Average Grade Calculation

**Problem:** A user enters the number of subjects `n`, and then, accordingly, the student's grades in `n` subjects. Determine the average grade.

| No. | Inputs | Outputs                |
| --- | ------ | ---------------------- |
| 1   | 5<br>10<br>11<br>9<br>8<br>10 | 9.60 |
| 2   | 3<br>5<br>5<br>5              | 5.00 |
| 3   | 1<br>10                        | 10.00 |

<details open>
<summary><b>Python Solution</b></summary>

```python

n = int(input("Enter the number of subjects: "))

total = 0

for _ in range(n):
    grade = int(input("Enter the grade: "))
    total += grade

average = total / n

print(f"The average grade is: {average:.2f}")
```
</details>


## Example 4: Number of # Characters Printing

**Problem:** Write a program to print integers from `n` to `0` with the number of `#` characters equal to the value of the number.

| No. | Inputs | Outputs                               |
| --- | ------ | ------------------------------------- |
| 1   | 6      | 6 ######<br>5 #####<br>4 ####<br>3 ###<br>2 ##<br>1 # |
| 2   | 3      | 3 ###<br>2 ##<br>1 # |
| 3   | 1      | 1 # |

<details open>
<summary><b>Python Solution</b></summary>

```python

n = int(input("Enter the number: "))

for i in range(n, -1, -1):
    print(i, "#" * i)
```
</details>

## Example 5: Triangle of Numbers Printing

**Problem:** Given an integer `n` (1 ≤ `n` ≤ 9). Print a triangle of numbers from `1` to `n` as shown in the example.

| No. | Inputs | Outputs             |
| --- | ------ | ------------------- |
| 1   | 9      | 1<br>22<br>333<br>4444<br>55555<br>666666<br>7777777<br>88888888<br>999999999 |
| 2   | 5      | 1<br>22<br>333<br>4444<br>55555 |
| 3   | 1      | 1 |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number: "))
for i in range(1, n + 1):
    print(str(i) * i)
```
</details>

## Example 6: Positive, Negative, and Zero Numbers Counting

**Problem:** Write a program that counts the positive and negative numbers, as well as zeros entered by the user, and outputs their quantity in one line with one space between them.

| No. | Inputs | Outputs                      |
| --- | ------ | ---------------------------- |
| 1   | 5<br>12<br>-45<br>0<br>14<br>0 | 2 1 2 |
| 2   | 1<br>2<br>3<br>4<br>5<br>6 | 6 0 0 |
| 3   | -1<br>-2<br>-3<br>-4<br>-5<br>-6 | 0 6 0 |

<details open>
<summary><b>Python Solution</b></summary>

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
</details>

## Example 7: Two-Digit Odd Numbers Printing

**Problem:** Print all two-digit odd numbers whose last digit is `n` - an integer entered by the user.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 5      | 15 25 35 45 55 65 75 85 95 |
| 2   | 1      | 11 21 31 41 51 61 71 81 91 |
| 3   | 0      | 10 20 30 40 50 60 70 80 90 |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number: "))

for i in range(10, 100):
    if i % 2 != 0 and i % 10 == n:
        print(i, end=" ")
```
</details>

## Example 8: Number of Digits Counting

**Problem:** Given a natural number `n`. Determine the number of digits in it.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 12367832 | 8       |
| 2   | 142      | 3       |
| 3   | 0        | 1       |

<details open>
<summary><b>Python Solution</b></summary>

```python

n = int(input("Enter the number: "))

count = 0

while n > 0:
    n //= 10 # Decrease the number by one digit
    count += 1 # Increase the count by one

print(count)
```
</details>

## Example 9: Printing Numbers with Conditions

**Problem:** Write a program that prints integers from `1` to `n` (1 < `n` ≤ 1000) with the following condition: for numbers divisible by 3, it prints `*3*` instead of the number, for numbers divisible by 5, it prints `*5*`, and for numbers divisible by 3 and 5 simultaneously, the message will be `*35*`.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 15     | 1<br>2<br>\*3\*<br>4<br>\*5\*<br>\*3\*<br>7<br>8<br>\*3\*<br>\*5\*<br>11<br>\*3\*<br>13<br>14<br>\*35\* |
| 2   | 20     | 1<br>2<br>\*3\*<br>4<br>\*5\*<br>\*3\*<br>7<br>8<br>\*3\*<br>\*5\*<br>11<br>\*3\*<br>13<br>14<br>\*35\*<br>16<br>17<br>\*3\*<br>19<br>\*5\* |
| 3   | 10     | 1<br>2<br>\*3\*<br>4<br>\*5\*<br>\*3\*<br>7<br>8<br>\*3\*<br>\*5\* |

<details open>
<summary><b>Python Solution</b></summary>

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
</details>

## Example 10:  Multiplication Table Printing

**Problem:** Write a program to create a multiplication table (from 1 to 10) for the entered integer `n`.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 3      | 3 x 1 = 3<br>3 x 2 = 6<br>3 x 3 = 9<br>3 x 4 = 12<br>3 x 5 = 15<br>3 x 6 = 18<br>3 x 7 = 21<br>3 x 8 = 24<br>3 x 9 = 27<br>3 x 10 = 30 |
| 2   | 5      | 5 x 1 = 5<br>5 x 2 = 10<br>5 x 3 = 15<br>5 x 4 = 20<br>5 x 5 = 25<br>5 x 6 = 30<br>5 x 7 = 35<br>5 x 8 = 40<br>5 x 9 = 45<br>5 x 10 = 50 |
| 3   | 7      | 7 x 1 = 7<br>7 x 2 = 14<br>7 x 3 = 21<br>7 x 4 = 28<br>7 x 5 = 35<br>7 x 6 = 42<br>7 x 7 = 49<br>7 x 8 = 56<br>7 x 9 = 63<br>7 x 10 = 70 |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```
</details>

## Example 11: Sum of Products Calculation


**Problem:** For a given integer `n` (n > 1), calculate the value `1 × 2 + 2 × 3 + …​ + (n - 1) × n`.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 6      | 70      |
| 2   | 5      | 40      |
| 3   | 3      | 8       |

<details open>
<summary><b>Python Solution</b></summary>
    
```python
n = int(input("Enter the number: "))
total = 0

for i in range(1, n):
    total += i * (i + 1)

print(total)

```
</details>

## Example 12: Number Entry and Exit

**Problem:** Write a program where the user enters integers. If an integer `n` is entered, the program should end its execution with the message `Done`. First, the user enters the number `n`, and then the rest of the numbers. 

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 5<br>67<br>112<br>14<br>5 | Done |
| 2   | 3<br>1<br>2<br>3 | Done |
| 3   | 1<br>1 | Done |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number: "))

while True:
    number = int(input("Enter the number: "))
    if number == n:
        print("Done")
        break
```
</details>

## Example 13: Sum of Integers Calculation

**Problem:** Given `n` integers. Each number is entered on a separate line. Calculate the sum of the numbers.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 10<br>0<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9 | 45 |
| 2   | 3<br>1<br>2<br>3 | 6 |
| 3   | 1<br>1 | 1 |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number of integers: "))
total = 0

for _ in range(n):
    total += int(input("Enter the number: "))

print(total)
```
</details>

## Example 14: Pattern Printing

**Problem:** Write a program to build a pattern as in the output data for the entered value `n`.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 7      | 1  2  3  4  5  6  7<br>2  3  4  5  6  7<br>3  4  5  6  7<br>4  5  6  7<br>5  6  7<br>6  7<br>7 |
| 2   | 5      | 1  2  3  4  5<br>2  3  4  5<br>3  4  5<br>4  5<br>5 |
| 3   | 3      | 1  2  3<br>2  3<br>3 |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number: "))
for i in range(1, n + 1):
    for j in range(i, n + 1):
        print(j, end=" ")
    print()
```
</details>

## Example 15: Factorial Calculation

**Problem:** Given a positive integer `n`, calculate the value of `n!` - the factorial of this number.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 3      | 6       |
| 2   | 4      | 24      |
| 3   | 1      | 1       |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(factorial)
```
</details>

**Note** We assign the value `1` to the variable `factorial` because the factorial of `0` is `1`. Then, we use a `for` loop to iterate through the numbers from `1` to `n` and multiply them to the `factorial` variable. Also, we can't assign it to `0` because the multiplication of any number by `0` is `0`.

## Example 16: Sum of Sequence Elements Calculation

**Problem:** Determine the sum of all elements of the sequence that ends with the number `0`. A sequence of integers that ends with the number `0` is entered (the number `0` itself is not included in the sequence, but is used as a sign of its end).

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 2<br>5<br>3<br>0 | 10 |
| 2   | 1<br>2<br>3<br>4<br>5<br>0 | 15 |
| 3   | 0 | 0 |

<details open>
<summary><b>Python Solution</b></summary>

```python
total = 0

while True:
    number = int(input("Enter the number: "))
    if number == 0:
        break
    total += number

print(total)
```
</details>

## Example 17: Largest Element Calculation

**Problem:** Given a sequence of natural numbers, ending with the number `0`. Determine the value of the largest element in the sequence.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 5<br>3<br>8<br>0 | 8 |
| 2   | 1<br>2<br>3<br>4<br>5<br>0 | 5 |
| 3   | 17<br>12<br>3<br>0 | 17 |

<details open>
<summary><b>Python Solution</b></summary>

```python
max_number = 0

while True:
    number = int(input("Enter the number: "))
    if number == 0:
        break
    if number > max_number:
        max_number = number

print(max_number)
```
</details>


## Example 18: Sum of Digits Calculation

**Problem:** Write a program that outputs all three-digit numbers whose sum of digits is equal to a certain value `n` entered by the user.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 4      | 112 121 130 202 211 220 301 310 400 |
| 2   | 5      | 104 113 122 131 140 203 212 221 230 302 311 320 401 410 500 |
| 3   | 6      | 105 114 123 132 141 150 204 213 222 231 240 303 312 321 330 402 411 420 501 510 600 |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number: "))

digits_total = 0

for i in range(100, 1000):
    current_number = i
    digits_total = 0
    
    while current_number > 0:
        digits_total += current_number % 10
        current_number //= 10

    if digits_total == n:
        print(i, end=" ")
```

</details>


## Example 19: Power Calculation

**Problem:** Given integers `a` and `b`. Calculate `a` to power of `b` without using the exponentiation operation.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 2<br>3  | 8       |
| 2   | 3<br>3  | 27      |
| 3   | 5<br>2  | 25      |

<details open>
<summary><b>Python Solution</b></summary>

```python
a = int(input("Enter the base: "))
b = int(input("Enter the exponent: "))

result = 1

for _ in range(b):
    result *= a

print(result)
```
</details>


## Example 20: Quiz Winner Determination

**Problem:** High school students took part in a computer science quiz. They had to answer 20 questions. The winner of the quiz is the participant who correctly answered the most questions. How many questions did the winner answer correctly? If there are participants in the quiz who could not give a correct answer to any of the questions, print Yes, otherwise print No. It is guaranteed that there are participants who correctly answered at least one question. The program receives the number of quiz participants `n` (1 ≤ `n` ≤ 50) as input, then for each participant, the number of questions they answered correctly is entered.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 5<br>10<br>15<br>7<br>0<br>16 | 16<br>Yes |
| 2   | 3<br>0<br>0<br>0<br>0 | 0<br>Yes |
| 3   | 4<br>20<br>20<br>20<br>20 | 20<br>No |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number of participants: "))
max_score = 0
failed_quiz = False

for _ in range(n):
    score = int(input("Enter the score: "))
    if score > max_score:
        max_score = score
    elif score == 0:
        failed_quiz = True

print(max_score)
print("Yes" if failed_quiz else "No")
```
</details>

## Example 21: Average Speed Calculation

**Problem:** A surveillance camera automatically registers the speed of passing cars, rounding the speed values to integers. It is necessary to determine the average registered speed of all cars. If the speed of at least one car was more than 60 km/h, print Yes, otherwise print No. The program receives the number of registered cars `n` (1 ≤ `n` ≤ 30) as input, then the speeds of the cars are indicated. The speed value cannot be less than 1 and more than 300. The program should first print the average speed with an accuracy of one decimal place, then Yes or No.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 3<br>50<br>45<br>65 | 53.3<br>Yes |
| 2   | 2<br>100<br>200 | 150.0<br>Yes |
| 3   | 1<br>30 | 30.0<br>No |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number of cars: "))

total_speed = 0
over_speed = False

for _ in range(n):
    speed = int(input("Enter the speed: "))
    total_speed += speed
    if speed > 60:
        over_speed = True

average_speed = total_speed / n
print(f"{average_speed:.1f}")
print("Yes" if over_speed else "No")
```

</details>

## Example 22: Automorphic Number Determination

**Problem:** Given a natural number `n`. Determine if it is an automorphic number. Note. An automorphic number is a number whose square is equal to the last digits of the square of this number: 5 - 25, 6 - 36, 25 - 625.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 9376   | True    |
| 2   | 26     | False   |
| 3   | 25     | True    |
| 4   | 6      | True    |
| 5   | 5      | True    |
| 6   | 1      | True    |
| 7   | 76     | True    |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number: "))
temp_number = n

square = n ** 2
digit_count = 0

while temp_number > 0:
    temp_number //= 10
    digit_count += 1

power = 10 ** digit_count

if square % power == n:
    print(True)
else:
    print(False)

```

</details>

## Example 23: Least Common Multiple Calculation

**Problem:** Write a program that helps to find the least common multiple (LCM) of two numbers. The program should read two positive integers `a` and `b` (each number is entered on a separate line) and print the smallest number that is divisible by both of these numbers without a remainder.
The formula to calculate the Least Common Multiple (LCM) of two numbers `a` and `b` is given by:

$$\text{LCM}(a, b) = \frac{|ab|}{\text{GCD}(a, b)},$$

where $\text{GCD}(a, b)$ is the greatest common divisor of numbers `a` and `b`.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 4<br>6  | 12      |
| 2   | 15<br>25 | 75      |
| 3   | 1<br>1   | 1       |
| 4   | 5<br>8   | 40      |

<details open>
<summary><b>Python Solution</b></summary>

```python
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

x = a
y = b

product = a * b

# Solution 1
while b:
    a, b = b, a % b

gcd = a
lcm = product // gcd
print(lcm)

# Solution 2
while y != 0:
    temp = y
    y = x % y
    x = temp

gcd = x
lcm = product // gcd
print(lcm)
```

</details>

## Example 24: Monotonous Sequence Printing

**Problem:** Given a natural number `n`. Print the first `n` members of the sequence. The sequence is a monotonous sequence in which each natural number `k` occurs exactly `k` times: 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, ....

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 1     | 1       |
| 2   | 2     | 1 2     |
| 3   | 3     | 1 2 2   |
| 4   | 4     | 1 2 2 3 |
| 5   | 5     | 1 2 2 3 3 |
| 6   | 6     | 1 2 2 3 3 3 |
| 7   | 7     | 1 2 2 3 3 3 4 |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number: "))

i = 1
count = 0

while count < n:
    for _ in range(i):
        if count < n:
            print(i, end=" ")
            count += 1
    i += 1
```

</details>


## Example 25: Fibonacci Number Determination

**Problem:** Given a natural number `n`. Determine which Fibonacci number it is. If `n` is not a Fibonacci number, print the value `-1`. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. The sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 11     | -1      |
| 2   | 8      | 6       |
| 3   | 13     | 7       |
| 4   | 21     | 8       |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number: "))

a = 0
b = 1
c = 0
count = 0

while c < n:
    c = a + b
    a = b
    b = c
    count += 1

if c == n:
    print(count)
else:
    print(-1)
```

</details>

## Example 26: Sequence Element Comparison

**Problem:** Given a sequence of natural numbers that ends with the number `0`. Determine how many elements of this sequence are greater than the previous element.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 4<br>3<br>6<br>8<br>0 | 2 |
| 2   | 1<br>2<br>3<br>4<br>0 | 3 |
| 3   | 1<br>1<br>1<br>1<br>0 | 0 |

<details open>
<summary><b>Python Solution</b></summary>

```python
count = 0
previous = int(input("Enter the number: "))

while True:
    number = int(input("Enter the number: "))
    if number == 0:
        break
    if number > previous:
        count += 1
    previous = number

print(count)
```

</details>

**Problem:** Given a sequence of natural numbers that ends with the number `0`. Determine how many elements of this sequence are equal to its largest element.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 3<br>8<br>10<br>2<br>10<br>7<br>0 | 2 |
| 2   | 1<br>2<br>3<br>4<br>0 | 1 |
| 3   | 1<br>1<br>1<br>1<br>0 | 4 |

<details open>
<summary><b>Python Solution</b></summary>

```python
max_number = 0
max_count = 0

while True:
    number = int(input("Enter the number: "))
    if number == 0:
        break
    if number > max_number:
        max_number = number
        max_count = 1
    elif number == max_number:
        max_count += 1

print(max_count)
```

</details>

## Example 28: Sequence Element Comparison

**Problem:** Given a sequence of natural numbers that ends with the number `0`. Determine the largest number of elements in this sequence that go one after the other and are equal to each other (i.e., the longest consecutive sequence of identical elements). Also, print the element that is repeated most consecutively. If there are multiple elements with the same maximum consecutive count, the task does not specify which one to print, so we'll choose to print any one of them.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 1<br>5<br>5<br>4<br>3<br>9<br>9<br>9<br>7<br>0 | 3<br>9 |
| 2   | 1<br>2<br>3<br>4<br>0 | 1<br>No numbers were entered before 0. |
| 3   | 1<br>1<br>1<br>1<br>0 | 4<br>1 |


<details open>
<summary><b>Python Solution</b></summary>

```python
max_count = 0
max_element = None
current_count = 1
last_element = None

number = int(input("Enter a number (0 to end): "))
last_element = number

while number != 0:
    number = int(input("Enter a number (0 to end): "))
    
    if number == last_element:
        current_count += 1
    else:
        if current_count > max_count:
            max_count = current_count
            max_element = last_element
        current_count = 1
    
    last_element = number

if current_count > max_count:
    max_count = current_count
    max_element = last_element

print(f"Longest sequence length: {max_count}")
if max_count > 0:
    print(f"Most repeated element: {max_element}")
else:
    print("No numbers were entered before 0.")

```

</details>


## Example 29: Divisibility Graphical Representation

**Problem:** Write a program to graphically represent the divisibility of numbers from `1` to `n` (the value of `n` is entered from the keyboard). In each line, print the next number and as many `+` characters as there are divisors of this number.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 1     | 1+      |
| 2   | 2     | 1+<br>2++ |
| 3   | 3     | 1+<br>2++<br>3++ |
| 4   | 4     | 1+<br>2++<br>3++<br>4+++ |
| 5   | 5     | 1+<br>2++<br>3++<br>4+++<br>5++ |
| 6   | 6     | 1+<br>2++<br>3++<br>4+++<br>5++<br>6++++ |
| 7   | 7     | 1+<br>2++<br>3++<br>4+++<br>5++<br>6++++<br>7++ |
| 8   | 8     | 1+<br>2++<br>3++<br>4+++<br>5++<br>6++++<br>7++<br>8++++ |
| 9   | 9     | 1+<br>2++<br>3++<br>4+++<br>5++<br>6++++<br>7++<br>8++++<br>9++++ |
| 10  | 10    | 1+<br>2++<br>3++<br>4+++<br>5++<br>6++++<br>7++<br>8++++<br>9++++<br>10++++ |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number: "))

for i in range(1, n + 1):
    divisors = 0
    for j in range(1, i + 1):
        if i % j == 0:
            divisors += 1
    print(f"{i}{'+' * divisors}")
```

</details>

## Example 30: Number Reversal

**Problem:** Given a natural number `n`. Print the number that is the reverse of the order of its digits.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 125    | 521     |
| 2   | 123456789 | 987654321 |
| 3   | 1      | 1       |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number: "))
temp_number = n

reversed_number = 0

# Solution 1
while n > 0:
    reversed_number = reversed_number * 10 + n % 10
    n //= 10

print(reversed_number)

# Solution 2
n = temp_number
power = 0 
while temp_number > 0:
    temp_number //= 10
    power += 1

reversed_number = 0

while n > 0:
    current_digit = n % 10
    number_to_add = current_digit * (10 ** (power - 1))
    reversed_number += number_to_add
    n //= 10
    power -= 1

print(reversed_number)
```

</details>

## Example 31: Number of Digits Counting

**Problem:** In one country, banknotes with denominations of 1, 2, 4, 8, 16, 32, and 64 are used. Given a natural number `n`. What is the smallest number of such banknotes that can be used to pay the amount `n` (indicate the number of each of the banknotes used for payment)? It is assumed that there are enough banknotes of all denominations.

| No. | Inputs | Outputs                        |
| --- | ------ | ------------------------------ |
| 1   | 165    | (128)<br>(32)<br>(4)<br>(1)     |
| 2   | 1      | (1)                            |
| 3   | 2      | (2)                            |
| 4   | 3      | (2)<br>(1)                     |
| 5   | 4      | (4)                            |
| 6   | 5      | (4)<br>(1)                     |
| 7   | 65     | (64)<br>(1)                    |
| 8   | 7      | (4)<br>(2)<br>(1)              |
| 9   | 225    | (128)<br>(64)<br>(32)<br>(1)   |
| 10  | 9      | (8)<br>(1)                     |


<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number: "))

ones = 0
twos = 0
fours = 0
eights = 0
sixteens = 0
thirty_twos = 0
sixty_fours = 0

while n > 0:
    if n >= 64:
        sixty_fours += 1
        n -= 64
    elif n >= 32:
        thirty_twos += 1
        n -= 32
    elif n >= 16:
        sixteens += 1
        n -= 16
    elif n >= 8:
        eights += 1
        n -= 8
    elif n >= 4:
        fours += 1
        n -= 4
    elif n >= 2:
        twos += 1
        n -= 2
    else:
        ones += 1
        n -= 1

if sixty_fours > 0:
    print(f"{sixty_fours} (64)")
if thirty_twos > 0:
    print(f"{thirty_twos} (32)")
if sixteens > 0:
    print(f"{sixteens} (16)")
if eights > 0:
    print(f"{eights} (8)")
if fours > 0:
    print(f"{fours} (4)")
if twos > 0:
    print(f"{twos} (2)")
if ones > 0:
    print(f"{ones} (1)")
```
</details>

**Notes:** All the examples above are solved using Python. You can find the solutions in the [examples](./examples) folder. Covered with explanations and comments, these examples will help you understand the practical implementation of the concepts covered in this module. Python tests are also included to verify the correctness of the solutions.
