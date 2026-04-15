import requests

# ئەو لینکەی کە بۆت ناردم
source_url = "https://ava3.store/upload/ava.m3u8"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

try:
    # لێرەدا پشکنین دەکەین بزانین لینکەکە کار دەکات
    response = requests.get(source_url, headers=headers, timeout=10)
    
    with open("ava_sport.m3u", "w") as f:
        f.write("#EXTM3U\n")
        # ئەگەر سایتەکە وەڵامی دایەوە (Status 200)، لینکەکە دادەنێین
        if response.status_code == 200:
            f.write("#EXTINF:-1,AVA Sport Live\n")
            f.write(source_url)
            print("Success: Link added to playlist.")
        else:
            f.write("# Link is currently offline")
            print("Link is not active at the moment.")

except Exception as e:
    with open("ava_sport.m3u", "w") as f:
        f.write(f"# Error: {str(e)}")
    print(f"Error: {e}")
