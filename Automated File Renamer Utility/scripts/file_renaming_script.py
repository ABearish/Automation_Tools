#!/usr/bin/env/ python3
from sys import exit as s_exit, argv as s_argv
from subprocess import run, CalledProcessError

def traverse_txt_file(file_path:str)->None:
    try:
        with open(file_path, 'r') as filelines:
            lines = filelines.readlines()
            for f in lines:
                old_file_name = f.strip()
                new_file_name = old_file_name.replace("jane", "jdoe")
                try:
                    run([f"mv", old_file_name, new_file_name], check=True)
                    print(f"SUCCESS: Renamed '{old_file_name}' to {new_file_name}")
                except CalledProcessError as e:
                    print(f"RENAME FAILED: File '{old_file_name}'. Command error: {e}")
    except FileNotFoundError as file_error:
        print(f"Failed: Cannot read file: \nError: {file_error}")
        s_exit(1)
    except Exception as e:
        print(f"Failed! Unexpected ERROR: \nError: {e}")
        s_exit(1)

def main()->None:
    file_path = ""
    if len(s_argv) > 1:
        file_path = s_argv[1]
    else:
        print(f"No file path provided\nExiting..")
        s_exit(1) 
    traverse_txt_file(file_path)

if __name__ == "__main__":
    main()