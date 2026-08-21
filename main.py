import os
import datetime

print("Toffee Playlist Generator Started...")

# গিটহাব সিক্রেট থেকে কুকি রিড করা
cookie_value = os.environ.get("TOFFEE_COOKIE", "")

if not cookie_value:
    print("Error: Toffee Cookie not found in Secrets!")
    exit(1)

# বর্তমান সময় বা ডেট বের করা
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# একটি সাধারণ প্লেলিস্ট ফাইল (m3u) ফরম্যাট তৈরি করা যেখানে আপনার কুকি যুক্ত থাকবে
playlist_content = f"""#EXTM3U
#EXT-X-VERSION:3
#EXTINF:-1 tvg-id="Toffee" tvg-name="Toffee Live" tvg-logo="" group-title="Toffee",Toffee Live Stream
#EXTVLCOPT:http-user-agent=Mozilla/5.0
#EXT-X-SESSION-DATA:DATA-ID="Cookie",{cookie_value}
# Updated at: {current_time}
https://toffeelive.com/en/watch/o3v235oBcqxnFHJBkAdC
"""

# playlist.m3u ফাইলে এই লেখাগুলো সেভ করা
with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(playlist_content)

print("playlist.m3u successfully generated and updated!")
