from collections import Counter
def find_most_frequent(text):

    newWords = []
    text = text.lower()
    text = text.replace(',', ' ')
    text = text.replace('...', '')
    text = text.replace('!', '')
    text = text.replace('-', ' ')
    text = text.replace('?', '')
    text = text.replace(':', '')
    text = text.replace(';', '')
    text = text.replace('.', '')
    text = text.replace('  ', ' ')
    text = text.replace('   ', ' ')
    text = text.replace('    ', ' ')
    text = text.split(' ')

    if " " in text:
            text.remove(" ")

    count = Counter(text)

    maximum = max(count.values())

    for k, v in count.items():
        if v == maximum:
            newWords.append(k)

    if '' in newWords:
        delit = list(newWords.pop())
        return delit
    else:
        return newWords