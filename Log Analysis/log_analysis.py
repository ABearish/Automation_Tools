#!/usr/bin/env python3
import csv
import re
from sys import argv as s_argv
from operator import itemgetter

def log_error(error_dict:dict, message:str)->None:
    curr_count = error_dict.get(message, 0)
    error_dict[message] = curr_count + 1

def log_user_count(user_dict:dict, usr:str, type_of_message:str)->None:
    is_user_present = usr in user_dict
    if not is_user_present: user_dict[usr] = {"ERROR": 0, "INFO":0}
    user_dict[usr][type_of_message] = user_dict[usr][type_of_message] + 1

def prepare_data_for_csv(log_tuple:tuple, header:list, filename:str, callback_func)->None:
    data_list = []
    for k,v in log_tuple:
        if len(header) == 2:    
            data_list.append({
                header[0]: k,
                header[1]: v
        })
        elif len(header) == 3:
            user_name = k
            err_count = v['ERROR']
            info_count = v['INFO']
            data_list.append({
                header[0]: user_name,
                header[1]: err_count,
                header[2]: info_count
        })
    callback_func(data_list, filename, header)

def write_to_csv(data_list:dict, filename:str, fieldnames:list)->None:
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_list)
        print(f"Success: Data written to {filename} at ./log_analysis")
    except Exception as e:
        print(f"ERROR! during file writing: {e}")

# Parse through log file and extract whether its INFO or ERROR
def parse_data(file_path:str):
    error_count = {}
    user_count = {} 
    with open(file_path, 'r') as log_file:
        pattern = r"ticky: ([A-Z]+)\s([\w\s']+).*?\((.*?)\)"
        lines = log_file.readlines()
        for line in lines:        
            result = re.search(pattern, line)
            # A check in case there's no match
            if result is None: continue
            type_of_log = result.group(1).strip()
            message = result.group(2).strip()
            user = result.group(3).strip()
            if type_of_log == "ERROR":
                log_error(error_count, message)
                log_user_count(user_count, user, "ERROR")
            elif type_of_log == "INFO":
                log_user_count(user_count, user, "INFO")
    
    # Sorts Error_Counts by highest Value and User_counts by alphabetical order1
    error_count = sorted(error_count.items(), key=itemgetter(1), reverse=True)
    user_count = sorted(user_count.items(), key=itemgetter(0)) 
    prepare_data_for_csv(error_count, ["Error Message", "Count"], "error_message.csv", write_to_csv)
    prepare_data_for_csv(user_count, ["User", "Error", "Info" ], "user_statistics.csv", write_to_csv)

def main()-> None:
    file_path_or_default = './syslog.log'
    file_msg = f"No file path provided. Using default: {file_path_or_default}"
    if len(s_argv) > 1:
        file_path_or_default= sys.argv[1]
        file_msg = f"Using provided file path: {s_argv[1]}"
    
    print(file_msg)
    parse_data(file_path_or_default)

if __name__ == "__main__":
    main()