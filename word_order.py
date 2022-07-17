# word counter 
from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input('enter words: ') for _ in range(int(input('how many words you want?:'))))
print(len(d))
print(*d.values())