import sys
import time
import datetime

def CreateLog():

    timestamp = time.ctime()

    logFileName = "MarvellousLog_%s.txt" % (timestamp)
    logFileName = logFileName.replace(" ", "_")
    logFileName = logFileName.replace(":", "_")

    print("Log File Created :", logFileName)

    fobj = open(logFileName, "w")

    fobj.write("Log file created successfully.\n")
    fobj.write("Creation Time : ")
    fobj.write(str(datetime.datetime.now()))

    fobj.close()

def main():

    Border = "-" * 40

    print(Border)
    print(" Marvellous Automation Script ")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Automation Script creates a log file.")
            print("Usage: python Filename.py start")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as")
            print("python Filename.py start")

        else:
            CreateLog()

    else:
        print("Invalid Parameter")
        print("Please use --h or --u for more information.")

    print(Border)
    print("Thank you for using Marvellous Automation Script")
    print(Border)

if __name__ == "__main__":
    main()