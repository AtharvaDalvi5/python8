import schedule
import time

message = input("Enter message : ")
interval = int(input("Enter interval in seconds : "))

def Display():
    print(message)

def main():
    if interval <= 0:
        print("Interval should be greater than zero.")
        return

    print("Automation Script Started.")

    schedule.every(interval).seconds.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()