template = "Hi, I'm {name} and I love to eat {food}!"

def string_factory(list_of_dict):
    new_list = []
    for dictn in list_of_dict:
        new_list.append(template.format(**dictn))
    return new_list


dict_list = [{"name":"Shekhar", "food":"Pizza"}, {"name":"Ruth", "food":"Pasta"}, {"name":"Troy", "food":"Pie"}]

print(string_factory(dict_list))
