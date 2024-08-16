

# [
# "####E#",
#  "#    #"
#  "#S####"
# ]




class Point:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

def walk(maze, wall, curr, end, seen, path):

    # Base case: off the map
    if curr.x < 0 or curr.x >= len(maze[0]) or curr.y < 0 or curr.y >= len(maze):
        return False
    
    # Base case: on a wall
    if maze[curr.y][curr.x] == wall:
        return False
    
    # Base case: on the end
    if curr.x == end.x and curr.y == end.y:
        path.append(Point(end.x, end.y))
        return True

    # Base case: if already been here
    if seen[curr.y][curr.x]:
        return False


    # Mark the cell as seen and update the maze
    seen[curr.y][curr.x] = True
    if maze[curr.y][curr.x] not in ["E", "S"]:
        maze[curr.y][curr.x] = "o"
    path.append(Point(curr.x, curr.y))

    # Debug: print the current state of the maze
    for row in maze:
        print("".join(row))
    print()

    # Explore all four directions: top, right, bottom, left
    for [dx, dy] in dir:
        next_curr = Point(curr.x + dx, curr.y + dy)
        if walk(maze, wall, next_curr, end, seen, path):
            return True
        

    # if in a dead end and to go back to the cell we have already seen
    path.pop()

    return False



def solve(maze, wall, start, end):
    seen = []
    path = []


    for i in range(len(maze)):
        seen.append([False] * len(maze[0]))
    
    start_point = Point(start["x"], start["y"])
    end_point = Point(end["x"], end["y"])

    walk(maze, wall, start_point, end_point, seen, path)

    return path

dir = [
    [-1, 0],  # Up
    [0, 1],  # Right
    [1, 0],  # Down
    [0, -1], # Left
    
]
maze = [
    list("XXXEXXX"),
    list("X   X X"),
    list("X XXX X"),
    list("X     X"),
    list("X     X"),
    list("XSXXXXX")
    ]
wall = "X"
start = {"x": 1, "y": 5}
end = {"x": 3, "y": 0}


path = solve(maze, wall, start, end)
for point in path:
    print(f"({point.x}, {point.y})")
    

