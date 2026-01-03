from src.utils import *

def get_next_id(lines):
    if not lines: # Allowed (implicit bool check on list)
        return 1
    ids = []
    for line in lines:
        try:
            parts = my_split(line, ',')
            ids = my_append(ids, int(my_strip(parts[0])))
        except ValueError:
            continue
            
    if my_len(ids) == 0:
        return 1
        
    current_max = 0
    for i in ids:
        if i > current_max:
            current_max = i
            
    return current_max + 1

def is_word_used(word, is_phrase=False):
    """
    Checks if the word/phrase has been used in a game (exists in Juego.txt).
    """
    games = read_file_lines(FILES['JUEGO'])
    count = 0 
    for game in games:
        parts = my_split(game, ',')
        if my_len(parts) >= 4:
            played_word = my_strip(parts[3]).upper()
            if played_word == word.upper():
                return True
    return False

def manage_file(filepath, item_name, is_phrase=False):
    """
    Generic CRUD for words/phrases file.
    Format: ID, TEXT
    """
    while True:
        clear_screen()
        title = get_msg('PHRASE_MGM') if is_phrase else get_msg('WORD_MGM')
        print(title.center(50, "="))
        
        print(f"(1) {get_msg('ADD')}")
        print(f"(2) {get_msg('DELETE')}")
        print(f"(3) {get_msg('MODIFY')}")
        print(f"(4) {get_msg('SHOW')}")
        print(f"(R) {get_msg('OPT_RETURN')}")
        
        print("\n" + get_msg('PROMPT'), end="")
        op = my_strip(input().upper())
        
        if op == '1': # ADD
            print(get_msg('ENTER_PHRASE') if is_phrase else get_msg('ENTER_WORD'), end="")
            text = my_strip(input()).upper()
            if my_len(text) == 0: continue
            
            lines = read_file_lines(filepath)
            
            # Check duplicates
            exists = False
            for line in lines:
                parts = my_split(line, ',')
                if my_len(parts) > 1 and my_strip(parts[1]).upper() == text:
                    exists = True
                    break
            
            if exists:
                print(get_msg('EXISTS'))
            else:
                new_id = get_next_id(lines)
                append_file_line(filepath, f"{new_id}, {text}")
                print(get_msg('ADDED'))
            pause()
            
        elif op == '2': # DELETE
            print(get_msg('ENTER_ID'), end="")
            try:
                target_id = int(my_strip(input()))
            except ValueError:
                continue
            
            lines = read_file_lines(filepath)
            found = False
            new_lines = []
            target_text = ""
            
            for line in lines:
                parts = my_split(line, ',')
                curr_id = int(my_strip(parts[0]))
                if curr_id == target_id:
                    found = True
                    target_text = my_strip(parts[1])
                else:
                    new_lines = my_append(new_lines, line)
            
            if not found:
                print(get_msg('NOT_FOUND'))
            else:
                if is_word_used(target_text, is_phrase):
                    print("Error: " + get_msg('EXISTS') + " (In History)")
                else:
                    write_file_lines(filepath, new_lines)
                    print(get_msg('DELETED'))
            pause()

        elif op == '3': # MODIFY
            print(get_msg('ENTER_ID'), end="")
            try:
                target_id = int(my_strip(input()))
            except ValueError:
                continue
                
            lines = read_file_lines(filepath)
            found = False
            new_lines = []
            
            for line in lines:
                parts = my_split(line, ',')
                curr_id = int(my_strip(parts[0]))
                if curr_id == target_id:
                    found = True
                    print(f"Current: {my_strip(parts[1])}")
                    print(get_msg('ENTER_PHRASE') if is_phrase else get_msg('ENTER_WORD'), end="")
                    new_text = my_strip(input()).upper()
                    if my_len(new_text) > 0:
                        # Check duplicate
                        dup = False
                        current_other_lines = []
                        for l in lines:
                             parts_l = my_split(l, ',')
                             if int(my_strip(parts_l[0])) != target_id:
                                current_other_lines = my_append(current_other_lines, l)
                        
                        for l in current_other_lines:
                             parts_l = my_split(l, ',')
                             if my_len(parts_l) > 1 and my_strip(parts_l[1]).upper() == new_text:
                                 dup = True
                                 break
                        if dup:
                            print(get_msg('EXISTS'))
                            new_lines = my_append(new_lines, line)
                        else:
                            new_lines = my_append(new_lines, f"{curr_id}, {new_text}")
                            print(get_msg('MODIFIED'))
                    else:
                        new_lines = my_append(new_lines, line)
                else:
                    new_lines = my_append(new_lines, line)
            
            if not found:
                print(get_msg('NOT_FOUND'))
            else:
                write_file_lines(filepath, new_lines)
            pause()

        elif op == '4': # SHOW
            print("-" * 40)
            print("ID | TEXT")
            print("-" * 40)
            lines = read_file_lines(filepath)
            for line in lines:
                print(line)
            print("-" * 40)
            pause()
            
        elif op == 'R':
            break

def admin_menu():
    while True:
        clear_screen()
        print(get_msg('ADMIN_MENU').center(50, "="))
        print(get_msg('OPT_WORDS'))
        print(get_msg('OPT_PHRASES'))
        print(get_msg('OPT_RETURN'))
        
        print("\n" + get_msg('PROMPT'), end="")
        op = my_strip(input().upper())
        
        if op == 'P':
            manage_file(FILES['PALABRAS'], 'Word')
        elif op == 'F':
            manage_file(FILES['FRASES'], 'Phrase', is_phrase=True)
        elif op == 'R':
            break
        else:
            print(get_msg('INVALID_OPT'))
            pause()
