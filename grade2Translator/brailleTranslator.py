"""
1. find letter in dataset
2. get unicode
3. check whole word abrv (len 5 first --> len 1), whole word, single words, partial_word, connect word, letter
"""
import pandas as pd
import string

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

lt_brailleData = pd.read_csv(r'letters_braille.csv')
df_lt_brailleData = pd.DataFrame(lt_brailleData)

partial_brailleData = pd.read_csv(r'partial_word.csv')
df_partial_brailleData = pd.DataFrame(partial_brailleData)

whole_brailleData = pd.read_csv(r'whole_word.csv')
df_whole_brailleData = pd.DataFrame(whole_brailleData)

abr5_brailleData = pd.read_csv(r'alternate meanings - abr5.csv')
df_abr5_brailleData = pd.DataFrame(abr5_brailleData)

abr4_brailleData = pd.read_csv(r'alternate meanings - abr4.csv')
df_abr4_brailleData = pd.DataFrame(abr4_brailleData)

abr3_brailleData = pd.read_csv(r'alternate meanings - abr3.csv')
df_abr3_brailleData = pd.DataFrame(abr3_brailleData)

abr2_brailleData = pd.read_csv(r'alternate meanings - abr2.csv')
df_abr2_brailleData = pd.DataFrame(abr2_brailleData)

numData = dict(digits=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])


def wholeStrUpperCase(string, unicode_string):
    capital_char = chr(10272)
    unicode_string += capital_char
    unicode_string += capital_char
    string = string.lower()

    return string, unicode_string


def checkWholeWord(string, unicode_string):
    idx = 0
    for elem in df_whole_brailleData['whole_word']:
        idx += 1
        if string.startswith(elem):
            prefix = df_whole_brailleData.iloc[idx - 1, 1]
            suffix = df_whole_brailleData.iloc[idx - 1, 2]

            unicode_string += chr(prefix)
            unicode_string += chr(suffix)

            string = string.replace(elem, '')
            break

    ans = [string, unicode_string]
    return ans


def checkPartialWord(string):
    idx = 0
    idx_word = -1
    found_unicode_string = ''
    found_elem = ''
    for elem in df_partial_brailleData['partial_word']:
        idx += 1

        if elem in string and elem[0] != string[0]:
            # find idx of elem in string
            idx_word = string.find(elem)
            prefix = df_partial_brailleData.iloc[idx - 1, 1]
            suffix = df_partial_brailleData.iloc[idx - 1, 2]

            found_unicode_string = chr(int(prefix)) + chr(int(suffix))

            # string = string.replace(elem, '')
            found_elem = elem
            break

    ans = [idx_word, found_unicode_string, found_elem]
    return ans


def translate(string):
    unicode_string = ''
    old_string = string.split()

    for word in old_string:

        if word.isupper():
            word, unicode_string = wholeStrUpperCase(word, unicode_string)

        newString, unicode_string = checkWholeWord(word, unicode_string)

        # DECIMALS: numSign 20 DecimalSign 1
        # for isNumber = True --> if see "." --> decimalSign

        # also in middle of word and suffix

        idx_word_partial, partial_unicode_string, elem = checkPartialWord(word)

        if idx_word_partial >= 0:
            list_letter = list(newString)

            isNum = False

            for i in list_letter:
                if i.isupper():
                    capital_char = chr(10272)
                    unicode_string += capital_char
                    i = i.lower()

                if i in numData['digits']:
                    numSign_char = chr(10300)
                    unicode_string += numSign_char

                    letterBooleanList = df_lt_brailleData['letter'] == i
                    letter_data = df_lt_brailleData.loc[letterBooleanList]
                    letter_unicode = letter_data['unicode']
                    braille_char = chr(letter_unicode)
                    unicode_string += braille_char

                    isNum = True

                    if list_letter.find(i) == idx_word_partial:
                        unicode_string += partial_unicode_string
                        list_letter = list_letter.replace(elem, '')

                else:
                    if isNum:
                        letterSign_char = chr(10288)
                        unicode_string += letterSign_char

                    letterBooleanList = df_lt_brailleData['letter'] == i
                    letter_data = df_lt_brailleData.loc[letterBooleanList]
                    letter_unicode = letter_data['unicode']
                    braille_char = chr(letter_unicode)
                    unicode_string += braille_char

            unicode_string += chr(10240)

        else:
            letterBooleanList = df_lt_brailleData['letter'] == i
            letter_data = df_lt_brailleData.loc[letterBooleanList]
            letter_unicode = letter_data['unicode']
            braille_char = chr(letter_unicode)
            unicode_string += braille_char

    return unicode_string
