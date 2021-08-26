import requests

r = requests.get("https://www.worldweatheronline.com/aizawl-weather/mizoram/in.aspx")

page_html_str = r.text

print(page_html_str[6606-50: 6606+50])


