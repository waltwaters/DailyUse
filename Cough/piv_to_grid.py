# -*- coding: utf-8 -*-
"""
Improved PIV to Grid Script
Handles specific column headers in the dataset.
"""

import numpy as np
import pandas as pd
import glob
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory


def piv_to_grid(csv_path):
    # Get the number of CSV files in the folder
    im = len(glob.glob(f'{csv_path}/*.csv'))
    if im == 0:
        raise ValueError("No CSV files found in the selected folder.")

    # Read one CSV file to determine the grid size and structure
    file = glob.glob(f'{csv_path}/*.csv')[0]
    data = pd.read_csv(file, header='infer', sep=';')

    # Extract unique x and y coordinates
    x = np.unique(data['x [pixel]'])
    y = np.unique(data['y [pixel]'])
    xx, yy = np.meshgrid(x, y)

    # Initialize arrays for the displacement and vorticity components
    u = np.zeros((len(y), len(x), im), dtype=float)  # x-displacement
    v = np.zeros((len(y), len(x), im), dtype=float)  # y-displacement
    w_z = np.zeros((len(y), len(x), im), dtype=float)  # Vorticity

    # Process each CSV file
    for i, file in enumerate(glob.glob(f'{csv_path}/*.csv')):
        print(f'Processing file {i + 1} of {im}: {file}')
        data = pd.read_csv(file, header='infer', sep=';')

        # Populate the grid data
        for j, y_val in enumerate(y):
            for k, x_val in enumerate(x):
                # Extract row matching current x and y values
                row = data[(data['x [pixel]'] == x_val) & (data['y [pixel]'] == y_val)]
                if not row.empty:
                    u[j, k, i] = row['x-displacement [pixel]'].values[0]
                    v[j, k, i] = row['y-displacement [pixel]'].values[0]
                    w_z[j, k, i] = row['Vorticity w_z (dv/dx - du/dy) [S]'].values[0]

    return xx, yy, u, v, w_z


# Main script
if __name__ == "__main__":
    # Use Tkinter to ask the user to select a folder
    root = Tk()
    root.withdraw()  # Hide the root window
    print("Please select the folder containing CSV files.")
    piv_data_folder = askdirectory(title="Select Folder Containing CSV Files")

    if not piv_data_folder:
        print("No folder selected. Exiting.")
    else:
        grid_folder = "processed_grid_data"
        save_path = os.path.join(piv_data_folder, grid_folder)

        # Create the output folder if it doesn't exist
        os.makedirs(save_path, exist_ok=True)

        try:
            x, y, u, v, w_z = piv_to_grid(piv_data_folder)

            # Save the processed grid data
            np.save(f'{save_path}/x.npy', x)
            np.save(f'{save_path}/y.npy', y)
            np.save(f'{save_path}/u.npy', u)
            np.save(f'{save_path}/v.npy', v)
            np.save(f'{save_path}/w_z.npy', w_z)

            print(f"Grid data saved to {save_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
