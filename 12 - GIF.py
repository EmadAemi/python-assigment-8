from os import listdir
import imageio.v2
myfiles = listdir('images')
images = []
for i in range(len(myfiles)):
    image = imageio.v2.imread("images/" + myfiles[i])
    images.append(image)
imageio.v2.mimsave('myGif.gif', images)
