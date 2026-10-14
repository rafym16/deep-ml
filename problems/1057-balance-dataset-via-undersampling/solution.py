def balance_undersample(data: list) -> list:
    """
    Undersample the majority classes so all classes have the same number of
    samples equal to the minority class count.

    data: list of (sample, label) tuples
    Returns: list of (sample, label) tuples, order-preserving
    """
    if not data:
        return []
    from collections import Counter
    
    counts = Counter(label for _, label in data)
    min_count = min(counts.values())

    kept = Counter()
    result = []

    for sample, label in data:
        if kept[label] < min_count:
            result.append((sample, label))
            kept[label] += 1

    return result
    
