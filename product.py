import requests
import json
import pyttsx3
engine = pyttsx3.init()
 
response = requests.get("https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=bitcoin&x_cg_demo_api_key=CG-MNkvyFrvDnfDySTdM64AUjjp")
print(response.status_code)

data = json.loads(response.text)  
print(f"Bitcoin price in USD: {data['bitcoin']['usd']}")   
engine.say(f"Bitcoin price in USD: {data['bitcoin']['usd']}")
engine.runAndWait()