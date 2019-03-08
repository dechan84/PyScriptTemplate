import sys
import argparse
import os
from subprocess import check_output


def convertFunc(listf, mode, sourceP):
    print("Enter mode: " + mode)
    path = os.path.dirname(os.path.abspath(__file__))
    inputList = []
    # Using list switch parsing
    if (listf is not None and sourceP is None):
        with open(listf, 'r') as f:
            # getting rid of the \n character
            inputList = [line.strip() for line in f]
            #print (inputList)
    # Using path switch (convert all) parsing
    elif (listf is None):
        if (sourceP is None):
            sourceP = "."
        path = path + "\\" + sourceP + "\\"
        print("Current path: " + path)
        for file in os.listdir(path):
            if (mode == "1"):
                if file.endswith(".std"):
                    inputList.append(path + file)
            elif(mode == "0"):
                if file.endswith(".ascii"):
                    inputList.append(path + file)
    else:
        print("Error: You need to use list or source path!")
        sys.exit(1)
    # Run convertion
    for file in inputList:
        print(inputList)
        if (mode == "1"):
            outputList = file.replace(".std", ".ascii")
            # Instead of xxxxx put your terminal cmd here
            # check_output("xxxxxx " + file + " " + outputList, shell=True)
        # Unkown reason why this mode is not working...
        elif (mode == "0"):
            outputList = file.replace(".ascii", ".std")
            # Instead of yyyyy put your terminal cmd here
            # check_output("yyyyyy " + file + " " + outputList, shell=True)


def main():

    myMode = "1"
    myList = None
    myPath = None
    # Using argparse for optional and positional cmd lines. Check
    # https://docs.python.org/3/howto/argparse.html
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        help="Optional path switch, receives a partial path with the current location," +
        " convert all available files on the path. Results available in the source path")
    parser.add_argument(
        "-l",
        help="Optional listfile switch, receives a .txt file that has the fullpaths of the namefiles to convert")
    parser.add_argument(
        "-m",
        help="Optional mode switch, depending on the mode you can add multiple functions. The default is 1")
    args = parser.parse_args()
    if (args.l):
        myList = args.l
    if (args.m):
        myMode = args.m
    if (args.p):
        myPath = args.p
    convertFunc(myList, myMode, myPath)


if __name__ == "__main__":
    main()
