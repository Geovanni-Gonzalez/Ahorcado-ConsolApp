import os

# Constants
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

FILES = {
    'ACCESO': os.path.join(DATA_DIR, 'Acceso.txt'),
    'PALABRAS': os.path.join(DATA_DIR, 'Palabras.txt'),
    'FRASES': os.path.join(DATA_DIR, 'Frases.txt'),
    'HISTORIA': os.path.join(DATA_DIR, 'Historia.txt'),
    'AYUDA': os.path.join(DATA_DIR, 'Ayuda.txt'),
    'JUEGO': os.path.join(DATA_DIR, 'Juego.txt'),
    'ESTADISTICAS': os.path.join(DATA_DIR, 'Estadísticas.txt')
}

# Global State
CURRENT_LANG = 'ES'

# Strings
STRINGS = {
    'ES': {
        'MAIN_MENU': "MENÚ PRINCIPAL",
        'OPT_ADMIN': "(A) Opciones administrativas",
        'OPT_PLAYER': "(J) Opciones de jugador",
        'OPT_EXIT': "(S) Salir",
        'INVALID_OPT': "Opción inválida, intente de nuevo.",
        'PROMPT': "Seleccione una opción: ",
        'ADMIN_MENU': "OPCIONES ADMINISTRATIVAS",
        'OPT_WORDS': "(P) Gestión de Palabras",
        'OPT_PHRASES': "(F) Gestión de Frases",
        'OPT_RETURN': "(R) Retornar",
        'PLAYER_MENU': "OPCIONES DE JUGADOR",
        'OPT_NEW_GAME': "Nuevo Juego",
        'OPT_HISTORY': "Historia del Juego",
        'OPT_STATS': "Estadísticas de Juegos",
        'OPT_HELP': "Ayuda",
        'PASSWORD_PROMPT': "Ingrese clave de acceso: ",
        'ACCESS_DENIED': "Acceso denegado.",
        'ACCESS_GRANTED': "Acceso concedido.",
        'PRESS_ENTER': "Presione ENTER para continuar...",
        'PRESS_C': "Presione C para continuar...",
        'WORD_MGM': "GESTIÓN DE PALABRAS",
        'PHRASE_MGM': "GESTIÓN DE FRASES",
        'ADD': "Incluir",
        'DELETE': "Eliminar",
        'MODIFY': "Modificar",
        'SHOW': "Mostrar",
        'ENTER_WORD': "Ingrese la palabra: ",
        'ENTER_PHRASE': "Ingrese la frase: ",
        'EXISTS': "Ya existe.",
        'ADDED': "Agregado exitosamente.",
        'ENTER_ID': "Ingrese el ID: ",
        'NOT_FOUND': "No encontrado.",
        'DELETED': "Eliminado exitosamente.",
        'MODIFIED': "Modificado exitosamente.",
        'NEW_GAME': "NUEVO JUEGO",
        'ENTER_NAME': "Ingrese su nombre: ",
        'SELECT_MODE': "Seleccione modo ((P)rincipiante / (A)vanzado): ",
        'MODE_BEG': "Principiante",
        'MODE_ADV': "Avanzado",
        'WIN': "¡GANADOR!",
        'LOSE': "¡PERDEDOR! La respuesta era: ",
        'PLAY_AGAIN': "¿Jugar de nuevo? (S/N): ",
        'USED_LETTERS': "Letras usadas: ",
        'ATTEMPTS': "Intentos restantes: ",
        'LANGUAGE_SELECT': "Select Language / Seleccione Idioma (EN/ES): "
    },
    'EN': {
        'MAIN_MENU': "MAIN MENU",
        'OPT_ADMIN': "(A) Administrative Options",
        'OPT_PLAYER': "(J) Player Options", 
        'OPT_EXIT': "(S) Exit",
        'INVALID_OPT': "Invalid option, try again.",
        'PROMPT': "Select an option: ",
        'ADMIN_MENU': "ADMINISTRATIVE OPTIONS",
        'OPT_WORDS': "(P) Word Management",
        'OPT_PHRASES': "(F) Phrase Management",
        'OPT_RETURN': "(R) Return",
        'PLAYER_MENU': "PLAYER OPTIONS",
        'OPT_NEW_GAME': "New Game",
        'OPT_HISTORY': "Game History",
        'OPT_STATS': "Game Statistics",
        'OPT_HELP': "Help",
        'PASSWORD_PROMPT': "Enter access password: ",
        'ACCESS_DENIED': "Access denied.",
        'ACCESS_GRANTED': "Access granted.",
        'PRESS_ENTER': "Press ENTER to continue...",
        'PRESS_C': "Press C to continue...",
        'WORD_MGM': "WORD MANAGEMENT",
        'PHRASE_MGM': "PHRASE MANAGEMENT",
        'ADD': "Add",
        'DELETE': "Delete",
        'MODIFY': "Modify",
        'SHOW': "Show",
        'ENTER_WORD': "Enter word: ",
        'ENTER_PHRASE': "Enter phrase: ",
        'EXISTS': "Already exists.",
        'ADDED': "Added successfully.",
        'ENTER_ID': "Enter ID: ",
        'NOT_FOUND': "Not found.",
        'DELETED': "Deleted successfully.",
        'MODIFIED': "Modified successfully.",
        'NEW_GAME': "NEW GAME",
        'ENTER_NAME': "Enter your name: ",
        'SELECT_MODE': "Select mode ((P)rincipiante[Beginner] / (A)vanzado[Advanced]): ",
        'MODE_BEG': "Beginner",
        'MODE_ADV': "Advanced",
        'WIN': "WINNER!",
        'LOSE': "LOSER! The answer was: ",
        'PLAY_AGAIN': "Play again? (Y/N): ",
        'USED_LETTERS': "Used letters: ",
        'ATTEMPTS': "Attempts remaining: ",
        'LANGUAGE_SELECT': "Select Language / Seleccione Idioma (EN/ES): "
    }
}

