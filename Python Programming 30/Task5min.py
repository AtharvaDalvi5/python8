import schedule
import time
import datetime

def WriteData():
    file = open("Marvellous.txt", "a")

    file.write("Task executed at:\n")
    file.write(str(datetime.datetime.now()))
    file.write("\n\n")

    file.close()

    print("Data written successfully.", datetime.datetime.now())

def main():
    print("Automation Script Started.")

    schedule.every(5).minutes.do(WriteData)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()