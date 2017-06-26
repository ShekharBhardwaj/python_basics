import os
import sys



def clear():
    os.system("cls" if os.name == "nt" else "clear")
    

def show_list(user_list):
    clear()
    
    i =1
    for item in user_list:
        str1 = ''.join(item)
        print("{}, {}".format(i,str1))
        i += 1
    print("-"*10)
        
def keywords(key, user_list):
    
    if key.upper() == "HELP":
        print("""
        This is a shopping program.
        you can type  QUIT to get out
        or DONE when your list is over
        
        """)
        
    if key.upper() == "QUIT":
        sys.exit()
        
    if key.upper() == "DONE":
        if not user_list:
            print("No item in the list.")
        else:
            show_list(user_list)
            sys.exit()

        
        
    

def add_item_to_list(user_list):
    
    item = raw_input("Your item? ")
    if item.upper() == "DONE" or item.upper() == "QUIT" or item.upper() == "HELP":
        keywords(item, user_list)
    else:
    
        if not user_list:
            user_list += item
        else:
            position = input("Which position you want this {} to be saved".format(item))
    
        try:
            real_index = abs(int(position))
            user_list.insert(real_index, item)
        except:
            user_list += item
                
        show_list(user_list)
    
    
    
def shopping_list():
    
    user_list =[]
    
    while True:
        add_item_to_list(user_list)
        
        
shopping_list()
        
    