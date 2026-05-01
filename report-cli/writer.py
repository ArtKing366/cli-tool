def write_report(total, count, avg, output):
    text = f"Total: {total}\nCount: {count}\nAverage: {avg}"
    with open(output, "w", encoding="utf-8") as file:
        file.write(text)

