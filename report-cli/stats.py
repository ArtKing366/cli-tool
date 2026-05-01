def aggregation_data(filtered):
    total_value = 0
    count_string = 0

    for item in filtered:
        value = int(item[1])
        total_value += value
        count_string += 1

    avg = total_value / count_string if count_string else 0
    return total_value, count_string, avg
