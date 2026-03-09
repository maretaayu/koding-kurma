import urllib.request
import re
import random

animals = ['elephant', 'lion', 'monkey', 'cow', 'tiger', 'zebra', 'giraffe']
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
]

for a in animals:
    url = f"https://html.duckduckgo.com/html/?q={a}+sound+filetype:mp3"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': random.choice(user_agents)})
        html = urllib.request.urlopen(req).read().decode('utf-8')
        links = re.findall(r'href="(https?://[^"]+\.mp3)"', html)
        if links:
            mp3 = links[0]
            print(f"Found {a}: {mp3}")
            urllib.request.urlretrieve(mp3, f"assets/animals/{a}.mp3")
        else:
            print(f"No match for {a}. Searching again with 'roar'...")
            url2 = f"https://html.duckduckgo.com/html/?q={a}+roar+filetype:mp3"
            req2 = urllib.request.Request(url2, headers={'User-Agent': random.choice(user_agents)})
            html2 = urllib.request.urlopen(req2).read().decode('utf-8')
            links2 = re.findall(r'href="(https?://[^"]+\.mp3)"', html2)
            if links2:
                mp3 = links2[0]
                print(f"Found {a}: {mp3}")
                urllib.request.urlretrieve(mp3, f"assets/animals/{a}.mp3")
            else:
                print(f"Still no match for {a}: {url}")
    except Exception as e:
        print(f"Error {a}: {e}")
