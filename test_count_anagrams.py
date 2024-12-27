from word_tools import count_anagrams 
def test_empty_text():
  assert count_anagrams("", "abc") == 0