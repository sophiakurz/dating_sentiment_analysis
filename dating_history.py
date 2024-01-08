#!/usr/bin/env python
# coding: utf-8

# # A *Brief* Tour of My Breakups Through Texts

# As a heterosexual, college-aged woman, my dating pool, unfortunately, consists of college-aged men. Using sentiment analysis and text extraction, I wanted to determing the Subjectivity and Polarity of my ex's text messages from either immediately before or immemidiately after we decided to end things. As you go through this code, My hope is that you don't find my dating history realatable, but I do hope you find it entertaining.
# 
# Polarity is an attribute of sentiment analysis in which the output  lies between -1 and 1, where -1 refers to a negative sentiment and +1 refers to positive sentiment.
# 
# Subjectivity is the output that lies within 0 and 1, and refers to personal opinions and judgments.
# 
# All identities have been anonymized, and each individual is identified only by an initial (C, A, J, or G).

# In[93]:


#Importing neccesary packages

from PIL import Image
import pytesseract
import glob
import matplotlib.pyplot as plt
from textblob import TextBlob

path_to_tesseract = r"/opt/homebrew/bin/tesseract"
pytesseract.pytesseract.tesseract_cmd = path_to_tesseract


# In[92]:


C = Image.open("texts_from_exs/C.jpeg")
display(C)

pytesseract.tesseract_cmd = path_to_tesseract 
C_text = pytesseract.image_to_string(C) 
print(C_text)

blob = TextBlob(C_text)
polarity = blob.polarity
subjectivity = blob.subjectivity
print("Polarity =", polarity)
print("Subjectivity =", subjectivity)

print()

if polarity > 0.2:
    sentiment = "Positive"
elif polarity < -0.2:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

if subjectivity > 0.5:
    objectivity = "Subjectivity"
else:
    objectivity = "Objective"

print(f"Sentiment: {sentiment}")
print(f"Objectivity: {objectivity}")


# In[90]:


A = Image.open("texts_from_exs/A.jpeg")

new_size = (700, 800)

A = A.resize(new_size)

display(A)

pytesseract.tesseract_cmd = path_to_tesseract 
A_text = pytesseract.image_to_string(A) 
print(A_text)

blob = TextBlob(A_text)
polarity = blob.polarity
subjectivity = blob.subjectivity
print("Polarity =", polarity)
print("Subjectivity =", subjectivity)

print()

if polarity > 0.2:
    sentiment = "Positive"
elif polarity < -0.2:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

if subjectivity > 0.5:
    objectivity = "Subjectivity"
else:
    objectivity = "Objective"

print(f"Sentiment: {sentiment}")
print(f"Objectivity: {objectivity}")


# In[87]:


J = Image.open("texts_from_exs/J.jpeg")
display(J)

pytesseract.tesseract_cmd = path_to_tesseract 
J_text = pytesseract.image_to_string(J) 
print(J_text)

blob = TextBlob(J_text)
polarity = blob.polarity
subjectivity = blob.subjectivity
print("Polarity =", polarity)
print("Subjectivity =", subjectivity)

print()

if polarity > 0.2:
    sentiment = "Positive"
elif polarity < -0.2:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

if subjectivity > 0.5:
    objectivity = "Subjectivity"
else:
    objectivity = "Objective"

print(f"Sentiment: {sentiment}")
print(f"Objectivity: {objectivity}")


# In[88]:


path_to_tesseract = r"/opt/homebrew/bin/tesseract"
image_path = r"texts_from_exs/G.jpeg"

G = Image.open(image_path)
display(G)

pytesseract.tesseract_cmd = path_to_tesseract 
G_text = pytesseract.image_to_string(G) 
print(G_text)

blob = TextBlob(G_text)
polarity = blob.polarity
subjectivity = blob.subjectivity
print("Polarity =", polarity)
print("Subjectivity =", subjectivity)

print()

if polarity > 0.2:
    sentiment = "Positive"
elif polarity < -0.2:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

if subjectivity > 0.5:
    objectivity = "Subjectivity"
else:
    objectivity = "Objective"

print(f"Sentiment: {sentiment}")
print(f"Objectivity: {objectivity}")

