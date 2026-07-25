import schedule
import time
import os
import shutil
import sys

source = sys.argv[1]
destination = sys.argv[2]

def CopyFiles():

    if not os.path.isdir(source) or not os.path.isdir(destination):
        print("Invalid Directory")
        return

    log = open("CopyLog.txt", "a")

    for FolderName, SubFolder, FileName in os.walk(source):

        for fname in FileName:

            if fname.endswith(".txt"):

                try:
                    shutil.copy(os.path.join(FolderName, fname), destination)
                    log.write(fname + " Copied\n")

                except:
                    log.write(fname + " Not Copied\n")

    log.close()

    print("Copy Completed")

def main():

    schedule.every(10).minutes.do(CopyFiles)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()