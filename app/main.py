import sys

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
            
            #default case
            case _:
                print(f"{input_args[0]}: command not found")   

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