leet = {
    "1": "i",
    "3": "e",
    "4": "a",
    "5": "s",
    "7": "t",
    "0": "o",
    "@" :"a",
    "/\ ": "a",
    "/-\ ": "a",
    "*" : "a",
    "ä" : "a",
    "á" :"a",
    "à" : "a",
    "â" : "a",
    "a^": "a",
    "ã" : "a",
    "å" : "a",
    "ą" : "a",
    "ª" : "a",
    "∀" : "a",
    "∧" : "a",
    "α" : "a",
    "8" : "b",
    "|3": "b",
    "13": "b",
    "ß" : "b",
    "þ" : "b",
    "ć" : "c",
    "č" : "c",
    "ç" : "c",
    "©" : "c",
    "σ" : "c",
    "(" : "c",
    "¢" : "c",
    "<" : "c",
    '[' : "c",
    '©': "c",
    "[)" : "d",
    "|>" : "d",
    "|)" : "d",
    "|]": "d",
    "3" : "e",
    "€" : "e",
    "є" : "e",
    "[-": "e",
    "|=" : "f",
    "ƒ" : "f",
    "/=": "f",
    "6" : "g",
    "(_+": "g",
    "#" : "h",
    "/-/" : "h",
    "[-]" : "h",
    "]-[" : "h",
    ")-(" : "h",
    "(-)" : "h",
    ":-:" : "h",
    "|~|" : "h",
    "|-|" : "h",
    "]~[" : "h",
    "}{" : "h",
    # "1" : "i",
    '!' : "i",
    # "|" : "i",
    # "][" : "i",
    # "]" : "i",
    # ":": "i",
    "_|" : "j",
    "_/" : "j",
    "¿" : "j",
    "(/" : "j",
    "ʝ" : "j",
    ";" : "j",
    "X" : "k",
    "|<" : "k",
    "|{" : "k",
    "ɮ" : "k",
    "£" : "l",
    "1_" : "l",
    "ℓ" : "l",
    "|_" : "l",
    "[_": "l",
    "|V|" : "m",
    "|\/|" : "m",
    "/\/\ " : "m",
    "/V\ ": "m",
    "|V" : "n",
    "|\|" : "n",
    "/\/" : "n",
    "[\]" : "n",
    "/V" : "n",
    "[]" : "o",
    "0" :"o" ,
    "()" : "o",
    "°" : "o",
    "|*" : "p",
    "|o" : "p",
    "|º" : "p",
    "|°" : "p",
    "/*" : "p",
    "¶" : "q",
    "(_,)" : "q",
    "()_" : "q",
    "0_" : "q",
    "°|" : "q",
    "<|" : "q",
    "®" : "r",
    "2" : "r",
    "|?" : "r",
    "/2" : "r",
    "®" : "r",
    "Я" : "r",
    "|2": "r",
    "§" : "s",
    "5" : "s",
    "$" : "s",
    "_/¯": "s",
    "7" : "t",
    "†" : "t",
    "¯|¯" : "t",
    "(_)" : "u",
    "|_|" : "u",
    "L|" : "u",
    "µ": "u",
    "\/" : "v",
    "|/" : "v",
    "\/\/" : "w",
    "vv" : "w",
    "\//" :"w",
    "\^/" : "w",
    "\V/" : "w",
    "\|/" : "w",
    "\_|_/" : "w",
    "\_:_/" : "w",
    "><": "x",
    "}{" : "x",
    "×" : "x",
    ")(" : "x",
    " `/" : "y",
    "φ" : "y",
    "¥" : "y",
    "\/": "y",
    "≥" : "z",
    "7_" : "z",
    ">_": "z"
}


# word = 'h@l g@gO'

# word.lower()

def leet_conver(word):
    word = word.lower()
    newval = ""
    for char in word:

        if char in leet:
            newval+= leet[char]

        else:
            newval+= char
    return(newval)

