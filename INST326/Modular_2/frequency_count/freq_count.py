import string

text = "to to to the the the be or not to be...."
word_count_dict = {}

def strip_punctuation(line):
    line = line.translate(str.maketrans('','',string.punctuation))
    return line

def counting(dictionary):
    for i in dictionary:
        i = i.lower()
        if i not in word_count_dict:
            word_count_dict[i] = 0
        word_count_dict[i] += 1


def order_dict (dictionary):
    sorted_values = []
    for key in dictionary:
        sorted_values.append((dictionary[key], key))
    sorted_values = sorted(sorted_values)
    sorted_values = sorted_values[::-1]
    return sorted_values

def main(text):
    strip_punctuation(text)
    strip_text = strip_punctuation(text)
    words = strip_text.split()
    counting(words)
    print(order_dict(word_count_dict))

if __name__ == "__main__":
    main(text)