import urllib.request
import urllib.parse
import json

base_url = "https://commons.wikimedia.org/w/api.php?action=query&prop=videoinfo&iiprop=url&format=json&titles="

files = {
    'elephant': 'File:Asian_Elephant_Trumpeting.ogg',
    'lion': 'File:Lion_roar.ogg',
    'monkey': 'File:Chimpanzee_vocalization.ogg',
    'cow': 'File:Cow_moo.ogg',
    'tiger': 'File:Tiger_growling.ogg',
    'zebra': 'File:Horse_whinny_2.ogg',
    'giraffe': 'File:Chewing.ogg' 
}

for animal, fname in files.items():
    url = base_url + urllib.parse.quote(fname)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        pages = data['query']['pages']
        for page_id in pages:
            if 'videoinfo' in pages[page_id]:
                dl_url = pages[page_id]['videoinfo'][0]['url']
                print(f"Downloading {animal} from {dl_url}")
                urllib.request.urlretrieve(dl_url, f"assets/animals/{animal}.ogg")
            else:
                image_url = "https://commons.wikimedia.org/w/api.php?action=query&prop=imageinfo&iiprop=url&format=json&titles="
                u2 = image_url + urllib.parse.quote(fname)
                req2 = urllib.request.Request(u2, headers={'User-Agent': 'Mozilla/5.0'})
                r2 = urllib.request.urlopen(req2)
                d2 = json.loads(r2.read())
                p2 = d2['query']['pages']
                for pid2 in p2:
                    if 'imageinfo' in p2[pid2]:
                        dl2 = p2[pid2]['imageinfo'][0]['url']
                        print(f"Downloading {animal} from {dl2}")
                        urllib.request.urlretrieve(dl2, f"assets/animals/{animal}.ogg")
                    else:
                        print(f"URL missing for {animal} entirely")
    except Exception as e:
        print(f"Exception for {animal}: {e}")
