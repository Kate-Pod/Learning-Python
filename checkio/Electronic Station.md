#### 1. Words Order
You have a text and a list of words. You need to check if the words in a list appear in the same order as in the given text.
```
def words_order(text: str, words: list) -> bool:
  a = [x for x in text.split() if x in words]
  return a == words and sorted(set(a)) == sorted(words)
```
