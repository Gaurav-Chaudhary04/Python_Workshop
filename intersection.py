my_set = {1,2,3,4}
my_set1 = {4,5,6,7,8}

def find_intersection(set1,set2):
    inter_set = set1.intersection(set2)
    return inter_set
    
intersection = find_intersection(my_set, my_set1)
print(intersection)