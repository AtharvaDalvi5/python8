import schedule
import time
import datetime
import os
import sys

def CountFiles(path):

    count = 0

    for FolderName, SubFolder, FileName in os.walk(path):
        count = count + len(FileName)

    file = open("DirectoryCountLog.txt", "a")

    file.write("Directory : " + path + "\n")
    file.write("Total Files : " + str(count) + "\n")
    file.write("Date and Time : " + str(datetime.datetime.now()) + "\n\n")

    file.close()

    print("Information Stored")

def main():

    if len(sys.argv) != 2:
        print("Usage : python Filename.py DirectoryPath")
        return

    path = sys.argv[1]

    print("Automation Script Started.")

    schedule.every(5).minutes.do(CountFiles, path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()