#### 1. Sum Numbers
Sum the numbers.
```
def sum_numbers(text: str) -> int:
    return sum(int(i) for i in text.split() if i.isdigit())
```

#### 2. Even The Last
How to work with arrays indexes.
```
def checkio(array: list) -> int:
    m=0
    if len(array)==0:
        return m
    sum=0
    for i in range(0,len(array),2):
        sum+=array[i]
        m=sum*array[len(array)-1]
    return m
```
**best:**
```
def checkio(array: list) -> int:
    result = sum([num for num in array[::2]]) * array[-1] if array else 0
    return result
```

#### 3. Right to Left
You are given a sequence of strings. You should join these strings into a chunk of text where the initial strings are separated by commas. As a joke on the right handed robots, you should replace all cases of the words "right" with the word "left", even if it's a part of another word. All strings are given in lowercase.
```
def left_join(phrases: tuple) -> str:
    """
        Join strings and replace "right" to "left"
    """
    return (','.join(phrases)).replace('right','left')
```
#### 4. Right to Left
How to discern words and numbers.
```
def checkio(words: str) -> bool:
    с = 0
    for word in words.split():
        if word.isalpha():
            с += 1
        else:
            с = 0
        if c == 3:
            return True
    return False
```
