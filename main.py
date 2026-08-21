import datetime

print("Toffee Auto Update Script Started...")

# এখানে আপনার কুকি ফেচ করার বা আপডেট করার মূল কোড বসবে
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Last updated at: {current_time}")

# উদাহরণস্বরূপ: একটি ডামি ফাইল আপডেট বা তৈরি করার কোড
with open("playlist.m3u", "w") as f:
    f.write(f"#EXTM3U\n# Updated at: {current_time}\n# यहाँ আপনার টফির লিংক বা কুকি থাকবে")

print("Playlist updated successfully!")
