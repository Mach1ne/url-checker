import argparse
from url_checker.core import show_usage, build_report, read_file


def main():
    parser = argparse.ArgumentParser(description="Simple URL checker")
    parser.add_argument("--only-200", action="store_true", help="Show only 200 responses")
    parser.add_argument("--timeout", type=int, default=5, help="Timeout")
    parser.add_argument("--threads", type=int, default=10, help="Threads")
    parser.add_argument("--retries", type=int, default=2, help="Retries")
    parser.add_argument("--delay", type=float, default=1, help="Delay between retries")
    parser.add_argument("-i", "--input", help="Provide IP list")
    parser.add_argument("-o", "--output", help="Save in file")  
    parser.add_argument("urls", nargs="*")

    args = parser.parse_args()
    if args.delay < 0:
        print("Delay must be 0 or greater")
        exit(1)
    if args.threads < 1 or args.threads > 50:
        print("Threads must be between 1 and 50")
        exit(1)
    if args.input and args.urls:
        print("Use file or urls, not both\n")
        show_usage()
        exit(1)
    if args.input:
        targets = read_file(args.input)
    elif args.urls:
        targets = args.urls
    else:
        print("No targets provided!\n")
        show_usage()
        exit(1)

    report = build_report(targets, args.timeout, args.only_200, args.threads, args.retries, args.delay)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"Saved to {args.output}")
    else:
        print(report)

if __name__ == "__main__":
    main()




