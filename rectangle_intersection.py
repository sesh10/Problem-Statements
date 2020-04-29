class Rectangle():
    def __init__(self, min_x=0, min_y=0, max_x=0, max_y=0):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y

def intersection_area(rect1, rect2):
    # Fill this in.
    if rect2.max_x > rect1.max_x and rect2.max_y < rect1.max_y:
        length = rect1.max_x - rect2.min_x
        breadth = rect2.max_y - rect1.min_y

    elif rect1.max_x >= rect2.max_x and rect1.max_y > rect2.max_y:
        length = rect2.max_x - rect1.min_x
        breadth = rect2.max_y - rect1.min_y
        
    elif rect1.max_x <= rect2.max_x and rect1.max_y < rect2.max_y:
        length = rect1.max_x - rect2.min_x
        breadth = rect1.max_y - rect2.min_y
        
    elif rect2.max_x < rect1.max_x and rect2.max_y > rect1.max_y:
        length = rect2.max_x - rect1.min_x
        breadth = rect1.max_y - rect2.min_y

    else:
        print('Error')
        
    return length*breadth


#  BBB
# AXXB
# AAA
rect2 = Rectangle(0, 0, 3, 2)
rect1 = Rectangle(1, 1, 3, 3)

print(intersection_area(rect1, rect2))
# 2
