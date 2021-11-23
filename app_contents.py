import numpy as np
import pandas as pd
from datetime import datetime




df = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
df2 = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")
df3 = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv")


first_4_headings = df.head().columns[:4]


dt_list = []
dt_list2 = []
dt_list3 = []


for d_str in df.head().columns[4:]:
    dt = datetime.strptime(d_str, "%m/%d/%y")
    if dt.day == 1:
        new_dt_str = f"{dt.month}/{dt.day}/{str(dt.year)[2:]}"
        dt_list.append(new_dt_str)

for d_str in df2.head().columns[4:]:
    dt = datetime.strptime(d_str, "%m/%d/%y")
    if dt.day == 1:
        new_dt_str2 = f"{dt.month}/{dt.day}/{str(dt.year)[2:]}"
        dt_list2.append(new_dt_str2)

for d_str in df3.head().columns[4:]:
    dt = datetime.strptime(d_str, "%m/%d/%y")
    if dt.day == 1:
        new_dt_str3 = f"{dt.month}/{dt.day}/{str(dt.year)[2:]}"
        dt_list3.append(new_dt_str3)       


dt_list_1 = []
dt_list_2 = []
dt_list_3 = []


dt_list_1 = [np.array(df[dt]) for dt in dt_list]
data_array = np.vstack(dt_list_1)
new_df1 = pd.DataFrame(data_array.T, columns=dt_list)                   # ['Province/State', 'Country/Region', 'Lat', 'Long']

dt_list_2 = [np.array(df2[dt]) for dt in dt_list2]
data_array2 = np.vstack(dt_list_2)
new_df2 = pd.DataFrame(data_array2.T, columns=dt_list2) 

dt_list_3 = [np.array(df3[dt]) for dt in dt_list3]
data_array3 = np.vstack(dt_list_3)
new_df3 = pd.DataFrame(data_array3.T, columns=dt_list3) 


countries = list(np.array(df[first_4_headings[1]]))
provs = list(np.array(df[first_4_headings[0]]))

countries2 = list(np.array(df2[first_4_headings[1]]))
provs2 = list(np.array(df2[first_4_headings[0]]))

countries3 = list(np.array(df3[first_4_headings[1]]))
provs3 = list(np.array(df3[first_4_headings[0]]))


count_prov_list = [f"{c}: {p}".replace(": nan", "") for c, p in zip(countries, provs)]
count_prov_list2 = [f"{c}: {p}".replace(": nan", "") for c, p in zip(countries2, provs2)]
count_prov_list3 = [f"{c}: {p}".replace(": nan", "") for c, p in zip(countries3, provs3)]


PLACE = "Place"


place_series = pd.Series(count_prov_list, name=PLACE)
place_series2 = pd.Series(count_prov_list2, name=PLACE)
place_series3 = pd.Series(count_prov_list3, name=PLACE)


col_inx = 1
col_name = first_4_headings[1]


new_df1[PLACE] = place_series.copy()
new_df2[PLACE] = place_series2.copy()
new_df3[PLACE] = place_series3.copy()


new_df1 = new_df1.set_index(PLACE)
new_df2 = new_df2.set_index(PLACE)
new_df3 = new_df3.set_index(PLACE)


place_list = list(np.array(new_df1.index))
place_list2 = list(np.array(new_df2.index))
place_list3 = list(np.array(new_df3.index))

