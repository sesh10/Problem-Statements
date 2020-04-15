# You are given a hash table where the key is a course code, and the value is a list of all the course codes that are prerequisites for the key. 
# Return a valid ordering in which we can complete the courses. If no such ordering exists, return NULL.


def courses_to_take(course_all):
    # Fill this in.
    order = []
    for a in course_all.keys():
        if course_all[a] == [] and order == []:
            order.append(a)
    while len(order) != len(course_all):
        for a in course_all.keys():
            if (course_all[a] == order):
                if (a not in order):
                    order.append(a)
                
    return order
       
courses = {
  'CSC300': ['CSC100', 'CSC200'],
  'CSC200': ['CSC100'], 
  'CSC100': []
}
print(courses_to_take(courses))
# ['CSC100', 'CSC200', 'CSC300']
