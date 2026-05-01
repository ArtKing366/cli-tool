def filter_data(data, start, end):
    filtered = []

    for item in data:
        date = item[0]

        if start <= date <= end:
            filtered.append(item)

    return filtered
