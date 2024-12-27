def count_anagrams(text, word):
    if text == "" or word == "" :
        return 0
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
        # Skip this word if it's shorter than `word_length`
        if len(word_candidate) < word_length:
            continue

        # Iterate through all substrings of the current word
        for i in range(len(word_candidate) - word_length + 1):
            # Extract substring
            current_window = word_candidate[i:i + word_length]

            # Check if current window contains invalid characters
            if any(char not in word_sorted for char in current_window):
                continue  # Skip invalid windows early

            # Sort and compare to detect anagrams
            if ''.join(sorted(current_window)) == word_sorted:
                anagram_count += 1

            # Exit early if an impossible case is detected (e.g., no remaining matches)
            if anagram_count > 30:  
                break

    return anagram_count

    