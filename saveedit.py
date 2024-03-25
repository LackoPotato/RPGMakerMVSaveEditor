import getopt, json, lzstring,sys
from pathlib import Path
argumentList = sys.argv[1:]
options = "i:o:"
long_options = ["input=", "output="]

arguments, values = getopt.getopt(argumentList, options, long_options)
if len(arguments) == 0:
    raise Exception("No command line arguments provided\n(Required) Use -input (-i) for save file location\n(Optional) Use -output (-o) for output file location")

noOutputPath = True
for i in range(int(len(arguments))):
    argument = arguments[i][0]
    value =  arguments[i][1]
    if argument in ("-o", "--output"):
        output_path = Path(value)
        noOutputPath = False
        if not output_path.is_dir():
            raise Exception("Please provide a valid output path such as ./")
    elif argument in ("-i", "--input"):
        input_path = Path(value)
        if not input_path.is_file():
            raise Exception("Please provide a valid input file such as ./file.path")

input_path = str(input_path)
if noOutputPath:
    output_path = "./"
else:
    output_path = str(output_path)

file = open(input_path).read()
lz = lzstring.LZString()

fileData = lz.decompressFromBase64(file)
fileData = json.loads(fileData)

def print_subdirectory(data = []):
    print("Data: ")
    for thing in data:print("   ",thing)
    print("\n")

def request_subdirectory(directory = []):
    selectionFlag = True
    while selectionFlag:
        selection = input("Selection? ")
        if selection in directory:
            selectionFlag = False
            selectedValue = directory[selection]
        else:
            print("Write a valid subdirectory")
    return [selectedValue,selection]

def change_value(dictionary, path, new_value):
    current = dictionary
    for key in path[:-1]:
        current = current[key]
    current[path[-1]] = new_value

def dict_in_array(array):
    for value in array:
        if isinstance(value, dict):
            return True

def request_data(types = ['int','bool','float','str']):
    def set_type(value,typeofValue):
        if typeofValue == 'int':
            return int(value)
        elif typeofValue == 'bool':
            return bool(value)
        elif typeofValue == 'float':
            return float(value)
        else:
            return str(value)
    
    value = input("Data to set: ")
    selectionFlag = True
    while selectionFlag:
        dataType = input(f"Type of value {types}: ")
        if dataType in types:
            try:
                set_type(value,dataType)
            except:
                print(f"Choose a type which can transform {value}")
            else:
                return set_type(value,dataType)
        else:
            print(f"Choose a valid type {types}")

keepEditing = "y"
while keepEditing == "y":
    selectedData = fileData.copy()
    path = []
    while isinstance(selectedData, dict) or (isinstance(selectedData, list) and dict_in_array(selectedData)):
        if isinstance(selectedData, list) and dict_in_array(selectedData):
            for index in range(len(selectedData)):
                print("   ",index," ",type(selectedData[index]))
            print("Dict in Array, please choose an index")
            selectionFlag = True
            while selectionFlag:
                index = input(f"Index (0 - {len(selectedData)}): ")
                try:
                    int(index)
                    selectedData[int(index)]
                except:
                    print(f"Write a valid index (0 - {len(selectedData)})")
                else:
                    path.append(int(index))
                    selectionFlag = False
                    selectedData = selectedData[int(index)]
        else:
            print_subdirectory(selectedData)
            processData = request_subdirectory(selectedData)
            selectedData = processData[0]
            path.append(processData[1])
        print(f"Cur path: {path}\n")

    if not isinstance(selectedData, (int,float,str,type(None))):
        if input("Print data? y/n ") == "y":
            for i in range(len(selectedData)):
                    print(f"{i} {selectedData[i]}")
        print(f"Length of selected data = {len(selectedData)}\n")

    if input("Read data? y/n ") == "y":
        if isinstance(selectedData, list):
            selectionFlag = True
            while selectionFlag:
                index = input(f"Index (0 - {len(selectedData)}): ")
                try:
                    int(index)
                    selectedData[index]
                except:
                    print(f"Write a valid index (0 - {len(selectedData)})")
                else:
                    print(f"Value of Index: {selectedData[int(index)]}")
                    if input("Override this variable? y/n ") == "y":
                        path.append(int(index))
                        selectionFlag = False
                        change_value(fileData,path,request_data())
                    elif input("Exit path? y/n ") == "y":
                        selectionFlag = False
        elif isinstance(selectedData, (int,float,str,type(None))):
            print(f"Data: {selectedData}")
            if input("Override this variable? y/n ") == "y":
                change_value(fileData,path,request_data())
    
    keepEditing = input("Keep editing? y/n ")

if input("Export? y/n") == "y":
    if input("Export to JSON? y/n ") == "y":
        output = open(f"{output_path}output_edited.json", "x")
        output.write(json.dumps(fileData))
        print(f"Added file to {output_path}output_edited.json")
    else:
        output = open(f"{output_path}outputedited.txt", "x")
        output.write(lz.compressToBase64(json.dumps(fileData)))
        print(f"Added file to {output_path}output_edited.txt")
