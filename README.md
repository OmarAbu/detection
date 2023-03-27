#will be posting the model soon

# detection
Credit to Kaggle.. All training data and csv folders that I used can be found at https://www.kaggle.com/competitions/siim-isic-melanoma-classification/data.
# Part 1
 I first parsed through the train.csv and test.csv files to olny have 3 columns. The first column I wanted was the image_name, benign or malignant which I renamed to BE_OR_ME, and finally the last column which is a value representation if the image has benign (value of 1) or malignant mole (value of 0).
# Part 2
Used tensroflow to build a CNN (Convolution Neural Network) using features of the train imaged to help teach the model whether a mole is benign or malignant. 

# Part 3
working on a website with flask to allow users to ask the website and upload images to the website so that the model can give the user and idea of how likley their mole is benign or malignant.

# Disclamer
for any path variables in python, I had to copy the full path i.e store the 30,000+ images into a hardrive than copy an absolute path to it for tensorflow to recognize a folder of images even exist. 

#Required: tensorflow, jupyter notebook, flask 


