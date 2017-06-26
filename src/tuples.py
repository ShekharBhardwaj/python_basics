from scipy.weave.c_spec import tuple_converter
def add(base, *args):
    total = base
    for num in args:
        total += num
    
    return total

def multiply(*args):
    product = 1
    for num in args:
        product *= num
        
    return product

def stringcases(str_):
    str_1 = str_.upper()
    str_2 = str_.lower()
    str_3 = str_.title()
    str_4 = str_[::-1]
     
    return (str_1, str_2, str_3, str_4)

def combo(list_iter, str_iter):
    tuple_list=[]
    count = 0
    for item in list_iter:
        tuple_list.append((list_iter[count], str_iter[count]))
        count += 1
    
    return tuple_list
        
    
    
def combo_1(iterable_1, iterable_2):
    list_of_tuples = []
    count = 0
    for item in iterable_1:
        list_of_tuples.append((iterable_1[count], iterable_2[count]))
        count += 1
    return list_of_tuples
#print(add(1,1))

#print(multiply(2,3,4,5))

#print(stringcases("My name is slim shady"))

my_list = [1, 2, 3]
my_str = "abc"

print(combo(my_list, my_str))
