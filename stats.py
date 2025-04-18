def get_num_words(text):
	words = text.split()
	word_count = len(words)
	return word_count

def character_count(text):
	counts = {}
	text = text.lower()
	for char in text:
		if char in counts:
			counts[char] += 1
		else:
			 counts[char] = 1
	return counts

def sort_list(char_counts):
	char_list = []
	for char, count in char_counts.items():
		char_dict = {"char": char, "count": count}
		char_list.append(char_dict)

	char_list.sort(reverse=True, key=lambda x: x["count"])

	return char_list
