from src.utils import *

def login():
    """
    Prompts for password and verifies it against the file.
    Returns True if successful, False otherwise.
    """
    print("\n" + get_msg('PASSWORD_PROMPT'), end="")
    user_input = my_strip(input())
    
    lines = read_file_lines(FILES['ACCESO'])
    # lines are already stripped by read_file_lines
    if my_len(lines) > 0 and user_input == lines[0]:
        print(get_msg('ACCESS_GRANTED'))
        return True
    else:
        print(get_msg('ACCESS_DENIED'))
        return False
