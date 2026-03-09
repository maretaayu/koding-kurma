import urllib.request
import json
import os

files = {
    'elephant': 'File:Asian_Elephant_Trumpeting.ogg',
    'lion': 'File:Lion_roar.ogg',
    'monkey': 'File:Howler_monkey_sounds.ogg',
    'cow': 'File:Cow_moo.ogg',
    'tiger': 'File:Tiger_growling.ogg',
    'zebra': 'File:Horse_whinny_2.ogg', # Closest approximation in Commons
    'giraffe': 'File:Chewing.ogg' 
}

def get_wiki_sound(filename):
    url = f"https://en.wikipedia.org/w/api.php?action=query&prop=imageinfo&iiprop=url&format=json&titles={urllib.parse.quote(filename)}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        pages = data['query']['pages']
        for page_id in pages:
            return pages[page_id]['imageinfo'][0]['url']
    except Exception as e:
        print(f"Error for {filename}: {e}")
    return None

os.makedirs('assets/animals', exist_ok=True)
import urllib.parse

for animal, wiki_file in files.items():
    print(f"Fetching {animal}...")
    actual_url = get_wiki_sound(wiki_file)
    if actual_url:
        print(f"Downloading from {actual_url}")
        req = urllib.request.Request(actual_url, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            with urllib.request.urlopen(req) as response, open(f"assets/animals/{animal}.ogg", 'wb') as out_file:
                target_data = response.read()
                out_file.write(target_data)
        except Exception as e:
            print(f"Download error: {e}")
    else:
        print("URL not found!")

