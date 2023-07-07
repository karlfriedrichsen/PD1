import nibabel as nib
import nilearn as nil
import os
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np
import time
import stackview
#import skimage.io as skio

def multi_slice_viewer(volume):
    remove_keymap_conflicts({'j', 'k'})
    fig, ax = plt.subplots()
    ax.volume = volume
    ax.index = volume.shape[0] // 2
    ax.imshow(volume[ax.index])
    fig.canvas.mpl_connect('key_press_event', process_key)

def process_key(event):
    fig = event.canvas.figure
    ax = fig.axes[0]
    if event.key == 'j':
        previous_slice(ax)
    elif event.key == 'k':
        next_slice(ax)
    fig.canvas.draw()

def previous_slice(ax):
    volume = ax.volume
    ax.index = (ax.index - 1) % volume.shape[0]  # wrap around using %
    ax.images[0].set_array(volume[ax.index])

def next_slice(ax):
    volume = ax.volume
    ax.index = (ax.index + 1) % volume.shape[0]
    ax.images[0].set_array(volume[ax.index])
    
def remove_keymap_conflicts(new_keys_set):
    for prop in plt.rcParams:
        if prop.startswith('keymap.'):
            keys = plt.rcParams[prop]
            remove_list = set(keys) & new_keys_set
            for key in remove_list:
                keys.remove(key)


testDir='C:\\Users\\friedrichsenk\\Downloads\\1179205_v2'
fileList=os.listdir(testDir)
testFile='mra.nii'

mraTest=nib.load(testDir+'\\'+testFile)
mraArray=mraTest.get_fdata()
#plt.imshow(mraArray[50], cmap='bone')
#plt.axis('off')
#plt.show()

multi_slice_viewer(mraArray.T)

#stackview.slice(mraArray)

# for i in range(mraArray.shape[2]):
#     plt.imshow(mraArray[:,:,i], cmap='bone')
#     plt.show()
#     time.sleep(0.05)


    
#plt.imshow(mraArray[:,:,50], cmap='bone')

#zproj=np.sum(mraArray,axis=2)
#plt.imshow(zproj, cmap='bone')


