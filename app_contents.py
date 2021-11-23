import numpy as np
import pandas as pd
from datetime import datetime

CONFIRMED = "confirmed"
DEATHS = "deaths"
RECOVERED = "recovered"
PLACE = "Place"


def get_first_4(df: pd.DataFrame):
    return df.head().columns[:4]


def make_dt_list(df: pd.DataFrame):
    dt_list = []

    for d_str in df.head().columns[4:]:
        dt = datetime.strptime(d_str, "%m/%d/%y")
        if dt.day == 1:
            new_dt_str = f"{dt.month}/{dt.day}/{str(dt.year)[2:]}"
            dt_list.append(new_dt_str)
    return dt_list


dt_list_1 = []
dt_list_2 = []
dt_list_3 = []


dt_list_1 = [np.array(df[dt]) for dt in dt_list]
data_array = np.vstack(dt_list_1)
new_df1 = pd.DataFrame(
    data_array.T, columns=dt_list
)  # ['Province/State', 'Country/Region', 'Lat', 'Long']

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
count_prov_list2 = [
    f"{c}: {p}".replace(": nan", "") for c, p in zip(countries2, provs2)
]
count_prov_list3 = [
    f"{c}: {p}".replace(": nan", "") for c, p in zip(countries3, provs3)
]


def make_place_list(new_df: pd.DataFrame):
    place_series = pd.Series(count_prov_list, name=PLACE)
    new_df[PLACE] = place_series.copy()
    new_df1 = new_df.set_index(PLACE)
    place_list = list(np.array(new_df1.index))
    return place_list


if __name__ == "__main__":
    url_dict = {
        CONFIRMED: "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv",
        DEATHS: "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv",
        RECOVERED: "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv",
    }

    df_dict = {k: pd.read_csv(v) for k, v in url_dict.items()}
    dt_list_dict = {k: make_dt_list(df) for k, df in df_dict.items()}
    first_4_headings = get_first_4(df_dict[CONFIRMED])

    from pprint import pprint

    pprint(dt_list_dict)
