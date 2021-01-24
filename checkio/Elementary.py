# First Word
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
