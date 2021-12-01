from ftplib import FTP
import pandas as pd

# importing data from NOAA ftp server
ftp = FTP("ftp.swpc.noaa.gov")
ftp.login()
ftp.cwd('pub')
ftp.cwd('weekly')

with open('27DO.txt', 'wb') as fp:
    ftp.retrbinary('RETR 27DO.txt', fp.write)

# formatting file into array
lines_27 = []
with open('27DO.txt', 'rt') as fore_27:
    for line in fore_27:
        lines_27.append(line)

# closing connection
ftp.quit()