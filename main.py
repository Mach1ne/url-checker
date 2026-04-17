import argparse
from url_checker import build_report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple URL checker")
    parser.add_argument("--only-200", action="store_true", help="Show only 200 responses")
    parser.add_argument("--timeout", type=int, default=5, help="Timeout")
    parser.add_argument("-o", "--output", help="Save in file")
    parser.add_argument("urls", nargs="+")

    args = parser.parse_args()

    report = build_report(args.urls, args.timeout, args.only_200)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"Saved to {args.output}")
    else:
        print(report)