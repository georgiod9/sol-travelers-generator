# This file MUST be configured in order for the code to run properly

# Make sure you put all your input images into an 'assets' folder. 
# Each layer (or category) of images must be put in a folder of its own.

# CONFIG is an array of objects where each object represents a layer
# THESE LAYERS MUST BE ORDERED.

# Each layer needs to specify the following
# 1. id: A number representing a particular layer
# 2. name: The name of the layer. Does not necessarily have to be the same as the directory name containing the layer images.
# 3. directory: The folder inside assets that contain traits for the particular layer
# 4. required: If the particular layer is required (True) or optional (False). The first layer must always be set to true.
# 5. rarity_weights: Denotes the rarity distribution of traits. It can take on three types of values.
#       - None: This makes all the traits defined in the layer equally rare (or common)
#       - "random": Assigns rarity weights at random. 
#       - array: An array of numbers where each number represents a weight. 
#                If required is True, this array must be equal to the number of images in the layer directory. The first number is  the weight of the first image (in alphabetical order) and so on...
#                If required is False, this array must be equal to one plus the number of images in the layer directory. The first number is the weight of having no image at all for this layer. The second number is the weight of the first image and so on...

# Be sure to check out the tutorial in the README for more details.                

CONFIG = [
    {
        'id': 1,
        'name': 'background',
        'directory': 'Background',
        'required': True,
        'rarity_weights': [7, 16.75, 16.75, 16.75, 3.67, 0.5, 0.5, 3.67, 16.75, 7, 3.67, 7],
    },
    {
        'id': 2,
        'name': 'skin',
        'directory': 'Skin',
        'required': True,
        'rarity_weights': [10, 75, 15],
    },
    {
        'id': 3,
        'name': 'facial hair',
        'directory': 'Facial Hair',
        'required': True,
        'rarity_weights': [25, 25, 20, 20, 7, 3],
    },
    {
        'id': 4,
        'name': 'eyes',
        'directory': 'Eyes',
        'required': True,
        'rarity_weights': [6, 6, 15, 3, 50, 15, 1, 1, 3],
    },
    {
        'id': 5,
        'name': 'outfit',
        'directory': 'Outfit',
        'required': True,
        'rarity_weights': [4.5, 15, 4.5, 20, 20, 0.5, 15, 20, 0.5],
    },
    {
        'id': 6,
        'name': 'hats',
        'directory': 'Hats',
        'required': True,
        'rarity_weights': [7, 3.7, 15, 0.5, 15, 15, 0.5, 3.7, 3.7, 7, 15, 7, 7],
    },
    {
        'id': 7,
        'name': 'accessories',
        'directory': 'Accessories',
        'required': True,
        'rarity_weights': [12, 4, 4, 65, 15],
    },
    
]
