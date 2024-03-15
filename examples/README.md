# Examples 👨🏼‍💻

Here are some examples to get you started.

**Covered topics:**

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

## Problem 11: Sum of Products Calculation


**Problem** For a given integer `n` (n > 1), calculate the value `1 × 2 + 2 × 3 + …​ + (n - 1) × n`.

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

## Problem 12: Number Entry and Exit

**Problem** Write a program where the user enters integers. If an integer `n` is entered, the program should end its execution with the message `Done`. First, the user enters the number `n`, and then the rest of the numbers. 

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 5<br>67<br>112<br>14<br>5 | Done |
| 2   | 3<br>1<br>2<br>3 | Done |
| 3   | 1<br>1 | Done |

## Problem 13

Дано n цілих чисел. Кожне число вводиться в окремому рядку. Обчисліть суму чисел.

Вхідні дані:

10
0
1
2
3
4
5
6
7
8
9
Вихідні дані:

45

## Problem 14

Напишіть програму для побудови шаблону як у вихідних даних за введеним значенням n.

Вхідні дані:

7
Вихідні дані:

1  2  3  4  5  6  7
2  3  4  5  6  7
3  4  5  6  7
4  5  6  7
5  6  7
6  7
7

## Problem 15

За даним цілим додатнім числом n обчисліть n! - значення факторіалу цього числа.

Вхідні дані:

3
4
1
Вихідні дані:

6
24
1

## Problem 16

Визначте суму усіх елементів послідовності, яка завершується числом 0. Вводиться послідовність цілих чисел, що закінчується числом 0 (саме число 0 в послідовність не входить, а використовується як ознака її закінчення).

Вхідні дані:

2
5
3
0
Вихідні дані:

10

## Problem 17

Послідовність складається з натуральних чисел і завершується числом 0. Визначте значення найбільшого елемента послідовності. Вводиться послідовність цілих чисел, що закінчується числом 0 (саме число 0 в послідовність не входить, а використовується як ознака її закінчення).

Вхідні дані:

5
3
8
0
Вихідні дані:

8

## Problem 18

Напишіть програму, яка виводить усі трицифрові числа, сума цифр яких дорівнює деякому значенню n, яке вводить користувач.

Вхідні дані:

4
Вихідні дані:

112
121
130
202
211
220
301
310
400

## Problem 19

Дано цілі числа a і b. Обчислити ab, не використовуючи операцію піднесення до степеня.

Вхідні дані:

4
2
Вихідні дані:

16

## Problem 20

Старшокласники брали участь у вікторині з інформатики. Необхідно було відповісти на 20 питань. Переможцем вікторини вважається учасник, який правильно відповів на найбільшу кількість запитань. На скільки питань переможець відповів правильно? Якщо є учасники вікторини, які не змогли дати правильну відповідь ні на одне із запитань, виведіть Yes, інакше виведіть No. Гарантується, що є учасники, які правильно відповіли хоча б на одне запитання. Программа отримує на вхід число учасників вікторини n (1 ≤ n ≤ 50), потім для кожного учасника вводиться кількість питань, на які отримано правильну відповідь.

Вхідні дані:

5
10
15
7
0
16
Вихідні дані:

16
Yes

## Problem 21

Камера спостереження реєструє в автоматичному режимі швидкість проїжджаючих повз неї автомобілів, округляючи значення швидкості до цілих чисел. Необхідно визначити середню зареєстровану швидкість всіх автомобілів. Якщо швидкість хоча б одного автомобіля була більше 60 км/год, виведіть Yes, інакше виведіть No. Програма отримує на вхід число зафіксованих автомобілів n (1 ≤ n ≤ 30), потім вказуються їх швидкості. Значення швидкості не може бути менше 1 і більше 300. Програма повинна спочатку вивести середню швидкість з точністю до одного знака після десяткової крапки, потім Yes або No.

Вхідні дані:

3
50
45
65
Вихідні дані:

53.3
Yes

## Problem 22

Дано натуральне число n. Визначити, чи є воно автоморфним числом. Примітка. Автоморфне число - число, квадрат якого рівний останнім розрядами квадрата цього числа: 5 - 25, 6 - 36, 25 - 625.

Вхідні дані:

9376
26
Вихідні дані:

True
False

## Problem 23

Напишіть програму, яка допомагає знайти число (НСК - найменше спільне кратне) двох чисел. Програма повинна зчитувати два додатних цілих числа a і b (кожне число вводиться на окремому рядку) і виводити найменше число, яке ділиться на обидва цих числа без залишку. НСК(a, b) = |ab| / НСД(a, b), де НСД(a, b) - найбільший спільний дільник чисел a, b.

Вхідні дані:

8
5
Вихідні дані:

40

## Problem 24

Є монотонна послідовність, в якій кожне натуральне число k зустрічається рівно k разів: 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, .... За введеним натуральним числом n виведіть перші n членів цієї послідовності.

Вхідні дані:

5
Вихідні дані:

1 2 2 3 3

## Problem 25

Дано натуральне число n. Визначте, яким за рахунком числом Фібоначчі воно є. Якщо n не є числом Фібоначчі, виведіть значення -1.

Вхідні дані:

11
8
Вихідні дані:

-1
6

## Problem 26

Послідовність складається з натуральних чисел і завершується числом 0. Визначте, скільки елементів цієї послідовності більше попереднього елемента. Вводиться послідовність цілих чисел, що закінчується числом 0 (саме число 0 в послідовність не входить, а використовується як ознака її закінчення).

Вхідні дані:

4
3
6
8
0
Вихідні дані:

2

## Problem 27

Послідовність складається з натуральних чисел і завершується числом 0. Визначте, скільки елементів цієї послідовності рівні її найбільшому елементу. Вводиться послідовність цілих чисел, що закінчується числом 0 (саме число 0 в послідовність не входить, а використовується як ознака її закінчення).

Вхідні дані:

3
8
10
2
10
7
0
Вихідні дані:

2

## Problem 28

Дано послідовність натуральних чисел, що завершується числом 0. Визначте найбільше число елементів цієї послідовності, що йдуть підряд один за одним, і дорівнюють один одному. Вводиться послідовність цілих чисел, що закінчується числом 0 (саме число 0 в послідовність не входить, а використовується як ознака її закінчення). Додаткове завдання: виведіть найбільш повторюваний елемент послідовності.

Вхідні дані:

1
5
5
4
3
9
9
9
7
0
Вихідні дані:

3

## Problem 29

Скласти програму для графічного зображення подільності чисел від 1 до n (значення n вводиться з клавіатури). У кожному рядку треба надрукувати чергове число і стільки символів +, скільки є дільників у цього числа.

Вхідні дані:

5
Вихідні дані:

1+
2++
3++
4+++
5++

## Problem 30

Вводиться ціле число n. Вивести число, зворотне по порядку складових його цифр.

Вхідні дані:

125
123456789
1
Вихідні дані:

521
987654321
1

## Problem 31

В одній країні використовуються грошові купюри номіналом в 1, 2, 4, 8, 16, 32 і 64. Дано натуральне число n. Якою найменшою кількістю таких грошових знаків можна виплатити суму n (вказати кількість кожної з використовуваних для виплати купюр)? Передбачається, що є досить велика кількість купюр всіх номіналів.

Вхідні дані:

165
Вихідні дані:

2 (64)
1 (32)
1 (4)
1 (1)

**Notes:** All the examples above are solved using Python. You can find the solutions in the [examples](./examples) folder. Covered with explanations and comments, these examples will help you understand the practical implementation of the concepts covered in this module. Python tests are also included to verify the correctness of the solutions.
