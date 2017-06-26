
def packer(somegarbage=None,**kwargs):
    print(kwargs)
    

def un_packer(firstname=None, lastname=None):
    if firstname and lastname:
        print("Hi {} {} , Welcome!".format(firstname, lastname))
    else:
        print("Hello person with no name")
        
    
    
    
#packer(hello="world", some_list=[1,2,3,4,5], somegarbage="adasdasdasdadqdqwd")
un_packer(**{"firstname" : "Shekhar", "lastname": "bhardwaj"})