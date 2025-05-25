def get_num_words(contents):
        return len(contents.split())

def get_num_characters(contents):
	character_count = {}
	for character in contents:
		l_character = character.lower()
		if l_character in character_count:
			character_count[l_character] += 1
		else:
			character_count[l_character] = 1
	return character_count

def get_sorted_list(count_characters):
	sorted_list = []

	for character in count_characters:
		sorted_list.append ({"char": character, "num": count_characters[character]})
	sorted_list.sort(reverse=True, key=lambda x: x["num"])
	return sorted_list
