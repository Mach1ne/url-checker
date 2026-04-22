import requests
import time
from concurrent.futures import ThreadPoolExecutor

def fetch_url(data):
    url, timeout, retries, delay = data
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    for attempt in range(retries + 1):
        try:
            response = requests.get(url, timeout=timeout, headers=headers)
            status = response.status_code
            length = len(response.content)
            return (url, status, length)
        except Exception as e:
            if attempt == retries:
                return (url, "ERROR", f"{type(e).__name__}: {e}")
            time.sleep(delay)

def show_usage():
    print("Usage:")
    print("  python main.py --input ips.txt")
    print("  python main.py https://google.com 8.8.8.8")
    print()
    
def read_file(filename):
    targets = []

    with open(filename, "r") as file:
        for line in file:
            ip = line.strip()
            if ip:
                targets.append(ip)

    return targets

def check_url(urls, timeout, threads, retries, delay):
    urls_with_timeout = [(url, timeout, retries, delay) for url in urls]
    
    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = executor.map(fetch_url, urls_with_timeout)

    return list(results)


def build_report(urls, timeout, only_200, threads, retries, delay):
    result = check_url(urls, timeout, threads, retries, delay)
    lines = ["Результаты проверки:"]

    for url, status, info in result:
        if only_200 and status != 200:
            continue

        if status == "ERROR":
            lines.append(f"{url} → ERROR ({info})")

        elif 200 <= status < 300:
            lines.append(f"{url} → {status} | {info} bytes [OK]")

        elif 300 <= status < 400:
            lines.append(f"{url} → {status} | {info} bytes [REDIRECT]")

        elif 400 <= status < 500:
            lines.append(f"{url} → {status} | {info} bytes [CLIENT]")

        else:
            lines.append(f"{url} → {status} | {info} bytes [SERVER]")

    lines.append("")
    lines.append(f"Проверено: {len(result)} URL")

    return "\n".join(lines)