from stats import get_num_words
from stats import get_num_characters
from stats import get_sorted_list
import sys




def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
		return file_contents

def main():

	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_path = sys.argv[1]


	contents = get_book_text(book_path)
	count_words = get_num_words(contents)
	count_characters = get_num_characters(contents)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at ...{book_path}")
	print("----------- Word Count ----------")
	print(f"Found {count_words} total words")
	print("--------- Character Count -------") 
	sorted_list = get_sorted_list(count_characters)
	for entry in sorted_list:
		print (f"{entry['char']}: {entry['num']}") 
	print("============= END ===============")
main()
