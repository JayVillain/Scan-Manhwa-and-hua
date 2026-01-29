import requests
from bs4 import BeautifulSoup
import argparse
import re
from urllib.parse import urljoin

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def extract_chapter_number(text):
    match = re.search(r'chapter\s*([\d.]+)', text.lower())
    if match:
        try:
            return float(match.group(1))
        except ValueError:
            return None
    return None

def scan_series(url):
    print(f"Scanning series page: {url}")
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")

    chapter_links = soup.select("ul#chapter-wrapper a.chapter-link-item")

    if not chapter_links:
        print("No chapters found. Pastikan ini halaman series Komikcast.")
        return []

    chapters = []

    for a in chapter_links:
        href = a.get("href")
        title = a.get_text(strip=True)

        if not href:
            continue

        full_url = urljoin(url, href)
        ch_num = extract_chapter_number(title)

        chapters.append({
            "number": ch_num,
            "title": title,
            "url": full_url
        })

    chapters = [c for c in chapters if c["number"] is not None]
    chapters.sort(key=lambda x: x["number"])

    return chapters

def filter_chapters(chapters, args):
    if args.only is not None:
        return [c for c in chapters if c["number"] == args.only]

    if args.latest is not None:
        return chapters[-args.latest:]

    if args.from_ch is not None or args.to is not None:
        result = []
        for c in chapters:
            if args.from_ch is not None and c["number"] < args.from_ch:
                continue
            if args.to is not None and c["number"] > args.to:
                continue
            result.append(c)
        return result

    return chapters

def save_output(chapters, filename="chapters.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for c in chapters:
            f.write(c["url"] + "\n")
    print(f"Saved {len(chapters)} chapters to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Komikcast Series Scanner")
    parser.add_argument("url", help="URL series Komikcast")
    parser.add_argument("--from", dest="from_ch", type=float, help="Chapter mulai")
    parser.add_argument("--to", type=float, help="Chapter akhir")
    parser.add_argument("--only", type=float, help="Hanya satu chapter")
    parser.add_argument("--latest", type=int, help="Ambil N chapter terbaru")

    args = parser.parse_args()

    chapters = scan_series(args.url)
    if not chapters:
        return

    chapters = filter_chapters(chapters, args)
    save_output(chapters)

if __name__ == "__main__":
    main()
