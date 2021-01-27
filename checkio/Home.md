#### 1. Sum Numbers
Sum the numbers.
```
def sum_numbers(text: str) -> int:
    return sum(int(i) for i in text.split() if i.isdigit())
```

#### 1. Sum Numbers
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
