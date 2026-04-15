import requests

# لیستی کەناڵەکان و لینکەکانیان
channels = {
    "AVA_TV": "https://ava3.store/upload/ava.m3u8",
    "beIN_Sports_1": "https://3syrialive.s3.us-east-2.amazonaws.com/bein1/master.m3u8"
}

try:
    with open("all_channels.m3u", "w") as f:
        f.write("#EXTM3U\n")
        for name, url in channels.items():
            f.write(f"#EXTINF:-1,{name}\n")
            f.write(f"{url}\n")
    print("تەواو! لینکەکان نوێ کرانەوە")
except Exception as e:
    print(f"Error: {e}")
