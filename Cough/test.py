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
cmap = plt.get_cmap("inferno")  # Changed colormap to 'plasma'
fig, axs = plt.subplots(2, 3, figsize=(12, 5), dpi=100)
levels = np.linspace(0, 15, 200)
time_frames = [0, 1, 2, 3, 4, 5]
titles = [f"$t={i*0.1:.1f}\,s$" for i in range(6)]  # Keep only one valid decimal number
amp_factor = 2.5 * 1000

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
        ax.set_yticklabels([f'{tick / amp_factor:.1f}' for tick in ax.get_yticks()])
    else:
        ax.set_yticklabels([])
    if i >= 3:
        ax.set_xticklabels([f'{(tick-250) / amp_factor:.1f}' for tick in ax.get_xticks()])
    else:
        ax.set_xticklabels([])  # Remove x-axis labels for subfigures 1, 2, and 3
    ax.set_title(titles[i], fontsize=14)

# Add x and y labels in the middle of the figure
fig.text(0.5, 0.04, r"$x~(m)$", ha='center', fontsize=16)
fig.text(0.04, 0.5, r"$y~(m)$", va='center', rotation='vertical', fontsize=16)

cax = fig.add_axes([0.4, 0.93, 0.22, 0.03])
cbar = plt.colorbar(cp, orientation='horizontal', cax=cax)
cbar.set_ticks([0, 5, 10, 15])
cbar.ax.set_title(r"$V_{mag}~(ms^{-1})$", fontsize=14)

plt.subplots_adjust(wspace=0.11, hspace=0.22)
plt.show()