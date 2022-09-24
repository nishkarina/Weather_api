from ast import Delete
import sys
from winreg import DeleteKey, DeleteValue
import clipboard
import json

SAVED_DATA = 'clipboard.json'   #Created a variable named SAVED_DATA, whatever data I want to store essentially

'''To save data in json format'''
def save_data(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data,f)
'''Creating a json file named as test and passing key value pair'''
# save_items("test.json", {"key":"value"})


'''To load data we have created a function named load_items'''
def load_data(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data
    except:
        return {}


if len(sys.argv) >= 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)    #we have define a data variable here, which will give python dictionary that it will get

    
    if command == 'save':
        key = input('Enter a key: ')
        data[key] = clipboard.paste()  #this will store the key associated with our data
        save_data(SAVED_DATA,data)  #this will call our function to store or overwrite the data
        print('data has been saved')

    elif command == 'load':
        key = input('Enter the key: ')
        if key in data:
            clipboard.copy(data[key])
            print('data copied to clipboard.')
        else:
            print('key does not exists')


    elif command == 'list':
        print(data)
    else:
        print('unknown command')
else:
    print('Please pass exactly one command')