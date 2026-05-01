import argparse

from reader import open_file
from filter import filter_data
from stats import aggregation_data
from writer import write_report


def parser_function():
    parser = argparse.ArgumentParser(
        description="Generate report from CSV data with filtering and statistics"
    )

    parser.add_argument("--start", help="Start date for filtering")
    parser.add_argument("--end", help="End date for filtering")
    parser.add_argument("--input", help="Input CSV file path")
    parser.add_argument("--output", help="Output report file path")
    args = parser.parse_args()
    
    return args
    

def main():
    args = parser_function()

    data = open_file(args.input)
    filtered = filter_data(data, args.start, args.end)
    total, count, avg = aggregation_data(filtered)

    print(f"Total: {total}")
    print(f"Count: {count}")
    print(f"Average: {avg}")

    write_report(total, count, avg,args.output)


if __name__ == "__main__":
    main()
        
        



