def get_graph():
    main_graph = []
    with open("input.txt","r") as file:
        for line in file:
            arr = list(line.strip())
            main_graph.append(arr)
    return main_graph



def explore_path(graph, row, col):
    deltas = [[-1,0], [-1,-1], [-1,1], [1,0], [1,-1], [1,1],[0,-1],[0,1]]
    sum = 0
    for delta in deltas:
        word = "X"
        new_row = row
        new_col = col
        for i in range(3):
            new_row += delta[0]
            new_col += delta[1]
            row_in_bounds = 0 <= new_row < len(graph)
            col_in_bounds = 0 <= new_col < len(graph[0])

            if row_in_bounds and col_in_bounds:
                word = word + graph[new_row][new_col]
            else:
                break

        if word == "XMAS":
            sum += 1

    return sum

def explore_path_2(graph, row, col):
    deltasList = [[[-1,-1],[1,1]], [[-1,1], [1,-1]]]
    both_diagonal = 0

    for deltas in deltasList:
        word = ""
        for delta in deltas:
            new_row = row + delta[0]
            new_col = col + delta[1]
            row_in_bounds = 0 <= new_row < len(graph)
            col_in_bounds = 0 <= new_col < len(graph[0])

            if row_in_bounds and col_in_bounds:
                word  = word + graph[new_row][new_col]


        if word == "MS" or word == "SM":
            both_diagonal += 1

    if both_diagonal == 2:
        return 1
    else:
        return 0






def number_of_xmas(graph):
    sum = 0
    for row in range(len(graph)):
        for col in range(len(graph[0])):
            if graph[row][col] == "X":
                sum += explore_path(graph, row, col)
    return sum


def number_of_x_mas(graph):
    sum = 0
    for row in range(len(graph)):
        for col in range(len(graph[0])):
            if graph[row][col] == "A":
                sum += explore_path_2(graph, row, col)
    return sum

graph2 = get_graph()
print(number_of_xmas(graph2))
print(number_of_x_mas(graph2))


