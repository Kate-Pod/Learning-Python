#### 1. Words Order
You have a text and a list of words. You need to check if the words in a list appear in the same order as in the given text.
```
def words_order(text: str, words: list) -> bool:
    word_list = [text.index(word) for word in words if word in text.split()]
    return sorted(word_list) == word_list and len(word_list) == len(set(words))   #set - в случае одинаковых слов в списке words
```
