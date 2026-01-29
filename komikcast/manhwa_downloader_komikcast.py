import requests
from bs4 import BeautifulSoup
import os
import re
import time
from urllib.parse import urljoin, urlparse

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

IMAGE_EXT = (".jpg", ".jpeg", ".png", ".webp")

def clean_name(name):
    return re.sub(r'[\\/:*?"<>|]', '', name).strip()

def extract_chapter_number(url):
    m = re.search(r'chapter[-\s]?([\d.]+)', url.lower())
    return m.group(1) if m else "unknown"

def is_valid_image(src):
    src = src.lower()
    if not src.endswith(IMAGE_EXT):
        return False
    if any(x in src for x in [
        "avatar", "logo", "ads", "banner",
        "icon", "emoji", "comment"
    ]):
        return False
    return True

def get_series_title(chapter_url):
    r = requests.get(chapter_url, headers=HEADERS, timeout=20)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    title_tag = soup.select_one("h1")
    if title_tag:
        return clean_name(title_tag.get_text())

    return "Unknown Series"

def get_images(chapter_url):
    r = requests.get(chapter_url, headers=HEADERS, timeout=20)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")

    images = []
    for img in soup.find_all("img"):
        src = img.get("data-src") or img.get("data-lazy-src") or img.get("src")
        if not src:
            continue
        if not is_valid_image(src):
            continue
        images.append(urljoin(chapter_url, src))

    return list(dict.fromkeys(images))

def download_image(url, path):
    r = requests.get(url, headers=HEADERS, stream=True, timeout=30)
    r.raise_for_status()
    with open(path, "wb") as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)

def download_chapter(chapter_url, base_dir, series_name):
    ch_num = extract_chapter_number(chapter_url)
    chapter_dir = os.path.join(base_dir, series_name, f"Chapter {ch_num.zfill(2)}")
    os.makedirs(chapter_dir, exist_ok=True)

    print(f"\nDownloading {series_name} - Chapter {ch_num}")

    images = get_images(chapter_url)
    if not images:
        print("No images found")
        return

    for i, img_url in enumerate(images, 1):
        ext = os.path.splitext(urlparse(img_url).path)[1] or ".jpg"
        filename = f"{i:03d}{ext}"
        filepath = os.path.join(chapter_dir, filename)

        if os.path.exists(filepath):
            continue

        try:
            download_image(img_url, filepath)
            print(f"Saved {filename}")
            time.sleep(0.2)
        except Exception as e:
            print(f"Failed {img_url}: {e}")

def main():
    import sys

    if len(sys.argv) != 2:
        print("Usage: python downloader_komikcast.py chapters.txt")
        return

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        chapters = [x.strip() for x in f if x.strip()]

    if not chapters:
        print("chapters.txt kosong")
        return

    os.makedirs("downloads", exist_ok=True)

    series_name = get_series_title(chapters[0])

    for ch in chapters:
        download_chapter(ch, "downloads", series_name)

if __name__ == "__main__":
    main()
