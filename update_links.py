import requests
import re

source_url = "https://karwan.tv/ava-sport"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

try:
    response = requests.get(source_url, headers=headers, timeout=10)
    # گەڕان بەدوای لینکی m3u8
    match = re.search(r'(https?://[^\s<>"]+\.m3u8[^\s<>"]*)', response.text)
    
    with open("ava_sport.m3u", "w") as f:
        f.write("#EXTM3U\n")
        if match:
            new_link = match.group(1)
            f.write("#EXTINF:-1,AVA Sport\n")
            f.write(new_link)
            print("Success: Link updated.")
        else:
            f.write("# No Link Found Today")
            print("Warning: No link found in the page.")
            
except Exception as e:
    with open("ava_sport.m3u", "w") as f:
        f.write(f"# Error occurred: {str(e)}")
    print(f"Error: {e}")
