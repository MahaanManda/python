import os

def print_directory_tree(path, indent=""):
    if os.path.isdir(path):
        print(indent + f"[{os.path.basename(path)}]")
        items = sorted(os.listdir(path))
        for item in items:
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                print_directory_tree(item_path, indent + "  ")
            else:
                print(indent + "  " + item)
    else:
        print("Invalid directory path.")

# path_to_directory = "/Users/fr33nu/downloads/Telegram Desktop"
path_to_directory = "/Users/fr33nu/Desktop/python"
print_directory_tree(path_to_directory)
