

## Hexagonal Game of Life Simulation

This code implements a Conway's Game of Life simulation on a hexagonal grid.

### Dependencies

The code requires the following Python libraries:

* `numpy` ([https://numpy.org/](https://numpy.org/))
* `matplotlib` ([https://matplotlib.org/](https://matplotlib.org/))

### Usage

The code can be used as follows:

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import random

# Class implementing the hexagonal game of life
class HexagonalGameOfLife:
    # ... (class definition)

# Example usage
size = 10
generations = 10
image_prefix = "hexagonal_game_of_life"
game = HexagonalGameOfLife(size)
game.run_simulation(generations, image_prefix)
```

This will create a 10x10 hexagonal grid with randomly initialized cells and run the simulation for 10 generations. Images of the grid will be saved at each generation with filenames like "hexagonal_game_of_life_generation_X.png", where X is the generation number.

### Explanation

The code defines a class `HexagonalGameOfLife` that simulates the game on a hexagonal grid. The class provides methods for:

* Initializing the grid with random or custom cell states.
* Finding the neighbors of a cell in the hexagonal grid.
* Applying the Conway's Game of Life rules to update the cell states.
* Implementing two resurrection rules:
    * Resurrecting a random selection of dead cells every 6 generations.
    * Resurrecting a single random dead cell every 4 generations.
* Saving a visual representation of the grid as an image file.
* Running the simulation for a specified number of generations, saving images at each generation.

### Customization

* You can modify the `size` variable to change the size of the grid.
* You can adjust the `generations` variable to control the simulation duration.
* You can change the `image_prefix` to customize the filenames of the generated images.
