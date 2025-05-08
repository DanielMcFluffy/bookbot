def get_num_words(file_path):
    with open(file_path) as f:
        text = f.read()
        splitted_text = text.split()
        print(f"Found {len(splitted_text)} total words")

def get_word_occurences(text):
    lowercase_text = text.lower()
    occurences = dict()
    for char in lowercase_text:
        if char not in occurences:
            occurences[char] = 1
            continue
        occurences[char] += 1
    return occurences

def sort_dictionary(dictionary):
    _dictionary_list = []
    for key in dictionary:
        _dictionary_list.append({
            "char": key,
            "num": dictionary[key]
            })
    _dictionary_list.sort(reverse=True, key=lambda dic : dic["num"])
    return _dictionary_list

def process_file(file_path):
    with open(file_path) as file:
        text = file.read()
        sorted_dictionary = sort_dictionary(get_word_occurences(text))
        for x in sorted_dictionary:
            if not x["char"].isalpha():
                continue
            print(f"{x["char"]}: {x["num"]}")
