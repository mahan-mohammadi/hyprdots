def format_string(input_string):
    input_string = input_string.lower()
    punc_list = ['?' , '.' , '!' , ':' , "'"]
    for punc in punc_list:
        input_string = input_string.replace(punc , "")
    return input_string

def results(string_dict):
    for word,count in string_dict.items():
        print(f"{word} has appeared in the text {count} times")


input_string  = input("Enter your text: ")
formatted_string = format_string(input_string)

string_list = formatted_string.split(" ")
string_dict = {}

for s in string_list:
    string_dict.setdefault(s ,0)
    string_dict[s] += 1

sorted()
results(string_dict)

