#word count

def words(word_list):
    spaces=""
    word_dict = {}
    if "\n" in word_list:                       #check for:
          word_list=word_list.replace("\n"," ") #          newlines
    if "\t" in word_list:                       #          tabs
      word_list = word_list.replace("\t"," ")   #         and remove them by replacing with a space
    word_list=word_list.split(" ")
    for word in word_list:
        try: #if the word is convertable to an int run the word count and keep it as int in dictionary
            if word in word_dict:
                word_dict[int(word)] = word_dict[int(word)] + 1
            else:
                word_dict[int(word)] = 1
        except ValueError: #string types cause value errors so will be kept as str tpye in dictionary
            if word in word_dict:
                word_dict[str(word)] = word_dict[str(word)] + 1
            else:
                word_dict[str(word)] = 1
    if spaces in word_dict:
      del word_dict[spaces] # remove space count in dictionary
    return word_dict