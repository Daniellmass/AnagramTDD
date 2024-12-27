from word_tools import count_anagrams  # Import the function to be tested
import pytest

# Parameterized tests for continuous strings
@pytest.mark.parametrize("text, word, expected_result", [
    ("", "listen", 0),                        # Empty text
    ("listen", "", 0),                        # Empty word
    (None, "listen", 0),                      # None as text
    ("listenlisten", "listen", 7),            # Exact match repeated in text
    ("forxxorfxdofr", "for", 3),              # Multiple anagrams in the text
    ("abcdefabcdef", "abc", 2),               # Multiple anagrams in the text
    ("aabaabaa", "aaba", 4),                  # Overlapping anagrams
    ("abcde", "xyz", 0),                      # No anagrams in the text
    ("thequickbrownfoxjumps", "brown", 1),    # Single anagram in continuous text
    ("railfairesafetytales", "fairy", 0),     # Single match within continuous text
    ("abcdefghijklmnopqrst", "mnopq", 1)      # Single anagram match
])
def test_count_anagrams(text, word, expected_result):
    assert count_anagrams(text, word) == expected_result

# Performance test with a large input
def test_performance_count_anagrams():
    import time
    text = "a" * 1000000 + "listen"  # A very large text with one anagram at the end
    word = "listen"
    start_time = time.time()
    result = count_anagrams(text, word)
    end_time = time.time()
    assert end_time - start_time < 1, "Performance test failed!"  # Ensure execution time < 1 second
    assert result == 1