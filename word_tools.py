def count_anagrams(text, word):
    if not text or not word or len(word) > len(text):  # Handle edge cases
        return 0

    # Preliminary check: If any character in `word` is not in `text`, return 0
    if not all(char in text for char in set(word)):
        return 0

    word_length = len(word)
    word_sorted = ''.join(sorted(word))  # Pre-sort the word for comparison
    anagram_count = 0

    # Split the text into words and process each word separately
    words = text.split()

    for word_candidate in words:
        # Iterate through all substrings of the current word
        for i in range(len(word_candidate) - word_length + 1):
            current_window = word_candidate[i:i + word_length]
            if ''.join(sorted(current_window)) == word_sorted:  # Check if it's an anagram
                anagram_count += 1

    return anagram_count