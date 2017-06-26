def num_teachers(dict_teachers):
    i = 0
    for key in dict_teachers:
        i += 1
    return i

def num_courses(dict_teachers):
    i = 0
    for value in dict_teachers.values():
        i += len(value)
    return i

def courses(dict_teachers):
    course_list = []
    for value in dict_teachers.values():
        course_list += value
    
    return course_list
    
def most_courses(dict_teachers):
    key_list = []
    dict_most_subs={}
    for key in dict_teachers.keys():
        dict_most_subs={len(dict_teachers.get(key)):key}
    
    for key in dict_most_subs:
        key_list.append(key)
        
    return dict_most_subs.get(max(key_list))
        

def most_courses_1(dict_teachers):
    max_subs = 0
    max_sub_teacher = ""

    for teacher, course_list in dict_teachers.iteritems():
        if len(course_list) > max_subs:
            max_subs = len(course_list)
            max_sub_teacher = teacher
    return max_sub_teacher


def stats(dict_teachers):
    teach_n_subj_list = []
    for teacher, course_list in dict_teachers.items():
        temp_list=[teacher, len(course_list)]
        teach_n_subj_list.append(temp_list)
    return teach_n_subj_list
        
    
        
        
example = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],'Kenneth Love': ['Python Collections', 'Some subject']}
#print(num_teachers(example))

#print(num_courses(example))

#print(courses(example))

#print(most_courses_1(example))

print(stats(example))
