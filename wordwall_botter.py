import requests
import random

url = "https://wordwall.net/leaderboardajax/addentry"
url_id = input("Enter wordwall url -> ")
id = url_id.split("/")[4]

activityId = int(id)
name = input("Enter a bot name -> ")
bot_count = int(input("Enter how many bots do you want (less than 200) -> "))
score = int(input("Enter score -> "))
time_val = int(input("Enter time(s) -> "))

if bot_count <= 200:
    for i in range(bot_count):
        payload = {
            "score": score,
            "time": time_val,
            "name": f"{name}{random.randint(1000, 9999)}",
            "mode": 1,
            "activityId": activityId,
            "templateId": 5
        }

        response = requests.post(url, data=payload)

        if response.status_code == 200:
            print(f"[+] Bot {i+1} submitted successfully")
        else:
            print(f"[-] Bot {i+1} failed with status {response.status_code}")
else:
    print("Bot count must be 200 or less")
