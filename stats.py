def word_count(text):
        split_text = text.split()
        word_count = 0
        for word in split_text:
                word_count += 1
        return word_count

def char_count(text):
        characters = {}
        for char in text:
                lower = char.lower()
                if lower in characters:
                        characters[lower] += 1
                else:
                        characters[lower] = 1
        return characters

def sort_on(dict):
        return dict["num"]

def create_list(dict):
        letters = []
        for char in dict:
                if char.isalpha() == True:
                        letter = {"letter": char, "num": dict[char]}
                        letters.append(letter)
        
        return letters

def clean_list(list):
        letters_clean = []
        for i in range(0, len(list)):
                letter = list[i]["letter"]
                num = list[i]["num"]
                letters_clean.append(f"{letter}: {num}\n")

        return letters_clean