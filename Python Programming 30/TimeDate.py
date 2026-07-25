import schedule
import time
import datetime

def Display():
    print("Current Time And Date",datetime.datetime.now())

def main():
    print("Automation Script Started. ")

    schedule.every(10).seconds.do(Display)    
    
    while True:
        schedule.run_pending()
        time.sleep(1)
    
    print("end of Automation Script")

if __name__=="__main__":
    main()