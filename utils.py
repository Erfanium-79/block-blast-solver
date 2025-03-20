import numpy as np
# import tkinter as tk

def remove_filled_rows_and_cols(arr: np.ndarray) -> np.ndarray:
    #get row and col indicies of all one values
    row_indices = np.where(np.all(arr == 1, axis=1))[0]
    col_indices = np.where(np.all(arr == 1, axis=0))[0]

    # Modify the rows and columns
    arr[row_indices, :] = 0
    arr[:, col_indices] = 0

    return arr

def toggle_cell(buttons, grid_array, row, col):
    """Toggle the color of a button and update the corresponding array."""
    current_color = buttons[row][col].cget("bg")
    new_color = "black" if current_color == "white" else "white"
    buttons[row][col].config(bg=new_color)
    grid_array[row, col] = 1 if new_color == "black" else 0

def save_and_exit(root):
    """Close the Tkinter window."""
    root.destroy()

def can_place_block(grid: np.ndarray, block: np.ndarray) -> bool:
    """Check if the block can be placed in any position on the grid."""
    grid_size = 8
    block_rows, block_cols = np.where(block == 1)  # Get positions of 1s

    for i in range(grid_size):
        for j in range(grid_size):
            if all(0 <= i + r < grid_size and 0 <= j + c < grid_size and grid[i + r, j + c] == 0
                   for r, c in zip(block_rows, block_cols)):
                return True  # Found at least one valid placement

    return False  # No valid placement found

def trim_block(block: np.ndarray) -> np.ndarray:
    """Trim empty rows and columns from the block to focus only on its occupied area."""
    rows, cols = np.where(block == 1)  # Get positions of 1s
    if len(rows) == 0:  # If the block is empty, return it as is
        return block
    return block[min(rows):max(rows) + 1, min(cols):max(cols) + 1]

def can_place_block(grid: np.ndarray, block: np.ndarray) -> bool:
    """Check if the trimmed block can be placed in any position on the grid."""
    grid_size = 8
    block = trim_block(block)  # Trim the block before processing
    block_shape = block.shape
    block_rows, block_cols = np.where(block == 1)  # Get positions of 1s

    for i in range(grid_size - block_shape[0] + 1):
        for j in range(grid_size - block_shape[1] + 1):
            if all(grid[i + r, j + c] == 0 for r, c in zip(block_rows, block_cols)):
                return True  # Found at least one valid placement

    return False  # No valid placement found

def place_block_and_get_states(grid: np.ndarray, block: np.ndarray) -> list:
    """Place the trimmed block at all possible locations and return the new grid states."""
    grid_size = 8
    block = trim_block(block)  # Trim the block before processing
    block_shape = block.shape
    block_rows, block_cols = np.where(block == 1)  # Get positions of 1s
    valid_states = []

    for i in range(grid_size - block_shape[0] + 1):
        for j in range(grid_size - block_shape[1] + 1):
            if all(grid[i + r, j + c] == 0 for r, c in zip(block_rows, block_cols)):
                new_grid = grid.copy()

                # Place the block
                for r, c in zip(block_rows, block_cols):
                    new_grid[i + r, j + c] = 1

                # Remove filled rows and columns
                new_grid = remove_filled_rows_and_cols(new_grid)

                valid_states.append(new_grid)

    return valid_states  # List of all possible resulting grids