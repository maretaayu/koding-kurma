import urllib.request
import urllib.parse
import json
import re

animals = ['elephant', 'lion', 'monkey', 'cow', 'tiger', 'zebra', 'giraffe']

for animal in animals:
    url = f"https://freesound.org/search/?q={animal}+roar+or+{animal}+sound"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        # Look for data-mp3="https://cdn.freesound.org/previews/...
        match = re.search(r'data-mp3="([^"]+\.mp3)"', html)
        if match:
            mp3_url = match.group(1)
            print(f"Downloading {animal} from {mp3_url}")
            urllib.request.urlretrieve(mp3_url, f"assets/animals/{animal}.mp3")
        else:
            print(f"No match for {animal}")
    except Exception as e:
        print(f"Failed {animal}: {e}")
