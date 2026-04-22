# URL Checker

Simple CLI tool to check URLs and IP targets.

## Features

- Check targets from command line
- Load targets from file
- Multi-threaded requests
- Retries on failed requests
- Delay between retries
- Filter only 200 responses (`--only-200`)
- Save results to file

---

## Installation

Clone the repository and install:

```bash
pip install -e .
```

## Usage

Check targets from command line:
```bash
url-checker https://google.com https://example.com
```
Check targets from file:
```bash
url-checker --input ips.txt
```
Save results to file:
```bash
url-checker --input ips.txt --output result.txt
```
Show only successful responses:
```bash
url-checker --input ips.txt --only-200
```
Custom threads, retries and delay:
```bash
url-checker --input ips.txt --threads 5 --retries 2 --delay 1
```

## Arguments

--input, -i — read targets from file
--output, -o — save results to file
--timeout — request timeout (default: 5)
--threads — number of worker threads (1–50)
--retries — number of retries after failure
--delay — delay between retries (seconds)
--only-200 — show only HTTP 200 responses


## Output

```bash
https://google.com → 200 | 81603 bytes [OK]
https://example.com → 200 | 528 bytes [OK]
http://1.1.1.1 → 404 | 1285 bytes [CLIENT]
https://badsite.example → ERROR (ConnectionError: ...)

```

## Notes

Targets without http:// or https:// may return an error
Large number of threads may affect system/network performance
