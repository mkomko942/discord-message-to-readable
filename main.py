from colorama import Fore
from collections import Counter

def most_frequent(List): 
    occurence_count = Counter(List) 
    return [name_line[0] for name_line in occurence_count.most_common(2)]

def remove_date(line_to_remove):
    if "Today" in line_to_remove:
        name_line = line_to_remove.split("Today")
        name_line[1] = ""
    elif "Yesterday" in line_to_remove:
        name_line = line_to_remove.split("Yesterday")
        name_line[1] = ""
    elif "/" in line_to_remove:
        name_line = [line_to_remove[:-11], ""]
    else:
        return line_to_remove
    return name_line

message  = open("message.txt", "r")

seperate_message = message.readlines()

for name_line in seperate_message:
    current_line = remove_date(name_line)
    if len(current_line) == 2:
        for name_line in current_line:
            print(f"{Fore.GREEN}{name_line}")
    else:
        print(f"{Fore.RESET}{str(name_line)}")
