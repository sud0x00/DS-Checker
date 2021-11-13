import math
import re
import sys
from collections import Counter
if len(sys.argv) < 2:
    print("You must specify a file name.")
    sys.exit(-1)
file1 = sys.argv[1]
file2 = sys.argv[2]


WORD = re.compile(r'\w+')
text1 = open(file1, 'r').read()
x = Counter(WORD.findall(text1))
text2 = open(file2, 'r').read()
y = Counter(WORD.findall(text2))

def cosDistance(vector1, vector2):
    intersection = set(vector1.keys()) & set(vector2.keys()) 
    numerator = sum([vector1[x] * vector2[x] for x in intersection])
    sum1 = sum([vector1[x] ** 2 for x in vector1.keys()])
    sum2 = sum([vector2[x] ** 2 for x in vector2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

cosine = cosDistance(x, y)

print("Cosine Distance:\t", round(cosine,10))

