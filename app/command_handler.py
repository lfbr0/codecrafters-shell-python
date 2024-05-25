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
                    
            #default case
            case _:
                print(f"{input_args[0]}: command not found")   
                