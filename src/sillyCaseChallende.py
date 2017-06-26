def sillycase(arg):
    mid = int(len(arg)/2)
    
    new_args = (arg[:mid]).lower() + (arg[mid:]).upper()
    
    return new_args
    
    
    
print(sillycase("Shekhar"))