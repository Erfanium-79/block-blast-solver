import tkinter as tk
import numpy as np
from utils import *  # Import functions from utils.py

# Initialize Tkinter window
root = tk.Tk()
root.title("Block Blast Grid Selector")

grid_size = 8
block_size = 5

# Create the main grid
main_grid_array = np.zeros((grid_size, grid_size), dtype=int)
main_buttons = []
main_frame = tk.Frame(root)
main_frame.pack()

for r in range(grid_size):
    row_buttons = []
    for c in range(grid_size):
        btn = tk.Button(main_frame, width=4, height=2, bg="white", 
                        command=lambda r=r, c=c: toggle_cell(main_buttons, main_grid_array, r, c))
        btn.grid(row=r, column=c, padx=1, pady=1)
        row_buttons.append(btn)
    main_buttons.append(row_buttons)

# Create blocks
block_arrays = [np.zeros((block_size, block_size), dtype=int) for _ in range(3)]
block_buttons = []
blocks_frame = tk.Frame(root)
blocks_frame.pack(pady=10)

for b in range(3):
    frame = tk.Frame(blocks_frame)
    frame.grid(row=0, column=b, padx=10)
    buttons = []
    for r in range(block_size):
        row_buttons = []
        for c in range(block_size):
            btn = tk.Button(frame, width=4, height=2, bg="white", 
                            command=lambda r=r, c=c, b=b: toggle_cell(block_buttons[b], block_arrays[b], r, c))
            btn.grid(row=r, column=c, padx=1, pady=1)
            row_buttons.append(btn)
        buttons.append(row_buttons)
    block_buttons.append(buttons)

# Button to save and exit
submit_btn = tk.Button(root, text="Save & Exit", command=lambda: save_and_exit(root))
submit_btn.pack(pady=10)

# Show the window once
root.update()
root.wait_window()


if __name__ == "__main__":
    # print("Main Grid:\n", main_grid_array)
    # print("Block 1:\n", block_arrays[0])
    # print("Block 2:\n", block_arrays[1])
    # print("Block 3:\n", block_arrays[2])
    # print(can_place_block(main_grid_array, block_arrays[0]))
    # grid = np.zeros((8, 8), dtype=int)
    # block = np.array([
    #     [0, 0, 0, 0, 0],
    #     [0, 1, 1, 0, 0],
    #     [0, 1, 1, 0, 0],
    #     [0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0]
    # ])

    resulting_grids = place_block_and_get_states(main_grid_array, block_arrays[0])
    print(f"Number of valid placements: {len(resulting_grids)}")
    print(resulting_grids)
