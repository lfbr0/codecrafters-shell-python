import sys
import shutil
import subprocess

#shell builtin commands
SHELL_BUILTINS = [
    'echo',
    'exit',
    'type'
]

"""
Handle input from user
"""
def handle_input(input_args):
    match input_args[0]:
            #handle exit from shell
            case 'exit':
                if len(input_args) < 2:
                    exit(0)
                else:
                    try:
                        exit_code = int(input_args[1])
                        exit(exit_code)
                    except ValueError:
                        print(f"exit: return code {input_args[1]} is not an integer!")
            
            #handle echo
            case 'echo':
                print(' '.join(input_args[1:]))
            
            #handle type
            case 'type':
                if len(input_args) < 2:
                    print(f"type: not enough arguments passed!")
                else:
                    type_target = input_args[1]
                    if type_target in SHELL_BUILTINS:
                        print(f'{type_target} is a shell builtin')
                    else:
                        type_target_path = find_executable(type_target)
                        if type_target_path == None:
                            print(f"{type_target} not found")
                        else:
                            print(f"{type_target} is {type_target_path}")
            
            #default case -> try to find program in PATH
            case _:
                program_path = find_executable(input_args[0])
                if program_path == None:
                    print(f"{input_args[0]}: command not found")
                else:
                    #if found execute it, and redirect stdout of it to this out
                    program_args = input_args[1:]
                    program_process = subprocess.run([program_path] + program_args, capture_output=True, text=True)
                    print(program_process.stdout.strip())

"""
Find executable in PATH variable and return its path...
"""
def find_executable(target):
    return shutil.which(target)

"""
Main function
"""
if __name__ == "__main__":
    try:
        #app loop
        while (True):
            # Uncomment this block to pass the first stage
            sys.stdout.write("$ ")
            sys.stdout.flush()

            # Wait for user input & split into space strings
            input_args = input().split()
            
            #handle inputs
            handle_input(input_args)
            
        #continue
        pass
    except KeyboardInterrupt:
        pass #ignore, user wants to quit shell