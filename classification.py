import numpy as np
import cv2
import os
import argparse
from shutil import copyfile

## Get arugments
parser = argparse.ArgumentParser()
parser.add_argument("--num_classes", type=int, required= True, help= "Number of classes you want to label")
parser.add_argument("--image_folder", type=str, required = True, help="The path of the folder that contain images you want to label")
parser.add_argument("--output", type=str, default = "./" , help="The output path of the labelled folders")
parser.add_argument("--resize", type=bool, default = False, help="If the image size is large and can't be displayed well, Make it True ")
parser.add_argument("--start", type=int, default = 0, help="The index of the image you want to start labelling from")
opt = parser.parse_args()
print(opt)


ZERO_KEY = ord('0')
q_KEY = ord('q')


dirs = os.listdir(opt.image_folder)
#os.chdir(opt.output)


# Create output directories
os.makedirs(opt.output+"/annotations",exist_ok=True)
for i in range(opt.num_classes):
	os.makedirs(opt.output+"/annotations/"+"Class_"+str(i),exist_ok=True)


idx = 0
last_key = None

# Start labelling
while idx < len(dirs):

        if idx < opt.start:
            idx +=1
            continue

        filename = dirs[idx]
        try:
            frame = cv2.imread(opt.image_folder+'/'+filename)
            FrameId = 'FrameId ' + '%010d'%(idx)
            print(FrameId)
            if opt.resize:
            	frame = cv2.resize(frame, (frame.shape[1]//2,frame.shape[0]//2))
            cv2.imshow(FrameId,frame)
            key = cv2.waitKey()
            cv2.destroyAllWindows()
        except:
            continue

        #print('key = ', key)
	
	# Keys from 0 to num_classes-1 is clicked -> label this image to the class chosen
        if (key >= ZERO_KEY and key < ZERO_KEY+ opt.num_classes):
            cls = key - ZERO_KEY
            copyfile(opt.image_folder+'/'+filename, opt.output+"/annotations/"+'Class_'+str(cls)+'/'+filename)
            print('Class = ', cls)

 	# ESC is clicked -> Get back to the previous image to label again 
        elif (key == 27):
            idx -= 1

            ## Check if the last image was labelled to remove it or neglected
            if (last_key >= ZERO_KEY and last_key < ZERO_KEY+ opt.num_classes):
            	cls = last_key - ZERO_KEY
            	filename_back = dirs[idx]
            	os.remove(opt.output+"/annotations/"+'Class_'+str(cls)+'/'+filename_back)
            	print("Image Removed!")
            idx -= 1


 	# q is clicked -> Exit the program 
        elif (key == q_KEY):
            break

	# Any other button is clicked -> Neglect this image
        else:
            print("Image not labelled")
            pass


        if np.shape(frame) == () :
            break



        idx+=1
        last_key = key
