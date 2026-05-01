def open_file(input):
    with open(input, 'r', encoding='utf-8') as f:
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
