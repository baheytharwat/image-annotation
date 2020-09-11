# image-annotation
A python script that helps in labelling images for image classification task.

## Dependencies
Make sure that you have installed:
- numpy
- opencv
- argparse

## Installation
##### Clone and install requirements
    $ git clone https://github.com/baheytharwat/image-annotation.git
    $ cd image-annotation/
    $ pip3 install -r requirements.txt
    
## How it works?

    $ python3 classification.py --image_folder <folder path> --num_classes  <number of classes>
    
For example, If the folder path you want to label its images is  `/home/bahey/data` and the number of classes are `3`. Then, The command will be:

    $ python3 classification.py --image_folder /home/bahey/data --num_classes 3 

#### For more options :
    $ python3 label.py --image_folder /home/bahey/data --num_classes 3 --output /home/bahey/data/output --start 100 --resize True 

- output: is the output path to save the labelled images. A folder called `annotations` is created and contains a folder to each class. `default=./` (The same directory with the code)
- start: is the index of the image you want to start labelling from. `default=0`
- resize: If the image is not displayed well because its large size, Make it True. `default=False`



## User manual

Accordingly to the number of classes you choose and the Images folder you specified, The images will be displayed to you and you can click:

- A number from `[0 : num_classes-1]` to label the image to the chosen class.
- `ESC` to get back to the previous image and relabel it.
- `q` to exit the program.
- Any other key will neglect the displayed image and not label it.

