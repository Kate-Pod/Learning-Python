#### 1. First Word
You are given a string and you have to find its first word.
```
def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    s=text.find(' ')
    if text[s] ==' ':
        return text[0:s]
    else:
        return text
```
#### 2. Acceptable Password I
In this mission, you need to create a password verification function. The verification condition is:the length should be bigger than 6.
```
def is_acceptable_password(password: str) -> bool:
    if len(password)>6:
        return True
    else:
      return False
```
#### 3. Number Length
You have a positive integer. Try to find out how many digits it has?
```
def number_length(a: int) -> int:
    s=str(a)
    return len(s)
```
#### 4. End Zeros
How many zeros are at the end?
#### мой:
```
def end_zeros(num: int) -> int:
   i=0
   if num==0:
      i=1
      return i
   while num>0:
      dig=num%10
      if dig==0:
         i+=1
      else:
         break
      num=num/10
   return i
```
#### best:
```
def end_zeros(number):
    n = str(number)
    return len(n) - len(n.strip('0'))
```
```
def end_zeros(number):
    result = not number
    while number and not number % 10:
        number /= 10
        result += 1
    return result
```
```
import re
def end_zeros(num: int) -> int:
    return len(re.search('0*$', str(num)).group(0))
```
```
def end_zeros(num: int) -> int:
    count = 0 if num != 0 else 1
    while num // 10 != 0 and num % 10 == 0:
        count += 1
        num //= 10
    return count
```
#### 5. Backward String
Reverse a string
```
def backward_string(val: str) -> str:
    return val[::-1]
```
#### 6. Remove All Before
Remove all the elements before the given one from the array.
```
def remove_all_before(items: list, border: int) -> Iterable:
   try:
      ind=items.index(border)
      for i in range(0,ind):
         items.pop(0)
      return items
   except:
      return items
```
#### 7. All Upper I
Are all symbols in upper case?


