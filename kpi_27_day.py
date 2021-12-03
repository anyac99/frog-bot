from ftplib import FTP
import pandas as pd
import schedule
import time

def ftp_import():

    # importing data from NOAA ftp server
    ftp = FTP("ftp.swpc.noaa.gov")
    ftp.login()
    ftp.cwd('pub')
    ftp.cwd('weekly')

    with open('27DO.txt', 'wb') as fp:
        ftp.retrbinary('RETR 27DO.txt', fp.write)

    # formatting file into array
    lines = []
    with open('27DO.txt', 'rt') as fore_27:
        for line in fore_27:
            lines.append(line)

    # closing connection
    ftp.quit()

    # prepping for df
    forecast_27 = []

    for i, line in enumerate(lines[10:-1]):
        forecast_27.append(line.split())

    headers = ['Year', 'Month', 'Date', 'Radio Flux', 'Planetary A Index', 'Largest Kp Index']

    df_27fore = pd.DataFrame(forecast_27[1:], columns=headers)

    # cleaning df
    df_27fore['Date'] = df_27fore[['Month', 'Date']].astype(str).agg(' '.join, axis=1)
    df_27fore = df_27fore.drop(df_27fore.columns[[0, 1, 3, 4]], axis=1)

    return df_27fore #pandas df
kpi_27day = ftp_import()

# data updates every monday, updating on tuesdays in case of delays

# def get_kpi_27day():
#     global kpi_27day 
#     kpi_27day = ftp_import()

# schedule.every().tuesday.do(get_kpi_27day)

def aurora_days(kpi):
    days = []
    for i in kpi_27day.index:
        if int(kpi_27day['Largest Kp Index'][i]) >= kpi:
            days.append(kpi_27day['Date'][i])
    return days # array of strings


# loop so that the scheduling task keeps on running all time
# while True:
#     schedule.run_pending()
#     time.sleep(1)

# scheduling df update blocks bot from going online (gets stuck in while loop)





