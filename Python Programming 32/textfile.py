import schedule
import time
import datetime

def CreateFile():

    filename = "File_" + datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    file = open(filename, "w")
    file.write("Filename : " + filename + "\n")
    file.write("Creation Date : " + str(datetime.date.today()) + "\n")
    file.write("Creation Time : " + str(datetime.datetime.now()) + "\n")
    file.close()

    print("File Created")

def main():

    print("Automation Script Started")

    schedule.every(1).minutes.do(CreateFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()