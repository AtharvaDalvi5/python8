import schedule
import time
import datetime
import shutil

s= input("Enter source file path : ")
dest = input("Enter destination folder path : ")

def Backup():

    filename = "Backup_" + datetime.datetime.now()+ ".txt"

    shutil.copy(s, dest + "\\" + filename)

    file = open("backup_log.txt", "a")
    file.write("Backup completed successfully at ")
    file.write(str(datetime.datetime.now()))
    file.write("\n")
    file.close()

    print("Backup Completed")

def main():
    print("Automation Script Started.")

    schedule.every(1).hours.do(Backup)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()