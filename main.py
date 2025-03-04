import sys
if len(sys.argv) < 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

from stats import word_count
from stats import char_count
from stats import sort_on
from stats import create_list
from stats import clean_list
filepath = sys.argv[1]
def get_book_text(filepath):
	with open(filepath) as f:
		file_text = f.read()
	return file_text

def main():
	text = get_book_text(filepath)
	count = word_count(text)
	char = char_count(text)
	create = create_list(char)
	sort = create.sort(reverse=True, key=sort_on)
	clean = clean_list(create)
	print("============ BOOKBOT ============\n")
	print(f"Analyzing book found at {filepath}\n")
	print("----------- Word Count ----------\n")
	print(f"Found {count} total words\n")
	print("--------- Character Count -------\n")
	print('\n'.join(clean))
	print("============= END ===============")

main()