#### 1. Stressful Subject
The function should recognise if a subject line is stressful. A stressful subject line means that all letters are in uppercase, and/or ends by at least 3 exclamation marks, and/or contains at least one of the following “red” words: "help", "asap", "urgent". Any of those "red" words can be spelled in different ways - "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P", even in a very loooong way "HHHEEEEEEEEELLP," they just can't have any other letters interspersed between them.
```
import re
def is_stressful(subj):
    red=["help", "asap", "urgent"]
    matchers = [
        re.compile('+[.!-]*'.join(iter(word)), re.I)
        for word in red
    ]
    return (subj.isupper() or
            subj.endswith('!!!') or
            any(re.search(rgx, subj) for rgx in matchers))
```
