import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def get_v_mag(u, v, frame):
    mag = np.sqrt(u[:,:,frame]**2 + v[:,:,frame]**2)
    return mag

## Load PIV Data Cough

x = np.load("PIV_Data/x.npy")
y = np.load("PIV_Data/y.npy")
u_vel = np.load("PIV_Data/u.npy")
v_vel = np.load("PIV_Data/v.npy")


cough_start = 90 # Frame number where cough starts
cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["#333d47","#20a9ca","#25caa0","#f9b347","#f95b3a"])

x_start = 320
xticks = [0+x_start, 200+x_start, 400+x_start, 600+x_start, 800+x_start]

fig,axs = plt.subplots(2,3,figsize=(12, 5), dpi=600)
plt.rcParams["mathtext.fontset"] = "cm"
hfont = {'fontname':'Times New Roman',
        'family':'serif',
        'size' : 12}
levels = np.linspace(0, 6, 200)

axs[0,0].contourf(x, y, get_v_mag(u_vel,v_vel, 0+cough_start), levels = levels, cmap = cmap)
axs[0,0].set_xticks(xticks)
axs[0,0].set_xticklabels([''.format(element) for element in xticks], **hfont)
axs[0,0].set_yticks([-10, -210, -410, -610])
axs[0,0].set_yticklabels(-1*(axs[0,0].get_yticks()+10)/1000, **hfont)
axs[0,0].set_xlim([x_start, x_start+800])
axs[0,0].set_ylim([-610, -10])
axs[0,0].set_ylabel("$y~(m)$", fontsize=16)
axs[0,0].set_title("$t=0\,s$", fontsize=14)

axs[0,1].contourf(x, y, get_v_mag(u_vel,v_vel, 100+cough_start), levels = levels, cmap = cmap)
axs[0,1].set_xticks(xticks)
axs[0,1].set_xticklabels([''.format(element) for element in xticks], **hfont)
axs[0,1].set_yticks([-10, -210, -410, -610])
axs[0,1].set_yticklabels([''.format(element) for element in axs[0,1].get_yticks()], **hfont)
axs[0,1].set_xlim([x_start, x_start+800])
axs[0,1].set_ylim([-610, -10])
axs[0,1].set_title("$t=0.1\,s$", fontsize=14)

axs[0,2].contourf(x, y, get_v_mag(u_vel,v_vel, 200+cough_start), levels = levels, cmap = cmap)
axs[0,2].set_xticks(xticks)
axs[0,2].set_xticklabels([''.format(element) for element in xticks], **hfont)
axs[0,2].set_yticks([-10, -210, -410, -610])
axs[0,2].set_yticklabels([''.format(element) for element in axs[0,2].get_yticks()], **hfont)
axs[0,2].set_xlim([x_start, x_start+800])
axs[0,2].set_ylim([-610, -10])
axs[0,2].set_title("$t=0.2\,s$", fontsize=14)

axs[1,0].contourf(x, y, get_v_mag(u_vel,v_vel, 300+cough_start), levels = levels, cmap = cmap)
axs[1,0].set_xticks(xticks)
axs[1,0].set_xticklabels([(element-x_start)/1000 for element in xticks], **hfont)
axs[1,0].set_yticks([-10, -210, -410, -610])
axs[1,0].set_yticklabels(-1*(axs[1,0].get_yticks()+10)/1000, **hfont)
axs[1,0].set_xlim([x_start, x_start+800])
axs[1,0].set_ylim([-610, -10])
axs[1,0].set_ylabel("$y~(m)$", fontsize=16)
axs[1,0].set_xlabel("$x~(m)$", fontsize=16)
axs[1,0].set_title("$t=0.3\,s$", fontsize=14)

axs[1,1].contourf(x, y, get_v_mag(u_vel,v_vel, 400+cough_start), levels = levels, cmap = cmap)
axs[1,1].set_xticks(xticks)
axs[1,1].set_xticklabels([(element-x_start)/1000 for element in xticks], **hfont)
axs[1,1].set_yticks([-10, -210, -410, -610])
axs[1,1].set_yticklabels([''.format(element) for element in axs[1,1].get_yticks()], **hfont)
axs[1,1].set_xlim([x_start, x_start+800])
axs[1,1].set_ylim([-610, -10])
axs[1,1].set_xlabel("$x~(m)$", fontsize=16)
axs[1,1].set_title("$t=0.4\,s$", fontsize=14)

cp = axs[1,2].contourf(x, y, get_v_mag(u_vel,v_vel, 500+cough_start), levels = levels, cmap = cmap)
axs[1,2].set_xticks(xticks)
axs[1,2].set_xticklabels([(element-x_start)/1000 for element in xticks], **hfont)
axs[1,2].set_yticks([-10, -210, -410, -610])
axs[1,2].set_yticklabels([''.format(element) for element in axs[1,2].get_yticks()], **hfont)
axs[1,2].set_xlim([x_start, x_start+800])
axs[1,2].set_ylim([-610, -10])
axs[1,2].set_xlabel("$x~(m)$", fontsize=16)
axs[1,2].set_title("$t=0.5\,s$", fontsize=14)

cax = fig.add_axes([0.4, 1, 0.2, 0.02])
cbar2 = plt.colorbar(cp, orientation = 'horizontal', cax=cax)
cbar2.set_ticks([0, 2, 4, 6])
cbar2.ax.set_xticklabels(cbar2.ax.get_xticks(), **hfont)
cbar2.ax.set_title('$V_{mag}~(ms^{-1})$', fontsize=14)

plt.subplots_adjust(wspace=0.11, hspace=0.22)
plt.show()