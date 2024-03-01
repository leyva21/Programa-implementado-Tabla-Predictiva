def PredictTable():
    terminals = {"function", '(', ')', 'var', ':', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'boolean', 'string', ';', 'empty'}
    non_terminals = {'S', 'F', 'N', 'PM', 'PA', 'PC', 'PL', 'V', 'X', 'T', 'LT', 'P', 'RN', 'L'} #Columnas  - y filas arriba |
    table = {
        'S': {
            'function': ['F', 'N', 'PM'],
            '(': None,
            'var': None,
            ':': None,
            ';': None,
            'boolean': None,
            'string': None,
            ')': None
        },
        'F': {
            'function': ['function'],
            '(': None,
            'var': None,
            ':': None,
            ';': None,
            'boolean': None,
            'string': None,
            ')': None
        },
        'PM': {
            '(': ['PA', 'PL', 'PC'],
            'var': None,
            ':': None,
            ';': None,
            'boolean': None,
            'string': None,
            ')': None,
            'function': None,
        },
        'PA': {
            '(': ['('],
            'function': None,
            'var': None,
            ':': None,
            ';': None,
            'boolean': None,
            'string': None,
            ')': None
        },
        'PC': {
            ')': [')'],
            'function': None,
            'var': None,
            ':': None,
            '(': None,
            ';': None,
            'boolean': None,
            'string': None,
        },
        'PL': {
            'var': ['V', 'X', 'LT'],
            'function': None,
            ':': None,
            ';': None,
            'boolean': None,
            'string': None,
        },
        'V': {
            'var': ['var'],
            'function': None,
            '(': None,
            ':': None,
            ';': None,
            'boolean': None,
            'string': None,
            ')': None
        },
        'X': {
            'a': ['N', ':', 'T'], 'b': ['N', ':', 'T'], 'c': ['N', ':', 'T'], 'd': ['N', ':', 'T'], 'e': ['N', ':', 'T'], 'f': ['N', ':', 'T'], 'g': ['N', ':', 'T'], 'h': ['N', ':', 'T'], 'i': ['N', ':', 'T'], 'j': ['N', ':', 'T'], 'k': ['N', ':', 'T'], 'l': ['N', ':', 'T'], 'm': ['N', ':', 'T'], 'n': ['N', ':', 'T'], 'o': ['N', ':', 'T'], 'p': ['N', ':', 'T'], 'q': ['N', ':', 'T'], 'r': ['N', ':', 'T'], 's': ['N', ':', 'T'], 't': ['N', ':', 'T'], 'u': ['N', ':', 'T'], 'v': ['N', ':', 'T'], 'w': ['N', ':', 'T'], 'x': ['N', ':', 'T'], 'y': ['N', ':', 'T'], 'z': ['N', ':', 'T'],
            'function': None,
            '(': None,
            ':': None,
            ';': None,
            'boolean': None,
            'string': None,
            ')': None
        },
        'N': {
            'a': ['L', 'RN'], 'b': ['L', 'RN'], 'c': ['L', 'RN'], 'd': ['L', 'RN'], 'e': ['L', 'RN'], 'f': ['L', 'RN'], 'g': ['L', 'RN'], 'h': ['L', 'RN'], 'i': ['L', 'RN'], 'j': ['L', 'RN'], 'k': ['L', 'RN'], 'l': ['L', 'RN'], 'm': ['L', 'RN'], 'o': ['L', 'RN'], 'p': ['L', 'RN'], 'q': ['L', 'RN'], 'r': ['L', 'RN'], 's': ['L', 'RN'], 't': ['L', 'RN'], 'u': ['L', 'RN'], 'v': ['L', 'RN'], 'w': ['L', 'RN'], 'x': ['L', 'RN'], 'y': ['L', 'RN'], 'z': ['L', 'RN'],
            'function': None,
            '(': None,
            ':': None,
            ';': None,
            'boolean': None,
            'string': None,
            ')': None
        },
        'RN': {
            'a': ['L', 'RN'], 'b': ['L', 'RN'], 'c': ['L', 'RN'], 'd': ['L', 'RN'], 'e': ['L', 'RN'], 'f': ['L', 'RN'], 'g': ['L', 'RN'], 'h': ['L', 'RN'], 'i': ['L', 'RN'], 'j': ['L', 'RN'], 'k': ['L', 'RN'], 'l': ['L', 'RN'], 'm': ['L', 'RN'], 'o': ['L', 'RN'], 'p': ['L', 'RN'], 'q': ['L', 'RN'], 'r': ['L', 'RN'], 's': ['L', 'RN'], 't': ['L', 'RN'], 'u': ['L', 'RN'], 'v': ['L', 'RN'], 'w': ['L', 'RN'], 'x': ['L', 'RN'], 'y': ['L', 'RN'], 'z': ['L', 'RN'],
            ')': ['empty'],
            'function': None,
            '(': None,
            ':': None,
            ';': None,
            'boolean': None,
            'string': None
        },
        'L': {
            'a': ['a'], 'b': ['b'], 'c': ['c'], 'd': ['d'], 'e': ['e'], 'f': ['f'], 'g': ['g'], 'h': ['h'], 'i': ['i'], 'j': ['j'], 'k': ['k'], 'l': ['l'], 'm': ['m'], 'n': ['n'], 'o': ['o'], 'p': ['p'], 'q': ['q'], 'r': ['r'], 's': ['s'], 't': ['t'], 'u': ['u'], 'v': ['v'], 'w': ['w'], 'x': ['x'], 'y': ['y'], 'z': ['z'],
            'boolean': ['boolean'],
            'string': ['string'],
            'function': None,
            '(': None,
            ':': None,
            ';': None,
            ')': None
        },
        'T': {
            'boolean': ['boolean'],
            'string': ['string'],
            'function': None,
            '(': None,
            ':': None,
            ';': None,
            ')': None
        },
        'LT': {
            ';': ['P', 'X', 'LT'],
            ')': ['empty'],
            'function': None,
            '(': None,
            ':': None,
            'boolean': None,
            'string': None
        },
        'P': {
            ';': [';'],
            'function': None,
            '(': None,
            ':': None,
            'boolean': None,
            'string': None,
            ')': None
        },
    }
    return terminals, non_terminals, table
