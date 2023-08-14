 # """
 # test --> ation before tion
 # """
 #
# import pandas as pd
#
# pd.set_option('display.max_columns', None)
# pd.set_option('max_colwidth', None)
#
# # lt_brailleData = pd.read_csv(r'C:\Users\yang\Desktop\Coding\Braille-Translator\letters_braille.csv')
# # df_lt_brailleData = pd.DataFrame(lt_brailleData)
#
# ps_brailleData = pd.read_csv(r'C:\Users\yang\Desktop\Coding\Braille-Translator\prefix_suffix_braille.csv')
# df_ps_brailleData = pd.DataFrame(ps_brailleData)
#
# string = 'partition'
#
# prefix = string.startswith('part')
# suffix = string.endswith('tion')
#
# unicode_string = ''
# #
# # print(df_ps_brailleData['whole_word'])
# idx = 0
#
# for elem in df_ps_brailleData['partial_word']:
#     idx += 1
#     if string.endswith(elem):
#         prefix = df_ps_brailleData.iloc[idx - 1, 1]
#         suffix = df_ps_brailleData.iloc[idx - 1, 2]
#
#         unicode_string += chr(int(prefix))
#         unicode_string += chr(int(suffix))
#
#         string = string.replace(elem, '')
#
#         break
#
# print(string)
# print(unicode_string)
#
# # print(chr(10256))
# # print(chr(10255))
# # print(chr(10250))
# # print(chr(10288))
# # print(chr(10257))
#
# # if string.endswith()

"""
1. find letter in dataset
2. get unicode
3. check whole word abrv (len 5 first --> len 1), whole word, single words, partial_word, connect word, letter
"""
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

lt_brailleData = pd.read_csv(r'C:\Users\yang\Desktop\Coding\Braille-Translator\letters_braille.csv')
df_lt_brailleData = pd.DataFrame(lt_brailleData)

partial_brailleData = pd.read_csv(r'C:\Users\yang\Desktop\Coding\Braille-Translator\partial_word.csv')
df_partial_brailleData = pd.DataFrame(partial_brailleData)

whole_brailleData = pd.read_csv(r'C:\Users\yang\Desktop\Coding\Braille-Translator\whole_word.csv')
df_whole_brailleData = pd.DataFrame(whole_brailleData)


def checkWholeWord(string, unicode_string):
    # idx = 0
    # for elem in df_whole_brailleData['whole_word']:
    #     idx += 1
    #     if string.startswith(elem):
    #         prefix = df_whole_brailleData.iloc[idx - 1, 1]
    #         suffix = df_whole_brailleData.iloc[idx - 1, 2]
    #
    #         unicode_string += chr(prefix)
    #         unicode_string += chr(suffix)
    #
    #         string = string.replace(elem, '')
    #         break
    #
    # ans = [string, unicode_string]
    # return ans
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
    whole_unicode_string = ''
    partial_unicode_string = ''
    old_string = string.split()

    for word in old_string:
        idx_word_whole, whole_unicode_string = checkWholeWord(word)

        idx_word_partial, partial_unicode_string, elem = checkPartialWord(word)

        if idx_word_partial >= 0 and idx_word_whole >= 0:
            list_letter = string

            for i in list_letter:
                if list_letter.find(i) == idx_word_whole:
                    unicode_string += whole_unicode_string
                    list_letter = list_letter.replace(elem, '')

                elif list_letter.find(i) == idx_word_partial:
                    unicode_string += partial_unicode_string
                    list_letter = list_letter.replace(elem, '')

                else:
                    letterBooleanList = df_lt_brailleData['letter'] == i
                    letter_data = df_lt_brailleData.loc[letterBooleanList]
                    letter_unicode = letter_data['unicode']
                    braille_char = chr(letter_unicode)
                    unicode_string += braille_char

        elif idx_word_partial < 0 and idx_word_whole >= 0:
            list_letter = string

            for i in list_letter:
                if list_letter.find(i) == idx_word_whole:
                    unicode_string += whole_unicode_string
                    list_letter = list_letter.replace(elem, '')

                else:
                    letterBooleanList = df_lt_brailleData['letter'] == i
                    letter_data = df_lt_brailleData.loc[letterBooleanList]
                    letter_unicode = letter_data['unicode']
                    braille_char = chr(letter_unicode)
                    unicode_string += braille_char

        elif idx_word_partial >= 0 and idx_word_whole < 0:
            list_letter = string

            for i in list_letter:
                if list_letter.find(i) == idx_word_partial:
                    unicode_string += partial_unicode_string
                    list_letter = list_letter.replace(elem, '')

                else:
                    letterBooleanList = df_lt_brailleData['letter'] == i
                    letter_data = df_lt_brailleData.loc[letterBooleanList]
                    letter_unicode = letter_data['unicode']
                    braille_char = chr(letter_unicode)
                    unicode_string += braille_char

        else:
            letterBooleanList = df_lt_brailleData['letter'] == i
            letter_data = df_lt_brailleData.loc[letterBooleanList]
            letter_unicode = letter_data['unicode']
            braille_char = chr(letter_unicode)
            unicode_string += braille_char

            unicode_string += chr(10240)

    return unicode_string


print(translate('partition hi'))


