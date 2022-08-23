import sys
import clipboard
import json

SAVED_DATA = "clipboard.json "


def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


save_data("test.json", {"key": "value"})


def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("Enter a Key")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data Saved !!")
    elif command == "load":
        key = input("Enter a Key")
        if key in data:
            clipboard.copy(data[key])
            print("data copied to clipboard  ")
        else:
            print("key does not exist")
    elif command == "list":
        print(data)
    else:
        print("Unknown Command")
else:
    print("please pass exactly one command.")
