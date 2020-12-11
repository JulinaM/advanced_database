#!/usr/local/bin/python3.8
import operator
from collections import Counter

from mapreduce import MapReduce


class WordCount(MapReduce):

    def mapper(self, _, line):
        for word in line.split(" "):
            yield (word.strip(), 1)

    def combiner(self, key, values):
        yield key, sum(values)

    def reducer(self, key, values):
        yield key, sum(values)


# input = [
#     "this is an example of this line",
#     "this is an example of some example text",
#     "this is another example",
#     "and this is some more text and text and text"
#     ]

with open("alice.txt", "r") as f:
    input = f.readlines()

print(len(input))
print(input[1000:1010])
# exit()


output = WordCount().run(input)

max_key = ""
max_value = 0

for key, value in output:
    # print(key, " -- ", value)
    if value > max_value:
        max_key = key
        max_value = value

print("Most common word is : \"", max_key, "\" with count = ", max_value)


sorted_output = Counter(dict(sorted(output, key=lambda item: item[1])))
print("\nTop 10 most common words are :")
for k, v in sorted_output.most_common(10):
    print('%s: %i' % (k, v))

sorted_i = Counter(dict(sorted(output, key=operator.itemgetter(1))[:10], reverse=True))
print("\nTop 10 most common words are :")
for k, v in sorted_i.most_common(10):
    print('%s: %i' % (k, v))



