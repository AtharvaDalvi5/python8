import sys
import os
def DirectoryScnner(DirectoryPath):
    print("Files from the directory are : ")
    for Foldername,Subfolder,Filename in os.walk(DirectoryPath):
        for fname in Filename:
            print(fname)
def main():

    Border = "-"*40
    print(Border)
    print(" Marvellous Automation Script ")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Automation Script is Used to travel the Directory")
            print("For better Usage Please check --u flag")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as")
            print("python  Filename.py DirectoryName")
            print("Directory name Should be Absolute path ")
        else:
            DirectoryScnner(sys.argv[1])
    else :
        print("Invalid Parameter")
        print("please Use --h or --u for more information")

    print(Border)
    print(" Thank you for using  Marvellous Automation Script ")
    print(Border)

if __name__=="__main__":
    main()