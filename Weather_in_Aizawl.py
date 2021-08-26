import requests

r = requests.get("https://www.worldweatheronline.com/aizawl-weather/mizoram/in.aspx")

page_html_str = r.text

inx = page_html_str.index("Aizawl Weather Now")
temperature = page_html_str[inx+ 427: inx+430]
print(f"The Temperature in Aizawl is : {temperature}°C")


