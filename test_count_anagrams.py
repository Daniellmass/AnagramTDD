from word_tools import count_anagrams  # Import the function to be tested
import pytest

# Parameterized tests for different cases
@pytest.mark.parametrize("text, word, expected_result", [
    ("", "abc", 0),                   # Empty text
    ("abc", "", 0),                   # Empty word
    (None, "abc", 0),                 # None as text
    ("abcabc", "abc", 2),             # Multiple anagrams in the text
    ("abcd", "abc", 0),               # No anagrams in the text
    ("aabbcc", "abc", 0),             # Not enough letters to form an anagram
    ("bcaacb", "abc", 2),             # Two anagrams with mixed order
    ("abcabcabc", "abc", 3),          # Consecutive anagrams
    ("abcdefgh", "hgf", 0),           # Word with no matching letters in the text
    ("cbaebabacd", "abc", 2)          # Complex case with two anagrams
])
def test_count_anagrams(text, word, expected_result):
    assert count_anagrams(text, word) == expected_result

# Performance test
def test_performance_count_anagrams():
    import time
    text = "a" * 1000000 + "abc"  # A very large text with one anagram at the end
    word = "abc"
    start_time = time.time()
    result = count_anagrams(text, word)
    end_time = time.time()
    assert end_time - start_time < 1, "Performance test failed!"  # Ensure execution time < 1 second
    assert result == 1