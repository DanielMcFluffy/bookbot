    
def main():
    characters = {}
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        splitted_contents = list(file_contents.lower())
        
        for t in splitted_contents:
            if t.isalpha() == False:
                continue
            if t not in characters:
                characters[t] = 1
            else:
                characters[t] += 1
        print(characters)
    print("--- Begin report of books/frankestein.txt ---")
    print(f"{len(file_contents.split())} words found in the document")
    print()
    for c in characters:
        print(f"The {c} character was found {characters[c]} times")
    print("--- End report ---")
main()
