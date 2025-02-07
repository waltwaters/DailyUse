import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import os


hfont = {
    'fontname': 'Times New Roman',
    'family': 'serif',
    'size': 12
}


# Define the folder containing the CSV files
folder_path = '/Users/waltwang/PycharmProjects/DailyUse/Cough/csv_path/csv'

# Get a list of all CSV files in the directory
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Sort the files by name
csv_files.sort()

# Set up the figure for 6 subfigures (3x2 layout)
fig, axs = plt.subplots(2, 3, figsize=(12, 8), dpi=100)

# Titles for the subplots
titles = [r"$t=0\,s$", r"$t=0.1\,s$", r"$t=0.2\,s$",
          r"$t=0.3\,s$", r"$t=0.4\,s$", r"$t=0.5\,s$"]

# Loop over each CSV file and plot them in the subfigures
for i, csv_file in enumerate(csv_files[:6]):  # Only plot the first 6 CSV files
    # Construct the full file path
    csv_file_path = os.path.join(folder_path, csv_file)

    # Print the current CSV file being processed
    print(f"Processing file: {csv_file_path}")


    # Load the CSV file with the correct delimiter
    data = pd.read_csv(csv_file_path, delimiter=';')

    # Extract columns from the CSV (adjust these based on the actual column names)
    x = data['x [pixel]'].values
    y = data['y [pixel]'].values
    u_vel = data['x-displacement [pixel]'].values
    v_vel = data['y-displacement [pixel]'].values

    # Define grid dimensions for contour plotting
    x_grid = np.unique(x)  # Unique x values
    y_grid = np.unique(y)  # Unique y values

    # Reshaping u and v to match the grid
    U_grid = u_vel.reshape(len(y_grid), len(x_grid))
    V_grid = v_vel.reshape(len(y_grid), len(x_grid))

    # Calculate the magnitude of the velocity (displacement) field
    v_mag = np.sqrt(U_grid ** 2 + V_grid ** 2)

    # Choose the subplot position (i//2 for row, i%2 for column)
    row = i // 3
    col = i % 3
    ax = axs[row, col]

    # Plot the contour in the corresponding subplot
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list(
        "", ["#333d47", "#20a9ca", "#25caa0", "#f9b347", "#f95b3a"]
    )
    cp = ax.contourf(x_grid, y_grid, v_mag, 200, cmap=cmap)

    # Set axis labels and titles for each subplot


    # Set axis limits
    ax.set_xlim([min(x_grid), max(x_grid)])
    ax.set_ylim([min(y_grid), max(y_grid)])

# Adjust layout to make room for colorbar
fig.subplots_adjust(hspace=0.3, wspace=0.3, top=0.9, bottom=0.1)

# Colorbar
cax = fig.add_axes([0.4, 0.94, 0.22, 0.02])
cbar = plt.colorbar(cp, orientation='horizontal', cax=cax)
cbar.set_ticks([0, 2, 4, 6])
cbar.ax.set_xticklabels(cbar.ax.get_xticks(), **hfont)
cbar.ax.set_title(r"$V_{mag}~(ms^{-1})$", fontsize=14)

# Show the final plot
plt.subplots_adjust(wspace=0.11, hspace=0.22)

plt.show()