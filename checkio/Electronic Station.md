#### 1. Words Order
You have a text and a list of words. You need to check if the words in a list appear in the same order as in the given text.
```
def words_order(text: str, words: list) -> bool:
    word_list = [text.index(word) for word in words if word in text.split()]      #порядок индексов, в котором встречаются слова words в text
    return sorted(word_list) == word_list and len(word_list) == len(set(words))   #set - в случае одинаковых слов в списке words
```
#### 2. Digits Multiplication
```
def checkio(number: int) -> int:
    ints = [int(i) for i in str(number) if i != '0'] 
    a = 1
    for n in ints: 
        a = a * n
    return a
```
#### 3. Sort by Extension
Sort the list by the file extension. The files with the same extension should be sorted by name. (example: ['1.cad', '1.bat', '.aa', '.bat'])
```
def sort_by_ext(files: List[str]) -> List[str]:
    l= list(str(f).rsplit('.',1) for f in files)  #rsplit - разделим каждый элемент в списке по точке (.) справа только один раз ('1.aa.doc' --> '1.aa', 'doc')
    return ['.'.join(a) for a in sorted(l, key = lambda x: (len(x[0])!= 0, x[1],x[0]))]
```
#### 5. Acceptable Password II
In this mission you need to create a password verification function.
Those are the verification conditions: the length should be bigger than 6; should contain at least one digit
```
import re
def is_acceptable_password(password: str) -> bool:
    return len(password)>6 and any([re.search(i,'0123456789') for i in password])
```
