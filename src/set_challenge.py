COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}


def covers(set_of_topics):
    
    list_of_courses = []
    for topic in set_of_topics:
        
        for k,v in COURSES.items():
            if topic in v:
                list_of_courses.append(k)
    return list_of_courses

def covers_all(set_of_topics):
    list_of_courses = []
    for k,v in COURSES.items():
        intersect_set = set_of_topics & v
            
        if intersect_set == set_of_topics:
            list_of_courses.append(k) 
    return list_of_courses
                

        
        
        
        
        
print(covers_all({"conditions", "input"}))  

#print (covers({"Python", "Ruby"}))
            
        
    