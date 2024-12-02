from collections import Counter

def get_lists():
    list1 = []
    list2 = []

    with open("input", 'r') as file:
        for line in file:
            sections = line.strip().split("   ")
            list1.append(int(sections[0]))
            list2.append(int(sections[1]))

    list1.sort()
    list2.sort()
    return [list1,list2]



def total_distance(list1, list2):
    total_diff = [abs(a - b) for a,b in zip(list1,list2)]
    return sum(total_diff)

def similarity_score(list1, list2):
    hash_map2 = Counter(list2)

    total_score = 0
    for value in list1:
        if value in hash_map2:
            total_score += value  * hash_map2[value]

    return total_score


[listA, listB ] = get_lists()
print(total_distance(listA, listB)) # 2580760
print(similarity_score(listA,listB)) #25358365