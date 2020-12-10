#!/usr/local/bin/python3.8

import mapreduce


class WordCount(mapreduce):

    def mapper(self, _, line):
        for word in line.split(" "):
            # print ((word, 1))
            yield word, 1

    def combiner(self, key, values):
        yield key, sum(values)

    def reducer(self, key, values):
        # print( key, sum(values))
        yield key, sum(values)


input = [
    "hello",
    "this class is very interesting",
    "this is an example of word count"
]

with open("alice.txt", "r") as f:
    line = f.readlines()
print(len(line))

exit()

# output = WordCount().run(input)
# for k, v in output:
#     print(k, "--> ", v)
