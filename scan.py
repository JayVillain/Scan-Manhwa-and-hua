import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import argparse
import re
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def extract_chapter_number(text):
    match = re.search(r'chapter\s*([\d.]+)', text.lower())
    if match:
        return float(match.group(1))
    return None

def scan_one_page(url):
    response = requests.get(url, headers=HEADERS, timeout=20)
    soup = BeautifulSoup(response.text, "html.parser")

    chapters = []

    for a in soup.find_all("a", href=True):
        href = a["href"]
        text = a.get_text(strip=True)

        if "chapter" not in href.lower() and "chapter" not in text.lower():
            continue

        chapter_number = extract_chapter_number(text + " " + href)
        if chapter_number is None:
            continue

        full_url = urljoin(url, href)
        chapters.append((chapter_number, full_url))

    return list(set(chapters))

def scan_series(series_url, max_pages=50):
    all_chapters = []
    last_count = 0

    for page in range(1, max_pages + 1):
        if page == 1:
            page_url = series_url
        else:
            page_url = f"{series_url}?page={page}"

        print(f"Scanning page {page}: {page_url}")

        found = scan_one_page(page_url)
        if not found:
            break

        all_chapters.extend(found)
        unique_count = len(set(all_chapters))

        if unique_count == last_count:
            break

        last_count = unique_count
        time.sleep(1)

    all_chapters = list(set(all_chapters))
    all_chapters.sort(key=lambda x: x[0])
    return all_chapters

def apply_filter(chapters, args):
    if args.only is not None:
        return [c for c in chapters if c[0] == args.only]

    if args.latest is not None:
        return chapters[-args.latest:]

    start = args.start if args.start is not None else chapters[0][0]
    end = args.end if args.end is not None else chapters[-1][0]

    return [c for c in chapters if start <= c[0] <= end]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="Series URL")
    parser.add_argument("--from", dest="start", type=float)
    parser.add_argument("--to", dest="end", type=float)
    parser.add_argument("--only", type=float)
    parser.add_argument("--latest", type=int)

    args = parser.parse_args()

    chapters = scan_series(args.url)

    if not chapters:
        print("No chapters found")
        return

    filtered = apply_filter(chapters, args)

    with open("chapters.txt", "w", encoding="utf-8") as f:
        for number, url in filtered:
            f.write(url + "\n")
            print(f"Chapter {number}: {url}")

    print(f"Saved {len(filtered)} chapters to chapters.txt")

if __name__ == "__main__":
    main()
