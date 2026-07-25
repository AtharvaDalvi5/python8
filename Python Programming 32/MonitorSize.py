import schedule
import time
import datetime
import os
import sys

def FileSize(path):

    file = open("FilesizeLog.txt", "a")

    if os.path.exists(path):

        size = os.path.getsize(path)

        file.write("File Path : " + path + "\n")
        file.write("File Size : " + str(size) + " Bytes\n")
        file.write("Date and Time : " + str(datetime.datetime.now()) + "\n")

    else:

        file.write("File Not Found : " + path + "\n")
        file.write("Date and Time : " + str(datetime.datetime.now()) + "\n")

    file.close()

    print("Information Stored")

def main():

    path = sys.argv[1]

    schedule.every(30).seconds.do(FileSize, path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()