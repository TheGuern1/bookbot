import sys
from stats import get_num_words, get_book_text, get_char_frequency, sorted_list

def main():
   if len(sys.argv) !=2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)
   else:
      book_path = sys.argv[1]
      text = get_book_text(book_path)
      num_words = get_num_words(text)
      print("============ BOOKBOT ============")
      print(f"Analyzing book found at {book_path}...")
      print("----------- Word Count ----------")
      print("Found", num_words, "total words")
      print("--------- Character Count -------")	
      char_freq = sorted_list(text)
      for char, count in char_freq:
           print(f"{char}: {count}")
      print("============= END ===============")
	
main()
