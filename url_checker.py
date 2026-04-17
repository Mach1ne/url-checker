import requests


def check_url(urls, timeout):
    result = []
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    for url in urls:
        try:
            response = requests.get(url, timeout=timeout, headers=headers)
            status = response.status_code
            length = len(response.content)

            result.append((url, status, length))
        except Exception as e:
            result.append((url, "ERROR", str(e)))

    return result


def build_report(urls, timeout, only_200):
    result = check_url(urls, timeout)
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