input_file = open("text.txt", "r")

text = input_file.read()

text = text.replace ("\n"," ")

word_list = text.split(" ")

for word in word_list:
    word_2 = ""
    for i in range(len(word)):
        if word[i].isalpha():
            word_2 += word[i].lower()

    word_list[word_list.index(word)] = word_2

while '' in word_list:
    word_list.remove('')

word_dict = {}
for word in word_list:
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] +=1

for word in word_dict:
    print(word, word_dict[word])

input_file.close()