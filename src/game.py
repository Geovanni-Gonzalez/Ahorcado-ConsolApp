import random
from src.utils import *

STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
] # 7 stages (0 to 6)

def get_random_word(filepath):
    lines = read_file_lines(filepath)
    if my_len(lines) == 0:
        return None
    # Format: ID, WORD
    # random choice
    line = random.choice(lines)
    parts = my_split(line, ',')
    if my_len(parts) > 1:
        return my_strip(parts[1]).upper()
    return "DEFAULT"

def format_letters_list(letters):
    # manual join to look like ["A", "B"]
    res = "["
    count = 0 
    length = my_len(letters)
    for l in letters:
        res += '"' + l + '"'
        if count < length - 1:
            res += ", "
        count += 1
    res += "]"
    return res

def save_game(player, mode, word, attempts, used_letters, result):
    games = read_file_lines(FILES['JUEGO'])
    
    # Get Next ID
    next_id = 1
    if my_len(games) > 0:
        ids = []
        for g in games:
            parts = my_split(g, ',')
            try:
                ids = my_append(ids, int(my_strip(parts[0])))
            except ValueError:
                pass
        
        current_max = 0
        for i in ids:
            if i > current_max:
                current_max = i
        next_id = current_max + 1
        
    formatted_letters = format_letters_list(used_letters)
    
    # 1, Cristian, Principiante, tecnologico, 8, ["A", ...], ganador
    line = f"{next_id}, {player}, {mode}, {word}, {attempts}, {formatted_letters}, {result}"
    append_file_line(FILES['JUEGO'], line)

def play(player, mode, is_beginner):
    filepath = FILES['PALABRAS'] if is_beginner else FILES['FRASES']
    target = get_random_word(filepath)
    
    if target is None:
        print("Error: No words/phrases available.")
        pause()
        return

    guessed_letters = []
    attempts_max = 6 # 0 to 6 indices for stages. 6 wrong guesses -> dead.
    wrong_guesses = 0
    
    while True:
        clear_screen()
        print(get_msg('NEW_GAME').center(50, "="))
        print(f"Player: {player} | Mode: {mode}")
        print(STAGES[wrong_guesses])
        
        # Display word
        display = ""
        missing_count = 0
        for char in target:
            if char == ' ':
                 display += "  "
            elif my_in(char, guessed_letters):
                 display += char + " "
            else:
                 display += "_ "
                 missing_count += 1
        
        print("\n" + display + "\n")
        print(get_msg('USED_LETTERS') + format_letters_list(guessed_letters))
        print(get_msg('ATTEMPTS') + str(attempts_max - wrong_guesses))
        
        if missing_count == 0:
            print("\n" + get_msg('WIN'))
            save_game(player, mode, target, wrong_guesses, guessed_letters, "ganador")
            break
            
        if wrong_guesses >= attempts_max:
            print("\n" + get_msg('LOSE') + target)
            save_game(player, mode, target, wrong_guesses, guessed_letters, "perdedor")
            break
            
        print("\n" + get_msg('PROMPT'), end="")
        guess = my_strip(input()).upper()
        
        if my_len(guess) != 1:
            continue
            
        if not guess.isalpha(): # Allowed? isalpha is string method.
            # Assuming yes. If not, check ASCII range.
            continue
            
        if my_in(guess, guessed_letters):
            continue
            
        guessed_letters = my_append(guessed_letters, guess)
        
        if my_not_in(guess, target):
            wrong_guesses += 1

    print("\n" + get_msg('PRESS_C'), end="")
    while True:
        inp = my_strip(input().lower())
        if inp == 'c':
            break

def new_game():
    clear_screen()
    print(get_msg('NEW_GAME').center(50, "="))
    
    print(get_msg('ENTER_NAME'), end="")
    name = my_strip(input())
    if my_len(name) == 0: return

    # Language Selection (Bonus)
    print(get_msg('LANGUAGE_SELECT'), end="")
    lang_opt = my_strip(input()).upper()
    if lang_opt == 'EN':
        set_lang('EN')
    else:
        set_lang('ES')

    print(get_msg('SELECT_MODE'), end="")
    mode_input = my_strip(input()).upper()
    
    is_beginner = True
    mode_str = get_msg('MODE_BEG')
    
    if mode_input == 'A' or mode_input == 'AVANZADO' or mode_input == 'ADVANCED':
        is_beginner = False
        mode_str = get_msg('MODE_ADV')
    elif mode_input == 'P' or mode_input == 'PRINCIPIANTE' or mode_input == 'BEGINNER':
        is_beginner = True
    else:
        # Check first letter
        if my_len(mode_input) > 0 and mode_input[0] == 'A':
            is_beginner = False
            mode_str = get_msg('MODE_ADV')
    
    play(name, mode_str, is_beginner)
    
    # Restore language optional?
    # Requirement: "y que además toda la interfaz del juego también esté en inglés"
    # Doesn't say we revert. But usually meaningful to revert or stay.
    # I'll update main menu to use `get_msg` dynamic so it persists.
