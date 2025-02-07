import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog

def get_v_mag(u, v, frame):
    """Calculate the magnitude of velocity for a given frame."""
    mag = np.sqrt(u[:, :, frame]**2 + v[:, :, frame]**2)
    return mag

# Create a Tkinter root window (it won't be shown)
root = tk.Tk()
root.withdraw()  # Hide the root window
import matplotlib.pyplot as plt
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog

def get_v_mag(u, v, frame):
    return np.sqrt(u[:, :, frame]**2 + v[:, :, frame]**2)

root = tk.Tk()
root.withdraw()

folder_selected = filedialog.askdirectory(title="Select the folder containing the PIV data")

if folder_selected:
    x = np.load(os.path.join(folder_selected, "x.npy"))
    y = np.load(os.path.join(folder_selected, "y.npy"))
    u_vel = np.load(os.path.join(folder_selected, "u.npy"))
    v_vel = np.load(os.path.join(folder_selected, "v.npy"))

    print(f"Data loaded from {folder_selected}")
else:
    print("No folder selected. Exiting program.")
    exit()

cough_start = 0
cmap = plt.get_cmap("viridis")
fig, axs = plt.subplots(2, 3, figsize=(12, 5), dpi=100)
levels = np.linspace(0, 15, 200)
time_frames = [0, 1, 2, 3, 4, 5]
titles = [f"$t={i*0.1}\,s$" for i in range(6)]

for i, ax in enumerate(axs.flat):
    frame = time_frames[i] + cough_start
    v_mag = get_v_mag(u_vel, v_vel, frame)
    x_masked = (x > 250) & (x < 2250)
    v_mag_masked = np.ma.masked_where(~x_masked, v_mag)
    cp = ax.contourf(x, y, v_mag_masked, levels=levels, cmap=cmap)
    ax.set_xlim([250, 2250])
    ax.set_ylim([np.min(y), np.max(y)])
    ax.invert_yaxis()
    ax.set_xticks(np.linspace(250, 2250, 5))
    ax.set_yticks(np.linspace(np.min(y), np.max(y), 4))
    if i % 3 == 0:
        ax.set_ylabel(r"$y~(m)$", fontsize=16)
    if i >= 3:
        ax.set_xlabel(r"$x~(m)$", fontsize=16)
    ax.set_title(titles[i], fontsize=14)

cax = fig.add_axes([0.4, 0.93, 0.22, 0.03])
cbar = plt.colorbar(cp, orientation='horizontal', cax=cax)
cbar.set_ticks([0, 5, 10, 15])
cbar.ax.set_title(r"$V_{mag}~(ms^{-1})$", fontsize=14)

plt.subplots_adjust(wspace=0.11, hspace=0.22)
plt.show()
# Ask the user to select a folder
folder_selected = filedialog.askdirectory(title="Select the folder containing the PIV data")

# Check if a folder was selected
if folder_selected:
    # Load PIV Data Cough from the selected folder
    x = np.load(os.path.join(folder_selected, "x.npy"))
    y = np.load(os.path.join(folder_selected, "y.npy"))
    u_vel = np.load(os.path.join(folder_selected, "u.npy"))
    v_vel = np.load(os.path.join(folder_selected, "v.npy"))

    # Find the max and min values of x and y
    max_x = np.max(x)
    min_x = np.min(x)
    max_y = np.max(y)
    min_y = np.min(y)

    # Print confirmation
    print(f"Data loaded from {folder_selected}")
else:
    print("No folder selected. Exiting program.")

cough_start = 0  # Frame number where cough starts
cmap = matplotlib.colors.LinearSegmentedColormap.from_list(
    "", ["#333d47", "#20a9ca", "#25caa0", "#f9b347", "#f95b3a"]
)

# Plot setup
fig, axs = plt.subplots(2, 3, figsize=(12, 5), dpi=100)
plt.rcParams["mathtext.fontset"] = "cm"
hfont = {
    'fontname': 'Times New Roman',
    'family': 'serif',
    'size': 12
}
levels = np.linspace(0, 15, 200)

# Subplots
time_frames = [0, 1, 2, 3, 4, 5]
titles = [r"$t=0\,s$", r"$t=0.1\,s$", r"$t=0.2\,s$",
          r"$t=0.3\,s$", r"$t=0.4\,s$", r"$t=0.5\,s$"]

# Subplots
for i, ax in enumerate(axs.flat):
    frame = time_frames[i] + cough_start
    v_mag = get_v_mag(u_vel, v_vel, frame)

    # Mask the data where 250 < x < 2000
    x_masked = (x > 250) & (x < 2250)  # Select x-values between 250 and 2000
    v_mag_masked = np.ma.masked_where(~x_masked, v_mag)  # Mask corresponding velocity magnitude data

    # Plot the contour with the masked data
    cp = ax.contourf(x, y, v_mag_masked, levels=levels, cmap=cmap)

    # Scaling factor for x and y labels (only for display, not for axis limits)
    amp_factor = 2.5 * 1000  # Adjust this factor to scale appropriately in pixel/m

    # Set the x and y ticks and limits, taking into account the starting point of x=250
    ax.set_xlim([250, 2250])  # Set x-axis to the range 250 < x < 2000
    ax.set_ylim([np.min(y), np.max(y)])  # Set y-axis to its full range

    # Invert the y-axis direction
    ax.invert_yaxis()  # This will make the y-axis point downwards (0 will be at the top)

    # Generate uniformly spaced ticks between 250 and 2000 for x-axis
    x_ticks = np.linspace(250, 2250, num=5)
    # Generate uniformly spaced ticks between np.min(y) and np.max(y) for y-axis
    y_ticks = np.linspace(np.min(y), np.max(y), num=4)

    # Set the actual x and y ticks (adjusted based on your desired scaling and data)
    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)

    # Update y-axis labels for the first column
    if i % 3 == 0:  # Add y-axis labels only for the first column
        ax.set_ylabel(r"$y~(m)$", fontsize=16)
        # Set the ticks on the y-axis
        ax.set_yticks(y_ticks)
        ax.set_yticklabels([f'{tick / amp_factor:.1f}' for tick in y_ticks], **hfont)
    else:
        ax.set_yticklabels(['' for _ in ax.get_yticks()])  # Hide the y-tick labels for others

    # Update x-axis labels for the bottom row
    if i >= 3:  # Add x-axis labels only for the bottom row
        ax.set_xlabel(r"$x~(m)$", fontsize=16)
        # Set the ticks on the x-axis
        ax.set_xticks(x_ticks)
        ax.set_xticklabels([f'{(tick-250) / amp_factor:.1f}' for tick in x_ticks], **hfont)
    else:
        ax.set_xticklabels(['' for _ in ax.get_xticks()])  # Hide the y-tick labels for others


    # Apply the title
    ax.set_title(titles[i], fontsize=14)

# Colorbar
cax = fig.add_axes([0.4, 0.93, 0.22, 0.03])
cbar = plt.colorbar(cp, orientation='horizontal', cax=cax)
cbar.set_ticks([0, 5, 10, 15])
cbar.ax.set_xticklabels(cbar.ax.get_xticks(), **hfont)
cbar.ax.set_title(r"$V_{mag}~(ms^{-1})$", fontsize=14)

# Adjust layout
plt.subplots_adjust(wspace=0.11, hspace=0.22)
plt.show()
