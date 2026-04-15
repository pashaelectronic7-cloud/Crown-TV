import requests
import re

# لینکی لاپەڕەی کەناڵەکە
source_url = "https://karwan.tv/ava-sport"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://karwan.tv/"
}

try:
    response = requests.get(source_url, headers=headers, timeout=15)
    # لێرەدا دەگەڕێین بەدوای هەر لینکێک کە کۆتاییەکەی .m3u8 بێت یان وشەی 'token'ی تێدا بێت
    # ئەم شێوازە هەموو جۆرە لینکێکی ڤیدیۆیی دەگرێتەوە
    links = re.findall(r'["\'](https?://[^"\']+\.m3u8[^"\']*)["\']', response.text)
    
    # ئەگەر لەناو کۆدی سەرەکیدا نەبوو، دەگەڕێین بەدوای ئەو سێرڤەرانەی کە 'ava'یان تێدایە
    if not links:
        links = re.findall(r'["\'](https?://[^"\']+ava[^"\']+\.m3u8[^"\']*)["\']', response.text, re.IGNORECASE)

    with open("ava_sport.m3u", "w") as f:
        f.write("#EXTM3U\n")
        if links:
            # پاککردنەوەی لینکەکە لە هەر نووسینێکی زیادە
            final_link = links[0].replace('\\', '')
            f.write("#EXTINF:-1,AVA Sport Live\n")
            f.write(final_link)
            print(f"Success! Found: {final_link}")
        else:
            f.write("# No direct stream link found in the page code")
            print("No links found.")

except Exception as e:
    with open("ava_sport.m3u", "w") as f:
        f.write(f"# Error: {str(e)}")
