from collections import Counter

# def word_count(args_str):
#     lower_args_str =  args_str.lower().split();
#     a_dict = {}
#     for substr in lower_args_str:
#         i = 0
#         while substr in lower_args_str:
#             if substr in lower_args_str:
#                 lower_args_str.remove(substr)
#                 i += 1
#         a_dict = {substr:i}
# 
#     return a_dict

def word_count(a_string):
    string_dict = {}
    for word in a_string.split():
        if word in string_dict:
            string_dict[word] += 1
        else:
            string_dict[word] = 1
    return string_dict


print(word_count("I am Shekhar , Shekhar is a good boy, and I am him a good boy"))