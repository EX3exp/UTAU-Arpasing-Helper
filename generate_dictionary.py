import cmudict
import pickle


cmu_dict = cmudict.dict()

def check_phonemes_with_ax(pronunciations_from_cmudict: list) -> list:
    '''make cmudict's phonemes to be same as UTAU Arpasing's phonemes.'''
    #check each phonemes have integer part, and deletes it if exists.
    return [pronunciation_.lower().strip() if pronunciation_[-1].isalpha() or pronunciation_ == 'AH0' else pronunciation_[:-1].lower().strip() for pronunciation_ in pronunciations_from_cmudict]


def check_phonemes_without_ax(pronunciations_from_cmudict: list) -> list:
    '''make cmudict's phonemes to be same as UTAU Arpasing's phonemes.'''
    #check each phonemes have integer part, and deletes it if exists.
    return [pronunciation_.lower().strip() if pronunciation_[-1].isalpha() else pronunciation_[:-1].lower().strip() for pronunciation_ in pronunciations_from_cmudict]


def check_word(word_from_cmudict: str) -> str:
    '''make cmudict's words do not start with exclamation mark.'''
    #check word starts with exclamation mark, and deletes it if exists.
    if word_from_cmudict[0].isalpha(): 
        return word_from_cmudict.lower().strip() 
    else: return word_from_cmudict[1:].lower().strip()
    

def save_ax_dict():
    #initialize a dict to load every words&pronunciations in cmudict.
    phoneme_dictionary = {}

    #load every words&pronunciations in cmudict, and make them same as UTAU Arpasing Style.
    for word, pronunciations in cmu_dict.items():
        phoneme_dictionary[check_word(word)] = check_phonemes_with_ax(pronunciations[0])

    #save as binary file (DICT_AX).
    with open('DICT_AX', 'wb') as f:
        pickle.dump(phoneme_dictionary, f)

    print(f">>> Successfully saved binary file(A), with {len(phoneme_dictionary)} words.")

def save_no_ax_dict():
    #initialize a dict to load every words&pronunciations in cmudict.
    phoneme_dictionary = {}

    #load every words&pronunciations in cmudict, and make them same as UTAU Arpasing Style.
    for word, pronunciations in cmu_dict.items():
        phoneme_dictionary[check_word(word)] = check_phonemes_without_ax(pronunciations[0])

    #save as binary file (DICT).
    with open('DICT', 'wb') as f:
        pickle.dump(phoneme_dictionary, f)

    print(f">>> Successfully saved binary file(B), with {len(phoneme_dictionary)} words.")

def main():
    save_ax_dict()
    save_no_ax_dict()

if __name__ == "__main__":
    main()
    