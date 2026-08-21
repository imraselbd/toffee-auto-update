import datetime
import json

print("Toffee JSON Generator Started...")

try:
    # ==========================================
    # COOKIE
    # ==========================================
    cookie_value = 'Edge-Cache-Cookie=YOUR_REAL_COOKIE_HERE'

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    channels_list = [
        # আপনার 80টি channel এখানে থাকবে
    ]

    # ==========================================
    # SET COOKIE TO EVERY CHANNEL
    # ==========================================
    for channel in channels_list:
        if "headers" not in channel:
            channel["headers"] = {}

        channel["headers"]["cookie"] = cookie_value

    # ==========================================
    # CREATE JSON
    # ==========================================
    final_output = {
        "status": "success",
        "name": "Toffee Live Channels",
        "owner": "OTT-KING",
        "channels_amount": len(channels_list),
        "Last_update": current_time,
        "response": channels_list
    }

    with open("toffee.json", "w", encoding="utf-8") as f:
        json.dump(
            final_output,
            f,
            indent=4,
            ensure_ascii=False
        )

    print("toffee.json successfully generated and updated!")
    print("Total channels:", len(channels_list))

except Exception as e:

    error_output = {
        "status": "error",
        "message": str(e),
        "name": "Toffee Live Channels",
        "owner": "OTT-KING",
        "channels_amount": 0,
        "Last_update": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "response": []
    }

    with open("toffee.json", "w", encoding="utf-8") as f:
        json.dump(
            error_output,
            f,
            indent=4,
            ensure_ascii=False
        )

    print("Error:", e)
