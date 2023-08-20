import os

class MahaanUtil:

    def print_directory_tree(self, path, indent=""):
        if os.path.isdir(path):
            print(indent + f"[{os.path.basename(path)}]")
            items = sorted(os.listdir(path))
            for item in items:
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    self.print_directory_tree(item_path, indent + "  ")  # Use self to call the method recursively
                else:
                    print(indent + "  " + item)
        else:
            print("Invalid directory path.")

util = MahaanUtil()
path_to_directory = '/Users/fr33nu/Desktop/python'
util.print_directory_tree(path_to_directory)