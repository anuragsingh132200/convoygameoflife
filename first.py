import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import random

class HexagonalGameOfLife:
    def __init__(self, size):
        self.size = size
        self.grid = np.zeros((size, size), dtype=int)
        self.prev_grid = np.zeros((size, size), dtype=int)
        self.generation = 0

    def initialize_grid(self):
        # Initialize the grid randomly with all dead cells
        self.grid = np.zeros((self.size, self.size), dtype=int)
        self.prev_grid = np.zeros((self.size, self.size), dtype=int)

    def get_neighbors(self, i, j):
        # Get the neighbors of a cell (i, j) in a hexagonal grid
        neighbors = []
        offsets = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, 1)]
        for offset in offsets:
            ni = i + offset[0]
            nj = j + offset[1]
            if 0 <= ni < self.size and 0 <= nj < self.size:
                neighbors.append((ni, nj))
        return neighbors

    def count_live_neighbors(self, i, j):
        # Count the number of live neighbors of a cell (i, j)
        neighbors = self.get_neighbors(i, j)
        count = sum(self.grid[n[0], n[1]] for n in neighbors)
        return count

    def apply_rules(self):
        new_grid = np.zeros((self.size, self.size), dtype=int)
        for i in range(self.size):
            for j in range(self.size):
                live_neighbors = self.count_live_neighbors(i, j)
                if self.grid[i, j] == 1:
                    # Cell is alive
                    if live_neighbors < 2:
                        new_grid[i, j] = 0  # Underpopulation
                    elif live_neighbors in [2, 3]:
                        new_grid[i, j] = 1  # Survival
                    else:
                        new_grid[i, j] = 0  # Overpopulation
                else:
                    # Cell is dead
                    if live_neighbors == 3:
                        new_grid[i, j] = 1  # Reproduction
        self.prev_grid = np.copy(self.grid)  # Update previous state
        self.grid = new_grid

    def resurrect_cells(self):
        # Resurrect cells every 6 generations
        if self.generation % 6 == 0:
            # Find all dead cells
            dead_cells = [(i, j) for i in range(self.size) for j in range(self.size) if self.grid[i, j] == 0]
            # Randomly choose cells to resurrect
            for cell in random.sample(dead_cells, len(dead_cells) // 2):
                self.grid[cell[0], cell[1]] = 1

    def random_resurrection(self):
        # Resurrect a random dead cell every 4 generations
        if self.generation % 4 == 0:
            # Find all dead cells
            dead_cells = [(i, j) for i in range(self.size) for j in range(self.size) if self.grid[i, j] == 0]
            # Randomly choose a cell to resurrect
            if dead_cells:
                cell = random.choice(dead_cells)
                self.grid[cell[0], cell[1]] = 1

    def save_grid_image(self, filename):
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
    # Parameters for hexagon size and spacing
        hex_size = 0.5  # Hexagon size
        vertical_spacing = hex_size * np.sqrt(3)  # Vertical spacing between rows
        horizontal_spacing = hex_size * 2  # Horizontal spacing between columns
        offset_x = horizontal_spacing / 2  # Offset for even rows

        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i, j] == 1:  # Only plot live cells
                    x = j * horizontal_spacing
                    if i % 2 == 0:
                        x += offset_x
                    y = i * vertical_spacing
                    hexagon = RegularPolygon((x, y), numVertices=6, radius=hex_size, edgecolor='black', facecolor='green')
                    ax.add_patch(hexagon)
                else:
                    x = j * horizontal_spacing
                    if i % 2 == 0:
                        x += offset_x
                    y = i * vertical_spacing
                    hexagon = RegularPolygon((x, y), numVertices=6, radius=hex_size, edgecolor='black', facecolor='white')
                    ax.add_patch(hexagon)
        ax.set_xlim(-hex_size, self.size * horizontal_spacing - hex_size)
        ax.autoscale_view()
        ax.axis('off')
        plt.savefig(filename)
        plt.close()


    def run_simulation(self, generations, image_prefix):
        self.initialize_grid()
        for gen in range(generations):
            self.apply_rules()
            self.resurrect_cells()
            self.random_resurrection()
            self.save_grid_image(f"{image_prefix}_generation_{self.generation}.png")
            self.generation += 1
       
        
        
# Example usage:
size = 10
generations = 10
image_prefix = "hexagonal_game_of_life"
game = HexagonalGameOfLife(size)
game.run_simulation(generations, image_prefix)
