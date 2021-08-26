import requests

r = requests.get("https://www.worldweatheronline.com/aizawl-weather/mizoram/in.aspx")

page_html_str = r.text

inx = page_html_str.index("Aizawl Weather Now")
inx_date = page_html_str.index("Time in Aizawl is")
#print(page_html_str[inx_date + 26 : inx_date + 32])
date = page_html_str[inx_date + 26 : inx_date + 32] + " " + page_html_str[inx_date + 46 : inx_date + 57]
print(f"\nDate: {date}")
print("\nThe Temperature in Aizawl: ")
temp_celcius = page_html_str[inx+ 427: inx+430]
print(f"In Celcius : {temp_celcius}°C")
temp_farenheit = (float(temp_celcius) * (9/5)) + 32
print(f"In Farenheit : {temp_farenheit}°F")


