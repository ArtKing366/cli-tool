import argparse

def parser_function():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start")
    parser.add_argument("--end")
    args = parser.parse_args()
    
    return args
    
args = parser_function()


def open_file():
    with open('data.csv', 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.split("\n")
    
    result = []
    
    for line in lines:
        
        if line == "":
            continue
        
        split_lines = line.split(',')
        
        date = split_lines[0]
        value = split_lines[1]
        
        result.append([date, value])


    return result

data = open_file()

def filter_data(data, start, end):
    filtered = []

    for item in data:
        date = item[0]

        if start <= date <= end:
            filtered.append(item)

    return filtered



filtered = filter_data(data, args.start, args.end)

def aggregation_data(filterd):
    total_value=0
    count_string=0
    for item in filtered:
        value = int(item[1])
        
        total_value += value
        count_string += 1
    
    avg = total_value / count_string
    
    return total_value, count_string, avg 

total, count, avg = aggregation_data(filtered)

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {avg}")
     
def write_report(total, count, avg):
    text = f"Total: {total}\nCount: {count}\nAverage: {avg}"
    with open ("report.txt", "w", encoding="utf-8") as file:
        file.write(text)
        
write_report(total, count, avg)       
        
        



