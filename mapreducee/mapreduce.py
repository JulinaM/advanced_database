def mapper(s):
    pairs = []
    for c in s:
        pairs.append((c, 1))
    return pairs


def combiner(pairs):
    index = {}
    for (k, v) in pairs:
        if k not in index:
            index[k] = 1
        else:
            index[k] = index[k] + v
        pairs = []
    for k in index:
        pairs.append((k, index[k]))
    return pairs


def reducer(pairs):
    output_pairs = []
    for k, v in pairs:
        reduced_val = sum((v, 0))
        output_pairs.append((k, reduced_val))
    return output_pairs


if __name__ == "__main__":
    pairs = mapper("hello")
    print(pairs)
    pairs = combiner(pairs)
    print(pairs)
    pairs = reducer(pairs)
    print(pairs)
