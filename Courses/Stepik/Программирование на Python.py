## Программирование на Python
### Операторы.Переменные.Типы данных.Условия

Задачи: 
1: Коля каждый день ложится спать ровно в полночь и недавно узнал, что оптимальное время для его сна составляет XX минут. Коля хочет поставить себе будильник так, 
чтобы он прозвенел ровно через XX минут после полуночи, однако для этого необходимо указать время сигнала в формате часы, минуты. Помогите Коле определить, на какое 
время завести будильник. Часы и минуты в выводе программы должны располагаться на разных строках.

X = int(input())
print(int(X/60))
print(X%60)

2:Катя узнала, что ей для сна надо X минут. В отличие от Коли, Катя ложится спать после полуночи в H часов и M минут. Помогите Кате определить, на какое время ей поставить
будильник, чтобы он прозвенел ровно через X минут после того, как она ляжет спать. На стандартный ввод, каждое в своей строке, подаются значения X, H и M. Гарантируется, что 
Катя должна проснуться в тот же день, что и заснуть. Программа должна выводить время, на которое нужно поставить будильник: в первой строке часы, во второй — минуты.

X = int(input())
H = int(input())
M = int(input())
print(int((H*60+M+X)/60))
print(int((H*60+M+X)%60))

3: Из передачи “Здоровье” Аня узнала, что рекомендуется спать хотя бы A часов в сутки, но пересыпать тоже вредно и не стоит спать более B часов. Сейчас Аня спит H часов в сутки. 
    Если режим сна Ани удовлетворяет рекомендациям передачи “Здоровье”, выведите “Это нормально”. Если Аня спит менее A часов, выведите “Недосып”, если же более B часов, то 
    выведите “Пересып”.
Получаемое число A всегда меньше либо равно B.
На вход программе в три строки подаются переменные в следующем порядке: A, B, H.

A = int(input())
B = int(input())
H = int(input())
if A<=H<=B:
    print('Это нормально')
elif H<A:
    print('Недосып')
elif H>B:
    print('Пересып')

4: Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым 
 числам ("первое число" "операция" "второе число") и выводит результат на экран.
Поддерживаемые операции: +, -, /, '*', mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.
Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
Обратите внимание, что на вход программе приходят вещественные числа.

x =float(input())
y =float(input())
z=input()
if z=='+':
    print(x+y)
elif z=='-':
    print(x-y)
elif z=='*':
    print(x*y)
elif z=='/':
    if y==0:
        print('Деление на 0!')
    else:
        print(x/y)
elif z=='mod':
    if y==0:
        print('Деление на 0!')
    else:
        print(x%y)
elif z=='pow':
    print(x**y)
elif z=='div':
    if y==0:
        print('Деление на 0!')
    else:
        print(x//y)
5: Написать программу, на вход которой подаётся тип фигуры комнаты и соответствующие параметры, которая бы выводила площадь получившейся комнаты.
Для числа π использувать значение 3.14.

n = input()
if n=='прямоугольник':
    a = float(input())
    b = float(input())
    print(a*b)
elif n=='треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p=((a+b+c)/2)
    print((p*(p-a)*(p-b)*(p-c))**0.5)
elif n=='круг':
    r = float(input())
    print(3.14*r**2)

6: Напишите программу, считывающую с пользовательского ввода целое число nn (неотрицательное), выводящее это число в консоль вместе с правильным образом изменённым словом 
"программист", для того, чтобы робот мог нормально общаться с людьми, например: 1 программист, 2 программиста, 5 программистов.
В комнате может быть очень много программистов. Проверьте, что ваша программа правильно обработает все случаи, как минимум до 1000 человек.

n = int(input())
b='программист'
if n%10==1 and n%100!=11:
    print(n,b)
    if n%100==11:
        print(n,b+'ов')
elif 2<=n%10<=4 and n%100!=12 and n%100!=13 and n%100!=14:
    print(n,b+'а')
elif n==0:
    print(n,b+'ов')
else:
    print(n,b+'ов')

Эталон:
n=int(input())
print(n,'программист'+('ов' if n%10==0 or 4<n%10<10 or 10<n%100<15 else 'а' if 1<n%10<5 else ''))
```
**6:** Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.
```{r}
n = input()
if (int(n[0])+int(n[1])+int(n[2]))==(int(n[3])+int(n[4])+int(n[5])):
    print('Счастливый')
else:
    print('Обычный')

Или:
a, b, c, d, e, f = input()
n= int(a)+int (b)+int(c)
m= int(d)+int (e)+int(f)
if n==m:
    print ('Счастливый')
else:
    print ('Обычный')


### Циклы.Строки.Списки
#### Цикл While
Задачи:
1: Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке, и после первого введенного нуля выводит сумму полученных на вход чисел.

n = int (input())
a = 0
while n != 0:
    a += n
    n = int (input())
print (a)

2:Напишите программу, которая считывает целые числа с консоли по одному числу в строке.
Для каждого введённого числа проверить:
если число меньше 10, то пропускаем это число;
если число больше 100, то прекращаем считывать числа;
в остальных случаях вывести это число обратно на консоль в отдельной строке.

n = 0
while n <= 100:
    n = int(input())
    if 10 <= n <= 100:
        print(n)
Или:
n = 0
while n<=100:
  n = int (input())
  if n > 100:
    break
  if n<10:
    continue
  print(n)

#### Цикл for
Задачи:
1:Напишите программу, на вход которой даются четыре числа a, b, c и d, каждое в своей строке. Программа должна вывести фрагмент таблицы умножения для всех
чисел отрезка [a; b][a;b] на все числа отрезка [c;d][c;d]. Числа a, b, c и d являются натуральными и не превосходят 10.
Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции.
Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков — заголовочные столбец и строка таблицы.

a, b, c, d = int(input()), int(input()), int(input()), int(input())
for i in range(c, d+1):                     # добавляем 1 к d, чтобы выводилось второе число заголовком
    print('\t', i, end='')                  # табуляция для c и d
print()
for j in range(a, b+1):                     # добавляем 1 к b, чтобы в range читалась последняя граница
    print(j, end='\t')
    for k in range(c, d + 1): 
        print(j * k, end='\t')
    print()

2: Напишите программу, которая считывает с клавиатуры два числа aa и bb, считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a;b], 
   которые кратны числу 3.
    
a,b = int(input()), int(input())
c = 0
d = 0
for i in range (a,b+1):
    if i%3 == 0:
        c +=i
        d +=i
    i+=1
print(c/d)

#### Строки и символы
1:Напишите программу, которая вычисляет процентное содержание символов G (гуанин) и C (цитозин) в введенной строке (программа не должна зависеть от регистра вводимых символов). 
n=input()
print((n.upper().count('C'.upper())+n.upper().count('G'.upper()))/len(n)*100)










