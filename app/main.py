import sys
from command_handler import handle_input

def main():

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


if __name__ == "__main__":
    main()
