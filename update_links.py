import requests
import re

# لینکی پەخشی ڕاستەوخۆ
source_url = "https://karwan.tv/ava-sport"

# ناساندنی سکریپتەکە وەک وێبگەڕێکی مۆدێرن
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://karwan.tv/",
    "Accept-Language": "en-US,en;q=0.9"
}

try:
    # داواکردنی ناوەڕۆکی سایتەکە
    response = requests.get(source_url, headers=headers, timeout=15)
    
    # گەڕان بەدوای هەر لینکێکی m3u8 (بە تۆکن یان بێ تۆکن)
    # لێرەدا شێوازی گەڕانەکەمان فراوانتر کردووە
    links = re.findall(r'(https?://[^\s<>"]+\.m3u8[^\s<>"]*)', response.text)
    
    with open("ava_sport.m3u", "w") as f:
        f.write("#EXTM3U\n")
        if links:
            # یەکەم لینک کە دەیدۆزێتەوە دایدەنێت
            final_link = links[0].replace('\\', '') # لادانی نیشانەی زیادە ئەگەر هەبێت
            f.write("#EXTINF:-1,AVA Sport Live\n")
            f.write(final_link)
            print(f"Success! Link found: {final_link}")
        else:
            f.write("# No Link Found - Site structure might have changed")
            print("Could not find any m3u8 link.")
            
except Exception as e:
    with open("ava_sport.m3u", "w") as f:
        f.write(f"# Error: {str(e)}")
    print(f"Error occurred: {e}")
