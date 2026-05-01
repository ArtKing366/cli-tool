def write_report(total, count, avg, path="report.txt"):
    text = f"Total: {total}\nCount: {count}\nAverage: {avg}"
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)

