def encode_morze(text):

    morse_code = {
    "A" : ".-", "B" : "-...", "C" : "-.-.", "D" : "-..", "E" : ".", "F" : "..-.",
    "G" : "--.", "H" : "....", "I" : "..", "J" : ".---", "K" : "-.-",
    "L" : ".-..", "M" : "--", "N" : "-.", "O" : "---", "P" : ".--.",
    "Q" : "--.-", "R" : ".-.", "S" : "...", "T" : "-", "U" : "..-",
    "V" : "...-", "W" : ".--", "X" : "-..-", "Y" : "-.--", "Z" : "--.."
    }

    diagrama = {"A" : "^_^^^", "B" : "^^^_^_^_^", "C" : "^^^_^_^^^_^", "D" : "^^^_^_^",
             "E" : "^", "F" : "^_^_^^^_^", "G" : "^^^_^^^_^", "H" : "^_^_^_^",
             "I" : "^_^", "J" : "^_^^^_^^^_^^^", "K" : "^^^_^_^^^", "L" : "^_^^^_^_^",
             "M" : "^^^_^^^", "N" : "^^^_^", "O" : "^^^_^^^_^^^", "P" : "^_^^^_^^^_^",
             "Q" : "^^^_^^^_^_^^^", "R" : "^_^^^_^", "S" : "^_^_^", "T" : "^^^",
             "U" : "^_^_^^^", "V" : "^_^_^_^^^", "W" : "^_^^^_^^^", "X" : "^^^_^_^_^^^",
             "Y" : "^^^_^_^^^_^^^", "Z" : "^^^_^^^_^_^"
              }

    l = [];
    s = '';
    text = text.upper();

    for i in text:
        if i in diagrama:
            l.append(diagrama.get(i));
        elif i == ' ':
            l.append('_');

    s = '___'.join(l);
    return s;