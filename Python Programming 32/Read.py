import schedule
import time
import sys

def ReadFile(path):

    try:

        file = open(path, "r")
        data = file.read()

        if data == "":
            print("File is Empty")
        else:
            print(data)

        file.close()

    except FileNotFoundError:
        print("File does not exist")

    except PermissionError:
        print("Permission Denied")

    except:
        print("File cannot be opened")

def main():

    path = sys.argv[1]

    schedule.every(1).minutes.do(ReadFile, path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()