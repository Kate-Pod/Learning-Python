**Здесь представлены мои решения с сайта py.checkio (https://py.checkio.org/user/Kate-Pod/)**  
*В формате md для разнообразия и удобства чтения.*

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
```
def is_all_upper(text: str) -> bool:
    if text==text.upper() or text ==' ':
        return True
    else:
        return False
```
#### 8. Replace First
The first element should become the last one
```
def replace_first(items: list) -> Iterable:
    if items.__len__()<=1:
        return items
    else:  
        items.append(items.pop(0))
        return items
```
#### 9. Max Digit
```
def max_digit(number: int) -> int:
    return int(max(str(number)))
```
#### 10. Split Pairs
Split the string into pairs of two characters.
**мое:**
```
def split_pairs(a):
    n=2
    b=[a[i:i+n] for i in range(0, len(a), n)]
    if len(a)%2==0:
        return [a[i:i+n] for i in range(0, len(a), n)]
    else:
        b.append(b.pop()+'_')
        return b
```
**best:**
```
def split_pairs(a):
    return [ch1+ch2 for ch1,ch2 in zip(a[::2],a[1::2]+'_')]
```
```
from textwrap import wrap

def split_pairs(a):
    a = a + '_' if len(a) % 2 else a
    return wrap(a, 2)
```
