def print_report(path, word_count, character_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for item in character_counts:
        print(f"{item["char"]}: {item["num"]}")