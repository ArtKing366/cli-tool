import argparse

from reader import open_file
from filter import filter_data
from stats import aggregation_data
from writer import write_report


def parser_function():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start")
    parser.add_argument("--end")
    args = parser.parse_args()
    
    return args
    

def main():
    args = parser_function()

    data = open_file()
    filtered = filter_data(data, args.start, args.end)
    total, count, avg = aggregation_data(filtered)

    print(f"Total: {total}")
    print(f"Count: {count}")
    print(f"Average: {avg}")

    write_report(total, count, avg)


if __name__ == "__main__":
    main()
        
        



