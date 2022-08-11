"""
Boxy dataset downloader
"""
from pathlib import Path
import urllib.request



BOXY_LINKS_PATH = Path("./data/boxy_links_files")
BOXY_DST_PATH = Path("E:\\boxy")

print(BOXY_LINKS_PATH.resolve())
print(BOXY_LINKS_PATH.exists())

with open(BOXY_LINKS_PATH, "r", encoding="UTF-8") as f:
    links = f.readlines()

for line in links:
    if "http" in line:
        link = line.replace("\n", "")
        filename = link.split("/")[-1]
        print(f"Downloading {filename}")
        urllib.request.urlretrieve(link, BOXY_DST_PATH.joinpath(filename))
