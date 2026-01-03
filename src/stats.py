from src.utils import *

# Simple wrapper since textwrap might use len/split internally? 
# We'll just print line by line or simplistic 70 char limit.
def print_wrapped(text, width=70):
    # Manual wrap
    curr_line = ""
    # We can't use split(' ') if we want to be super strict about using my_split
    words = my_split(text, ' ') 
    for word in words:
        if my_len(curr_line) + 1 + my_len(word) > width:
            print(curr_line)
            curr_line = word
        else:
            if my_len(curr_line) > 0:
                curr_line += " " + word
            else:
                curr_line = word
    if my_len(curr_line) > 0:
        print(curr_line)

def show_history():
    clear_screen()
    print(get_msg('OPT_HISTORY').center(50, "="))
    print()
    
    lines = read_file_lines(FILES['HISTORIA'])
    # Join manually? 
    content = ""
    for line in lines:
        content += line + " "
    
    print_wrapped(content, 70)
        
    print()
    print(get_msg('PRESS_C'), end="")
    while True:
        inp = my_strip(input().lower())
        if inp == 'c':
            break

def calculate_and_save_stats():
    """
    Reads Juego.txt, calculates stats, saves to Estadisticas.txt and returns them.
    Format of Juego.txt: Code, Name, Mode, Word/Phrase, Attempts, [Letters], Result
    """
    games = read_file_lines(FILES['JUEGO'])
    
    total_games = 0
    total_beg = 0
    total_adv = 0
    total_won = 0
    total_lost = 0
    
    word_defeats = {}
    phrase_defeats = {}
    
    player_scores = []
    
    for game in games:
        parts = my_split(my_strip(game), ',')
        if my_len(parts) < 7:
            continue
            
        # 0:Code, 1:Name, 2:Mode, 3:Word, 4:Attempts, 5:Letters, 6:Result, 7:Score
        name = my_strip(parts[1])
        mode = my_strip(parts[2])
        word = my_strip(parts[3]).upper()
        result = my_strip(parts[6]).lower()
        
        score = 0
        if my_len(parts) > 7:
             try:
                 score = int(my_strip(parts[7]))
             except ValueError:
                 score = 0
        
        # Add to scores list safely
        player_scores = my_append(player_scores, (name, score, mode))
        
        total_games += 1
        
        is_beg = False
        is_adv = False
        
        if mode.upper() == "PRINCIPIANTE" or mode.upper() == "BEGINNER":
            is_beg = True
        elif mode.upper() == "AVANZADO" or mode.upper() == "ADVANCED":
            is_adv = True
            
        if is_beg:
            total_beg += 1
            if "ganador" != result and "winner" != result: # defeat
                current = 0
                try:
                    current = word_defeats[word]
                except KeyError:
                    current = 0
                word_defeats[word] = current + 1
        elif is_adv:
            total_adv += 1
            if "ganador" != result and "winner" != result:
                current = 0
                try:
                    current = phrase_defeats[word]
                except KeyError:
                    current = 0
                phrase_defeats[word] = current + 1
                
        is_winner = False
        if result == "ganador" or result == "winner":
            is_winner = True
            
        if is_winner:
            total_won += 1
        else:
            total_lost += 1
            
    # Find max defeats
    most_defeated_word = "N/A"
    max_count = 0
    for w in word_defeats: 
        c = word_defeats[w]
        if c > max_count:
            max_count = c
            most_defeated_word = w
            
    most_defeated_phrase = "N/A"
    max_count_p = 0
    for w in phrase_defeats:
        c = phrase_defeats[w]
        if c > max_count_p:
            max_count_p = c
            most_defeated_phrase = w
    
    wd_count = 0
    if most_defeated_word != "N/A":
        wd_count = word_defeats[most_defeated_word]
        
    pd_count = 0
    if most_defeated_phrase != "N/A":
        pd_count = phrase_defeats[most_defeated_phrase]
    
    # Sort scores descending (Bubble sort because sort/sorted forbidden? "Toda funcion built-in que deseen utilizar debe ser validada")
    # sorted() is built-in. user said "append, Split, strip, pop, len or in no están permitidas".
    # sorted() is NOT explicitly banned, but let's be safe and use bubble sort.
    n = my_len(player_scores)
    for i in range(n):
        for j in range(0, n-i-1):
            if player_scores[j][1] < player_scores[j+1][1]:
                player_scores[j], player_scores[j+1] = player_scores[j+1], player_scores[j]
    
    stats_lines = []
    stats_lines = my_append(stats_lines, f"1. Palabra con mas derrotas: {most_defeated_word} ({wd_count})")
    stats_lines = my_append(stats_lines, f"2. Frase con mas derrotas: {most_defeated_phrase} ({pd_count})")
    stats_lines = my_append(stats_lines, f"3. Total de juegos: {total_games}")
    stats_lines = my_append(stats_lines, f"4. Total juegos Principiante: {total_beg}")
    stats_lines = my_append(stats_lines, f"5. Total juegos Avanzado: {total_adv}")
    stats_lines = my_append(stats_lines, f"6. Ganados: {total_won} | Perdidos: {total_lost}")
    stats_lines = my_append(stats_lines, "")
    stats_lines = my_append(stats_lines, "TOP 5 LEADERBOARD")
    stats_lines = my_append(stats_lines, "-----------------")
    
    count = 0
    for s in player_scores:
        if count >= 5: break
        stats_lines = my_append(stats_lines, f"{count+1}. {s[0]} - {s[1]} pts ({s[2]})")
        count += 1
    
    write_file_lines(FILES['ESTADISTICAS'], stats_lines)
    return stats_lines

def show_stats():
    clear_screen()
    print(get_msg('OPT_STATS').center(50, "="))
    print()
    
    lines = calculate_and_save_stats()
    for line in lines:
        print(line)
        
    print()
    pause()

def show_help():
    clear_screen()
    print(get_msg('OPT_HELP').center(50, "="))
    print()
    
    lines = read_file_lines(FILES['AYUDA'])
    for line in lines:
        print(line)
        
    print()
    pause()
