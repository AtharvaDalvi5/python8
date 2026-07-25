import schedule
import time
import os
import sys

path = sys.argv[1]

def DeleteFiles():

    log = open("DeleteLog.txt", "a")

    for FolderName, SubFolder, FileName in os.walk(path):

        for fname in FileName:

            filepath = os.path.join(FolderName, fname)

            try:

                if os.path.getsize(filepath) == 0:

                    os.remove(filepath)

                    log.write(filepath + "\n")

            except PermissionError:

                print("Permission Denied :", filepath)

    log.close()

    print("Empty Files Deleted")

def main():

    schedule.every(1).hours.do(DeleteFiles)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()