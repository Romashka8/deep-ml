def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    counts = {}

    for i in samples:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    res = []
    total = sum(counts.values())

    for value, count in counts.items():
        res.append((value, count / total))
    
    return res