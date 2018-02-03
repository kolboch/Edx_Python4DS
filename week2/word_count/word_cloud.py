from operator import itemgetter


# defining function before call, using it later
def replace_with_space(s, replace):
    return s.replace(replace, "")


# opening file with our text
file = open("98-0.txt", "r", encoding="utf-8")

# reading lines and splitting, default white space character is separator
words_list = []
for line in file:
    words_list.extend(line.lower().split())

# characters to replace
to_replace_list = [",", "'", "’", ";", "‘", ".", "“", "\\", "\"", "/", "”", "?", "!", "#", "(", ")", "*", "=", "+", "_",
                   ":"]

word_dict = {}
# word replacing and counting
for word in words_list:
    for to_replace in to_replace_list:
        word = replace_with_space(word, to_replace)
    if word_dict.get(word) is None:
        word_dict[word] = 1
    else:
        word_dict[word] += 1

# dictionary to list
counted_words = word_dict.items()

# sorting
sorted_by_count = sorted(counted_words, key=itemgetter(1), reverse=True)
for i in range(0, 10):
    print("{} {}".format(sorted_by_count[i][0], sorted_by_count[i][1]))
