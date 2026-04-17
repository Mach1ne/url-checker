# Simple URL Checker

Basic Python CLI tool for checking URLs.

## Features
- Check HTTP status codes
- Show response size
- Handle errors (timeout, connection issues)
- Filter only 200 responses (`--only-200`)
- Save output to file

## Install

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py https://api.github.com https://google.com
```

## Options

```bash
--only-200        Show only 200 responses
--timeout 5       Set request timeout (default: 5)
-o result.txt     Save output to file
```

## Examples

```bash
python main.py https://api.github.com
python main.py https://api.github.com --only-200
python main.py https://api.github.com -o result.txt
```

## Example Output

```text
Результаты проверки:
https://api.github.com → 200 | 2396 bytes [OK]
https://api.github.com/admin → 403 | 120 bytes [CLIENT]
https://badsite.example → ERROR (Connection error)

Проверено: 3 URL
```