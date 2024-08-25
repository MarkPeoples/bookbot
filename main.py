def count_characters(s):
    letter_count = {}
    for char in s:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    filter_count = {key: value for key, value in letter_count.items() if key.isalpha()}
    return filter_count

def sort_by_count(item):
    return item['count']

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    # Count words
    words = file_contents.split()
    word_count = len(words)
    print(f"Total words: {word_count}")
    
    # Convert to lowercase and count characters
    all_lower = file_contents.lower()
    lowercase_count = count_characters(all_lower)
    char_count_list = [{'char': char, 'count': count} for char, count in lowercase_count.items()]
    sorted_char_list = sorted(char_count_list, key=sort_by_count, reverse=True)
    print(sorted_char_list)

main()
