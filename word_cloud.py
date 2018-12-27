#Importing the required packages
from wordcloud import *
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#Opening the file containing comments
fp=open("Desktop/Youtube_Comments.txt","r")
words=fp.read()

#Opening the image which is to used as a wordcloud mask
mask = np.array(Image.open('Desktop/v.jpg')) 

#Generating the wordcloud by specifying all the needed parameters
word_cloud = WordCloud(width=600,height=600,max_font_size=76,min_font_size=12,stopwords=STOPWORDS,mask=mask,colormap='Blues').generate(words)

plt.figure(figsize=(10,10))
plt.imshow(word_cloud)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()
