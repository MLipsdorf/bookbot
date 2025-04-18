def get_num_words(filepath):
    num = 0
    word_list = []
    with open(filepath) as f:
        content = f.read()
        word_list = content.split()
        for words in word_list:
            num +=1
    return num

def count_chars(filepath):
    count_dict = {}
    word_list = []

    with open(filepath) as f:
        content = f.read()
        word_list = [words.lower() for words in content.split()]
        for i in range(0,len(word_list)):
            for char in word_list[i]:
                if char not in count_dict:
                    count_dict[char] = 1
                else:
                    count_dict[char] +=1
    return count_dict

def get_second_element(x):
    return x[1]

def create_report(count_dict,filepath, num):
    dict_list = list(count_dict.items())
    sorted_data = sorted(dict_list, key=get_second_element, reverse=True)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    for item in dict_list:
        print(f"{item[0]}: {item[1]}")
    

    