def solution(map):

    import numpy as np

    # extract height and width of map
    h, w = len(map), len(map[0])

    # locate all 1s below or to right of a 0
    locations = []
    for i in range(h):
        for j in range(w):
            # if current element is 0, check below and right
            if map[i][j] == 0:
                # check below
                if i != h - 1 and map[i + 1][j] == 1:
                    locations.append([i + 1, j])
                # check to right
                if j != w - 1 and map[i][j + 1] == 1:
                    locations.append([i, j + 1])
                # check to left
                if j != 0 and map[i][j - 1] == 1:
                    locations.append([i, j - 1])
    
    # loop to iterate through locations of 1s and drop them
    # first iteration tries dropping nothing

    # list to store path lengths
    lengths = []

    for k in range(len(locations) - 1):

        if k != 0:
            # remove a 1
            map[locations[k - 1][0]][locations[k - 1][1]] = 0

        # define the starting position
        pos = [0,0]
        # create queue for bfs
        q = []
        q.append(pos)
        # array to marks as visited
        visited = np.zeros((h, w), dtype=bool)
        visited[pos[0]][pos[1]] = True
        # predecessor array
        pred = {}
        for i in range(h):
            for j in range(w):
                pred[i,j] = None

        while len(q) > 0:

            # pop from queue
            current = q.pop(0)

            # find all neighbours
            neighbours = []
            if current[0] != 0 and map[current[0] - 1][current[1]] == 0:
                neighbours.append([current[0] - 1, current[1]])
            if current[1] != w - 1 and map[current[0]][current[1] + 1] == 0:
                neighbours.append([current[0], current[1] + 1])
            if current[1] != 0 and map[current[0]][current[1] - 1] == 0:
                neighbours.append([current[0], current[1] - 1])
            if current[0] != h - 1 and map[current[0] + 1][current[1]] == 0:
                neighbours.append([current[0] + 1, current[1]])

            # iterate through neighbours
            for neighbour in neighbours:
                if not visited[neighbour[0]][neighbour[1]]:
                    q.append(neighbour)
                    visited[neighbour[0]][neighbour[1]] = True
                    pred[neighbour[0],neighbour[1]] = current
            
        # use pred to backtrack
        end = [h - 1, w - 1]
        path = []

        while end is not None:
            path.append(end)
            end = pred[end[0], end[1]]
            
        # only append if actually made it to the end
        if path[-1] == [0,0]:
            lengths.append(len(path))

        if k != 0:
            # reset to 1
            map[locations[k - 1][0]][locations[k - 1][1]] = 1
            
    return min(lengths)


# solution([[0, 1, 1, 0], 
#           [0, 0, 0, 1], 
#           [1, 1, 0, 0], 
#           [1, 1, 1, 0]])
solution([[0, 0, 0, 0, 0, 0], 
          [1, 1, 1, 1, 1, 0], 
          [0, 0, 0, 0, 0, 0], 
          [0, 1, 1, 1, 1, 1], 
          [0, 1, 1, 1, 1, 1], 
          [0, 0, 0, 0, 0, 0]])
# solution([[0, 0, 0], 
#           [1, 1, 0], 
#           [1, 1, 0]])
# solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0]])
# solution([
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
# ])