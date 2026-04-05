from bs4 import BeautifulSoup
import requests
import re

leaderboard_url = "https://wordwall.net/leaderboardajax/addentry"
url_id = input("Enter wordwall url -> ")
id = url_id.split("/")[4]

def get_templateId(url_id):
    response = requests.get(url_id)

    if response.status_code != 200:
        print(f"Request failed with {response.status_code}")

    soup = BeautifulSoup(response.content, "html.parser")
    scripts = soup.find_all("script")

    server_model_script = None
    for script in scripts:
        if script.string and "ServerModel" in script.string:
            server_model_script = script.string
            break

    if not server_model_script:
        print("Could not find the ServerModel script on the page.")

    templateId = re.search(r's\.templateId=Number\((\d+)\)', server_model_script).group(1)
    return templateId

activityId = int(id)
name = input("Enter a bot name -> ")
bot_count = int(input("Enter how many bots do you want (less than 200) -> "))
score = int(input("Enter score -> "))
time_val = int(input("Enter time(s) -> "))
templateId = get_templateId(url_id)

def send_bots(score, time_val, name, activityId, templateId):
    if bot_count <= 200:
        generated_num = 0
        for i in range(bot_count):

            payload = {
                "score": score,
                "time": time_val * 1000,
                "name": f"{name}_{generated_num}",
                "mode": 1,
                "activityId": activityId,
                "templateId": templateId
            }
            generated_num = generated_num + 1
            response = requests.post(leaderboard_url, data=payload)

            if response.status_code == 200:
                print(f"[+] Bot {i+1} submitted successfully")
            else:
                print(f"[-] Bot {i+1} failed with status {response.status_code}")
    else:
        print("Bot count must be 200 or less")

send_bots(score, time_val, name, activityId, templateId)
