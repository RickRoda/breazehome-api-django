import requests
import os.path
import urllib3
import zipfile
import shutil
import time
from datetime import datetime
from datetime import timedelta
from feed_md_records import parseRecords
urllib3.disable_warnings()

# Miami Dade Records Daily Downloader Version 1.0
# Author - Richard Roda
# Description - This script will download the most recent daily zipfile from the Miami Dade
# FTP-API, unzip said file , and utilize the CSV Parser/Importer to bring the CSV data into 
# the BreazeHome CountyRecords and LienRecords databases.

# Variables #
basePath = os.path.dirname(__file__)
logPath = os.path.abspath(os.path.join(basePath, 'log.txt'))
logFile = open(logPath, 'a')
lastDownloadPath = os.path.abspath(os.path.join(basePath, 'last_download_date'))

# Functions #
# Write to the daily import log
def write_log(text):
    logFile.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S ') + text + '\n')

# download daily Miami Dade FTP API record with a specified date parameter
def download_daily_record(dateToDownload):
    #format date to proper format
    dateStr = dateToDownload.strftime('%m%d%Y')
    # create zip path #
    zipPath = os.path.abspath(os.path.join(basePath, dateStr + '.zip'))
    #compile API query string
    url = 'https://www2.miami-dadeclerk.com/Developers/api/FTPapi?folderName=Records&AuthKey=EE0C9D09-D8C5-4630-A8C2-E194F21D78A1&fileName=dly_records_' + dateStr + '.zip'
    write_log('Download from ' + url)
    try:
        response = requests.get(url)
        #if we recieve the OK status code #
        if response.status_code == 200:
            # write the zipfile to our system #
            with open(zipPath, 'wb') as f:
                f.write(response.content)
                f.close()
            write_log('download_daily_record zipfile success!')
            return True
        else:
            # daily zip file error, multiple reasons may cause this, with the most common being #
            # when trying to download a weekend or holiday date #
            write_log('download_daily_record failed with error code ' + str(response.status_code))
    except Exception as e:
        write_log('download_daily_record failed with exception: ' + str(e))
    return False

# update last_download_date with the most recent successful download date #
def update_last_download_date(dateObj):
    dateStr = dateObj.strftime('%m%d%Y')
    write_log('Update last download_daily_record to: ' + dateStr)
    with open(lastDownloadPath, 'w') as file:
        file.write(dateStr)
        file.close()

# unzip the last valid download file #
def unzip_last_download(dateObj):
    dateStr = dateObj.strftime('%m%d%Y')
    write_log('Unzipping last download_daily_record')
    dateStr+=".zip"
    with open(dateStr,'rb') as f:
        zf = zipfile.ZipFile(f)
        zf.extractall()
           

if __name__ == "__main__":
    write_log('==== Daily Miami Dade FTP API Download Initiated ====')
    with open(lastDownloadPath, 'r') as file:
        dateStr = file.read().replace('\n', '')
    dateStart = datetime.strptime(dateStr, '%m%d%Y') + timedelta(days=1)
    dateEnd = datetime.now()
    # while we still have daily downloads from past dates #
    while dateStart < dateEnd:
        print("Attempting to download daily Miami-Dade Records zipfile...")
        # if we successfully downloaded a new daily file #
        if (download_daily_record(dateStart)):
            print("Download Complete! File Date: " + dateStart.strftime('%m%d%Y'))
            # unzip the daily download file #
            print("Unzipping file! File Date: " + dateStart.strftime('%m%d%Y'))
            unzip_last_download(dateStart)
            print("Unzip complete!")
            print("Importing data for File Date "+ dateStart.strftime('%m%d%Y')+" into database...")
            recordFile = dateStart.strftime('%m%d%Y') + '.exp'
            zipFile = dateStart.strftime('%m%d%Y') + '.zip'
            zipSrc = "/home/breazer/breaze/breaze-api-django/county_records/import_scripts/" + zipFile
            zipDest = "/home/breazer/breaze/miamidaderecords/" + zipFile
            print("Parsing data. Please wait. This process may take a few minutes...")
            time.sleep(1)
            totalRecord, newRecord, updatedRecord =parseRecords(recordFile)
            # import the exp file extracted from the zip file and import data into db #
            print("Import for File " + recordFile + " Complete!")
            print("{} Miami Dade County Records for {} have been added\n{} new Miami Dade County Records have been added\n{} Miami Dade County Records have been updated".format(totalRecord, dateStart.strftime('%m%d%Y'), newRecord, updatedRecord))
            # update the last valid download to 'last_download_date' #
            update_last_download_date(dateStart)
            os.remove(recordFile)
            shutil.copyfile(zipSrc,zipDest)
            os.remove(zipFile)
        # continue to the next day #
        else:
            print("404 Error. File does not exist on the API")
            print("Possible Reasons:")
            print("1) File for today's date has not been uploaded to the API yet\n\t Uploads are done at 10:30PM EST")
            print("2) File date being requested is more than 30 days old.")
            print("3) File date being requested is in the future.")
        
        dateStart = dateStart + timedelta(days=1)
    write_log('==== Daily Miami Dade FTP API Download Completed ====')
    logFile.close()
