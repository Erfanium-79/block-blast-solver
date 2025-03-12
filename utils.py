import numpy as np
import tkinter as tk

def remove_filled_rows_and_cols(arr: np.ndarray) -> np.ndarray:
    #get row and col indicies of all one values
    row_indices = np.where(np.all(arr == 1, axis=1))[0]
    col_indices = np.where(np.all(arr == 1, axis=0))[0]

    # Modify the rows and columns
    arr[row_indices, :] = 0
    arr[:, col_indices] = 0

    return arr


def toggle_cell(buttons, grid_array, row, col):
    current_color = buttons[row][col].cget("bg")
    new_color = "black" if current_color == "white" else "white"
    buttons[row][col].config(bg=new_color)
    grid_array[row, col] = 1 if new_color == "black" else 0

def print_arrays():
    print("Main Grid:")
    print(main_grid_array)
    print("Block 1:")
    print(block_arrays[0])
    print("Block 2:")
    print(block_arrays[1])
    print("Block 3:")
    print(block_arrays[2])

# Initialize the main window
root = tk.Tk()
root.title("Block Blast Grid Selector")

grid_size = 8
block_size = 5

# Frame for main grid
main_frame = tk.Frame(root)
main_frame.pack()

# Main 8x8 grid
main_buttons = []
main_grid_array = np.zeros((grid_size, grid_size), dtype=int)
for r in range(grid_size):
    row_buttons = []
    for c in range(grid_size):
        btn = tk.Button(main_frame, width=4, height=2, bg="white", command=lambda r=r, c=c: toggle_cell(main_buttons, main_grid_array, r, c))
        btn.grid(row=r, column=c, padx=1, pady=1)
        row_buttons.append(btn)
    main_buttons.append(row_buttons)

# Frame for blocks
blocks_frame = tk.Frame(root)
blocks_frame.pack(pady=10)

block_buttons = []
block_arrays = [np.zeros((block_size, block_size), dtype=int) for _ in range(3)]
for b in range(3):
    frame = tk.Frame(blocks_frame)
    frame.grid(row=0, column=b, padx=10)
    buttons = []
    for r in range(block_size):
        row_buttons = []
        for c in range(block_size):
            btn = tk.Button(frame, width=4, height=2, bg="white", command=lambda r=r, c=c, b=b: toggle_cell(block_buttons[b], block_arrays[b], r, c))
            btn.grid(row=r, column=c, padx=1, pady=1)
            row_buttons.append(btn)
        buttons.append(row_buttons)
    block_buttons.append(buttons)

# Button to print the final arrays
submit_btn = tk.Button(root, text="Print Arrays", command=print_arrays)
submit_btn.pack(pady=10)

root.mainloop()
