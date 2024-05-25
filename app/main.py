import sys


def main():

    #list of recognized commands
    recognized_commands = []

    try:
        #app loop
        while (True):
            # Uncomment this block to pass the first stage
            sys.stdout.write("$ ")
            sys.stdout.flush()

            # Wait for user input & split into space strings
            input_args = input().split()

            if input_args[0] not in recognized_commands:
                print(f"{input_args[0]}: command not found")
        
        #continue
        pass
    except KeyboardInterrupt:
        pass #ignore, user wants to quit shell





if __name__ == "__main__":
    main()
