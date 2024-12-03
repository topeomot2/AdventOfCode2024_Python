def all_increasing(list1):
    return all(int(i) < int(j) for i, j in zip(list1, list1[1:]))

def all_decreasing(list1):
    return all(int(i) > int(j) for i, j in zip(list1, list1[1:]))

def max_diff(list1):
    return all(abs(int(i) - int(j)) <= 3 for i, j in zip(list1, list1[1:]))

def min_diff(list1):
    return all(abs(int(i) - int(j)) >= 1 for i, j in zip(list1, list1[1:]))

def validate(list1):
    return (all_increasing(list1) or all_decreasing(list1)) and max_diff(list1) and min_diff(list1)

def validate_by_removing(list1, i):
    new_list = [*list1[:i],*list1[i+1:]]
    return validate(new_list)

def is_safe(list_reports):
    return validate(list_reports)

def is_safe_2(list_reports):
    response = validate(list_reports)

    if response:
        return response

    for i in range(len(list_reports)):
        if validate_by_removing(list_reports,i):
            return True

    return False


def count_safe_reports():
    count = 0

    with open("input.txt", "r") as file:
        for line in file:
            if is_safe(line.strip().split(" ")):
                count += 1

    return count

def count_safe_reports_2():
    count = 0

    with open("input.txt", "r") as file:
        for line in file:
            if is_safe_2(line.strip().split(" ")):
                count += 1

    return count

print(count_safe_reports())
print(count_safe_reports_2())