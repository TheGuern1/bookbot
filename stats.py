
def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words    

def get_char_frequency(text):
   text = text.lower()
   freq = {}

   for char in text:
      if char in freq:
         freq[char] += 1
      else:
         freq[char] =1
   return freq

def sorted_list(text):
    freq_dict = get_char_frequency(text)  # get frequency dictionary
    sorted_freq = sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_freq