# Custom Helpers to avoid restricted built-ins
def my_len(seq):
    c = 0
    for _ in seq:
        c += 1
    return c

def my_in(item, seq):
    for x in seq:
        if x == item:
            return True
    return False

def my_not_in(item, seq):
    return not my_in(item, seq)

def my_strip(s):
    length = my_len(s)
    if length == 0:
        return ""
    
    start = 0
    while start < length:
        c = s[start]
        if c != ' ' and c != '\n' and c != '\r' and c != '\t':
            break
        start += 1
        
    end = length - 1
    while end >= start:
        c = s[end]
        if c != ' ' and c != '\n' and c != '\r' and c != '\t':
            break
        end -= 1
        
    res = ""
    # Range is allowed? "structures like while and for". Range is a type/function. 
    # Usually range is allowed. If NOT, use while.
    # I'll use while just to be safe.
    i = start
    while i <= end:
        res += s[i]
        i += 1
    return res

def my_split(s, delim):
    res = []
    curr = ""
    for char in s:
        if char == delim:
            res = res + [curr] 
            curr = ""
        else:
            curr += char
    res = res + [curr]
    return res

def my_append(lst, item):
    # lst.append(item) IS BANNED
    # use concatenation
    return lst + [item]

# Standard Utils
def get_msg(key):
    return STRINGS[CURRENT_LANG].get(key, key)

def set_lang(lang):
    global CURRENT_LANG
    if lang == 'ES' or lang == 'EN':
        CURRENT_LANG = lang

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    print(get_msg('PRESS_ENTER'))
    input()

def read_file_lines(filepath):
    if not os.path.exists(filepath):
        return []
    with open(filepath, 'r', encoding='utf-8') as f:
        # readlines() is allowed? implicit loop. 
        # "Toda funcion built-in ... validada"
        # I'll use basic iteration over file object.
        lines = []
        for line in f:
            stripped = my_strip(line)
            if my_len(stripped) > 0:
                lines = my_append(lines, stripped)
        return lines

def write_file_lines(filepath, lines):
    with open(filepath, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(str(line) + "\n")

def append_file_line(filepath, line):
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(str(line) + "\n")
