import os
import imageio

myfiles = os.listdir('giff') #esme axa
images = []
for i in range(len(myfiles)):
    image = imageio.imread('giff/'+ myfiles[i]) #name folder + esme har file
    images.append(image) #khode axa
imageio.mimsave('nazanin.gif',images)    