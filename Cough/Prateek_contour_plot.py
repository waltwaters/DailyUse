import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog


def get_v_mag(u, v, frame):
    """Calculate the magnitude of velocity for a given frame."""
    return np.sqrt(u[:, :, frame] ** 2 + v[:, :, frame] ** 2)


def create_contour(ax, x, y, u_vel, v_vel, frame, xticks, cmap, x_start):
    """Create a contour plot on the given axis."""
    levels = np.linspace(0, 6, 200)
    v_mag = get_v_mag(u_vel, v_vel, frame)
    c = ax.contourf(x, y, v_mag, levels=levels, cmap=cmap)

    # Set axis labels and limits
    ax.set_xticks(xticks)
    ax.set_xticklabels([(t - x_start) / 1000 for t in xticks], fontname='Times New Roman', family='serif', size=12)
    ax.set_yticks([-10, -210, -410, -610])
    ax.set_yticklabels([f'{-1 * (ytick + 10) / 1000:.1f}' for ytick in ax.get_yticks()], fontname='Times New Roman',
                       family='serif', size=12)
    ax.set_xlim([x_start, x_start + 800])




def main():
    # Create a Tkinter root window (it won't be shown)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Ask the user to select a folder
    folder_selected = filedialog.askdirectory(title="Select the folder containing the PIV data")

    if not folder_selected:
        print("No folder selected. Exiting program.")
        return

    # Load PIV Data from the selected folder
    x = np.load(os.path.join(folder_selected, "x.npy"))
    y = np.load(os.path.join(folder_selected, "y.npy"))
    u_vel = np.load(os.path.join(folder_selected, "u.npy"))
    v_vel = np.load(os.path.join(folder_selected, "v.npy"))

    print(f"Data loaded from {folder_selected}")

    # Parameters
    cough_start = 90  # Frame number where cough starts
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("",
                                                               ["#333d47", "#20a9ca", "#25caa0", "#f9b347", "#f95b3a"])
    x_start = 320
    xticks = [0 + x_start, 200 + x_start, 400 + x_start, 600 + x_start, 800 + x_start]

    # Create subplots
    fig, axs = plt.subplots(2, 3, figsize=(12, 5), dpi=100)
    plt.rcParams["mathtext.fontset"] = "cm"

    # Frame numbers for each subplot
    frames = [0, 100, 200, 300, 400, 500]
    titles = [r"$t=0\,s$", r"$t=0.1\,s$", r"$t=0.2\,s$", r"$t=0.3\,s$", r"$t=0.4\,s$", r"$t=0.5\,s$"]

    # Create each contour plot
    for i, ax in enumerate(axs.flat):
        create_contour(ax, x, y, u_vel, v_vel, frames[i] + cough_start, xticks, cmap, x_start)
        ax.set_title(titles[i], fontsize=14)
        if i >= 3:
            ax.set_xlabel("$x~(m)$", fontsize=16)

        if i % 3 == 0:
            ax.set_ylabel("$y~(m)$", fontsize=16)
        else:
            ax.set_yticklabels(['' for _ in ax.get_yticks()])

    # Add colorbar
    cax = fig.add_axes([0.4, 0.93, 0.2, 0.02])
    cbar2 = plt.colorbar(
        axs[1, 2].contourf(x, y, get_v_mag(u_vel, v_vel, 500 + cough_start), levels=np.linspace(0, 6, 200), cmap=cmap),
        orientation='horizontal', cax=cax)
    cbar2.set_ticks([0, 2, 4, 6])
    cbar2.ax.set_xticklabels(cbar2.ax.get_xticks(), fontname='Times New Roman', family='serif', size=12)
    cbar2.ax.set_title('$V_{mag}~(ms^{-1})$', fontsize=14)

    plt.subplots_adjust(wspace=0.11, hspace=0.22)
    plt.show()


if __name__ == "__main__":
    main()
