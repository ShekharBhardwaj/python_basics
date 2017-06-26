# COURSES = {
#     "Python Basics": {"Python", "functions", "variables",
#                       "booleans", "integers", "floats",
#                       "arrays", "strings", "exceptions",
#                       "conditions", "input", "loops"},
#     "Java Basics": {"Java", "strings", "variables",
#                     "input", "exceptions", "integers",
#                     "booleans", "loops"},
#     "PHP Basics": {"PHP", "variables", "conditions",
#                    "integers", "floats", "strings",
#                    "booleans", "HTML"},
#     "Ruby Basics": {"Ruby", "strings", "floats",
#                     "integers", "conditions",
#                     "functions", "input"}
# }
# 
# 
# 
# # for k,v in COURSES.items():
# #     print(v)
# 
# print(set("oklahoma") & set("ohio"))

# 
# TILES = ('-', ' ', '-', ' ', '-', '||',
#          '_', '|', '_', '|', '_', '|', '||',
#          '&', ' ', '_', ' ', '||',
#          ' ', ' ', ' ', '^', ' ', '||'
# )
# 
# for tile in TILES:
#     end_line = ""
#     if tile != "||":
#         output = tile
#     else:
#         end_line = "\n"
#     print(tile, end=end_line)