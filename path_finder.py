### Shortest path algorithm using tkinter for visual representation
import tkinter as tk
import queue

maze=[
    [1,1,1,3,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,1,1,1],
    [1,0,1,0,1,0,0,0,0,1],
    [1,0,1,0,1,1,1,1,0,1],
    [1,0,1,0,0,0,0,0,0,2],
    [1,1,1,1,1,1,1,1,1,1]    
]

class Labirint(tk.Tk):
    def __init__(self, maze, path):
        super().__init__()

        self.title("Labirint")
        self.geometry("400x400")

        self.canvas = tk.Canvas(self, bg="white", width=400, height=400)
        self.canvas.pack()

        self.labirint = maze
        self.path = path

        self.rows = len(self.labirint)
        self.columns = len(self.labirint[0])

        self.draw_labirint()

    def draw_labirint(self):
        cell_width = 400 // self.columns
        cell_height = 400 // self.rows

        for i in range(self.rows):
            for j in range(self.columns):
                x1 = j * cell_width
                y1 = i * cell_height
                x2 = x1 + cell_width
                y2 = y1 + cell_height

                if self.labirint[i][j] == 0:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
                    if (i, j) in self.path:
                        self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
                    
                elif self.labirint[i][j] == 1:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")
                elif self.labirint[i][j] == 2:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="red")
                elif self.labirint[i][j] == 3:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")

                if ((i, j) in self.path):
                    if (self.labirint[i][j] == 1):
                        fill_color = "blue"
                        self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)

def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None

def find_path(maze):
    start = 2
    end = 3
    start_pos = find_start(maze, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = set()
    path = []
    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        if maze[row][col] == end:
            return new_path

        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            r, c = neighbor
            if maze[r][c] != 1:
                new_path = path + [neighbor]
                q.put((neighbor, new_path))
                visited.add(neighbor)

    return new_path

def find_neighbors(maze, row, col):
    neighbors = []

    if row > 0:
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):
        neighbors.append((row + 1, col))
    if col > 0:
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]):
        neighbors.append((row, col + 1))

    return neighbors

def main():
    path = find_path(maze)
    app = Labirint(maze,path)
    app.mainloop()

if __name__ == "__main__":
    main()
