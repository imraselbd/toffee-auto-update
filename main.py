import os
import datetime
import json

print("Toffee Playlist Generator Started...")

# গিটহাব সিক্রেট থেকে কুকি রিড করা
cookie_value = os.environ.get("TOFFEE_COOKIE", "")

if not cookie_value:
    print("Error: Toffee Cookie not found in Secrets!")
    exit(1)

# বর্তমান সময় বা ডেট বের করা
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# চ্যানেলগুলোর ডাটা (এখানে আপনার কুকি অটো বসবে)
channels_data = [
    {
      "category_name": "News Channel",
      "name": "CNN VIP",
      "link": "https://bldcmprod-cdn.toffeelive.com/cdn/live/cnn/playlist.m3u8",
      "headers": {
        "Host": "bldcmprod-cdn.toffeelive.com",
        "cookie": cookie_value,
        "user-agent": "okhttp/4.11.0",
        "client-api-header": "angM1aXCHQLmmSW6cDlpXMD6tLdwnhMoUeaBBFKmd98bX6Vrae5xCMbm4gg0+u33rnxeGQDZNr2GD1tW0cWwKEpWimNlGqXVQGhpiIBz1JFxN+OxXcQqaMPrjwUhCyI5mO1DGyNv18+Z2EpmHtVnLzV9SrGsQWu4oRKjxE8QIMsRs6LrvL6hWGPlOGQke/qb5QxQZNetPzI39jHhX7Zi2XrCMIT4a+gk2Wu1c3wIybwkqknPcTp4Bj1cEF3Q+q1dV05SBhzpEDfoR2BLyQ6dV3LvmY6MNKxbUjby7hMsg35lFl2Df2mZsr7C27309w/qWi8lLXDjB7B1MozIGKn8rw3bXY5YlrPKBKztyiisAjQQi7kc5ISXyGSwRmhciwkciuitsSL0LlqHY7/Qkkh71EtaK3XEgVpLdH8zRCsTwfu1iIVPiDwTycuuBy4XWkcNnd0iLB35yftQpiL8HfpO2jQnrAwzePxszJ7mewVG+M0P/qyTBD52NkPR8uW0AZmDKp5LHTCGf7sqldDzpZvU+gsSdvtsBUcmHzjINGEoyXk=",
        "accept-encoding": "gzip",
        "custom-header-key": "custom_value_here"
      },
      "logo": "https://images.toffeelive.com/images/program/333/logo/240x240/mobile_logo_146607001735536058.png",
      "custom_status": "Active"
    },
    {
      "category_name": "News Channel",
      "name": "Somoy TV",
      "link": "https://bldcmprod-cdn.toffeelive.com/cdn/live/somoy_tv/playlist.m3u8",
      "headers": {
        "Host": "bldcmprod-cdn.toffeelive.com",
        "cookie": cookie_value,
        "user-agent": "okhttp/4.11.0",
        "client-api-header": "angM1aXCHQLmmSW6cDlpXMD6tLdwnhMoUeaBBFKmd98bX6Vrae5xCMbm4gg0+u33rnxeGQDZNr2GD1tW0cWwKEpWimNlGqXVQGhpiIBz1JFxN+OxXcQqaMPrjwUhCyI5mO1DGyNv18+Z2EpmHtVnLzV9SrGsQWu4oRKjxE8QIMsRs6LrvL6hWGPlOGQke/qb5QxQZNetPzI39jHhX7Zi2XrCMIT4a+gk2Wu1c3wIybwkqknPcTp4Bj1cEF3Q+q1dV05SBhzpEDfoR2BLyQ6dV3LvmY6MNKxbUjby7hMsg35lFl2Df2mZsr7C27309w/qWi8lLXDjB7B1MozIGKn8rw3bXY5YlrPKBKztyiisAjQQi7kc5ISXyGSwRmhciwkciuitsSL0LlqHY7/Qkkh71EtaK3XEgVpLdH8zRCsTwfu1iIVPiDwTycuuBy4XWkcNnd0iLB35yftQpiL8HfpO2jQnrAwzePxszJ7mewVG+M0P/qyTBD52NkPR8uW0AZmDKp5LHTCGf7sqldDzpZvU+gsSdvtsBUcmHzjINGEoyXk=",
        "accept-encoding": "gzip",
        "custom-header-key": "custom_value_here"
      },
      "logo": "https://assets-prod.services.toffeelive.com//Xi_Ga5oBNnOkwJLWkhKP/posters/ef2899d5-1ae0-4fee-aee5-45f9b0b3ba80.png",
      "custom_status": "Active"
    },
    {
      "category_name": "News Channel",
      "name": "Independent TV",
      "link": "https://bldcmprod-cdn.toffeelive.com/cdn/live/independent_tv/playlist.m3u8",
      "headers": {
        "Host": "bldcmprod-cdn.toffeelive.com",
        "cookie": cookie_value,
        "user-agent": "okhttp/4.11.0",
        "client-api-header": "angM1aXCHQLmmSW6cDlpXMD6tLdwnhMoUeaBBFKmd98bX6Vrae5xCMbm4gg0+u33rnxeGQDZNr2GD1tW0cWwKEpWimNlGqXVQGhpiIBz1JFxN+OxXcQqaMPrjwUhCyI5mO1DGyNv18+Z2EpmHtVnLzV9SrGsQWu4oRKjxE8QIMsRs6LrvL6hWGPlOGQke/qb5QxQZNetPzI39jHhX7Zi2XrCMIT4a+gk2Wu1c3wIybwkqknPcTp4Bj1cEF3Q+q1dV05SBhzpEDfoR2BLyQ6dV3LvmY6MNKxbUjby7hMsg35lFl2Df2mZsr7C27309w/qWi8lLXDjB7B1MozIGKn8rw3bXY5YlrPKBKztyiisAjQQi7kc5ISXyGSwRmhciwkciuitsSL0LlqHY7/Qkkh71EtaK3XEgVpLdH8zRCsTwfu1iIVPiDwTycuuBy4XWkcNnd0iLB35yftQpiL8HfpO2jQnrAwzePxszJ7mewVG+M0P/qyTBD52NkPR8uW0AZmDKp5LHTCGf7sqldDzpZvU+gsSdvtsBUcmHzjINGEoyXk=",
        "accept-encoding": "gzip",
        "custom-header-key": "custom_value_here"
      },
      "logo": "https://assets-prod.services.toffeelive.com/w_480,q_75,f_webp/ES_cZZsBNnOkwJLW1Oz1/posters/b872b8f5-cb6b-45a1-a1cd-7609df51d614.png",
      "custom_status": "Active"
    }
]

# চাইলে আপনি এই ডাটাগুলো একটি JSON ফাইল হিসেবেও সেভ করতে পারেন, 
# অথবা m3u ফাইল বানাতে পারেন। নিচের কোড দিয়ে m3u ফাইল তৈরি হবে:

m3u_content = "#EXTM3U\n"
for ch in channels_data:
    m3u_content += f'#EXTINF:-1 tvg-logo="{ch["logo"]}" group-title="{ch["category_name"]}",{ch["name"]}\n'
    m3u_content += f'#EXTVLCOPT:http-user-agent={ch["headers"]["user-agent"]}\n'
    m3u_content += f'{ch["link"]}\n'

# ফাইল সেভ করা
with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_content)

print("playlist.m3u successfully generated and updated!")
