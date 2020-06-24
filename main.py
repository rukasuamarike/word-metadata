# USE .TXT FILES FOR EXTRACT AND SAVE FILES

import sys

def no_symbols(word):  # removes non-alpha characters
    char: chr
    res = ""
    for char in word:
        if char.isalpha():
            res += char
    return res


def word_totals(filename): # creates a dictionary of words from the file and how many times it is in the file
    result = {}
    with open(filename, 'r') as f:
        for line in f:
            words = line.strip().split(' ')
            for word in words:
                word = no_symbols(word)
                if word in result:
                    result[word] += 1
                else:
                    result[word] = 1

    return result


def included(word, wlist):
    res = True
    for w in wlist:
        if w == word and wlist[word] == 0:
            res = False
    return res


def sort_alpha(dict):
    res = {}
    res = sorted(dict.items())
    return res


def sort_value(dict):
    res = {}
    res = reversed(sorted(dict.items(), key=lambda item: item[1]))
    return res


def printer(dict):
    val = {}
    res = "{"
    for key in dict:
        res += "[{},{}], ".format(key[0], key[1])

    return res + "}"


def save_file(file, content): # saves the dict to a txt file
    with open(file, 'a') as f:
        for key in content:
            f.write("{}:{}\n".format(key, int(content[key])))
        f.close()


def main():
    run = True # runs while true
    file = input("[extract file] filename: ")
    out = word_totals(file)
    print(word_totals(file))
    while run:
        cmd = input('what next? ([sort],[savefile],[end])')

        if cmd == 'end': # stops program
            run = False

        if cmd == 'sort': # sorting options for dict
            arg = input("sort by what? ([alpha],[value])")
            if arg == 'alpha':
                out = sort_alpha(out)
                print(printer(out))
            if arg == 'value':
                out = sort_value(out)
                print(printer(out))

        if cmd == 'savefile': # gives option to choose save location
            savefile = input("[save file] filename:")
            save_file(savefile, out)


if __name__ == '__main__':
    main()
