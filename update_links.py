import requests
import re

# لینکی سەرچاوە
source_url = "https://karwan.tv/ava-sport"

# ناساندنی سکریپتەکە وەک وێبگەڕێکی ئاسایی
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

try:
    # ناردنی داواکاری بۆ سایتەکە
    response = requests.get(source_url, headers=headers)
    
    # گەڕان بەدوای لینکی m3u8 کە تۆکنی پێوەیە
    match = re.search(r'(https?://[^\s<>"]+\.m3u8\?token=[^\s<>"]+)', response.text)
    
    if match:
        new_link = match.group(1)
        # دروستکردنی فایلی m3u
        with open("ava_sport.m3u", "w") as f:
            f.write("#EXTM3U\n")
            f.write("#EXTINF:-1,AVA Sport\n")
            f.write(new_link)
        print("Update successful! Link found.")
    else:
        print("Token not found. The site structure might have changed.")
        
except Exception as e:
    print(f"Error: {e}")


