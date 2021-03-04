root = "/home/lucien/Desktop/rec_systems"
datapath = root + "/data"

import numpy as np 
import pandas as pd 

#importing csv data 
creds = pd.read_csv(datapath + "/credits.csv")
keywords = pd.read_csv(datapath + "/keywords.csv")
links = pd.read_csv(datapath + "/links.csv")
links_small = pd.read_csv(datapath + "/links_small.csv")
metadata = pd.read_csv(datapath + "/movies_metadata.csv")
ratings = pd.read_csv(datapath + "/ratings.csv")
ratings_small = (datapath + "/ratings_small.csv")

#metadata
metadata.head(3)


################################################
# Recommender based on product description 
################################################

#We are using textual data (text description), and therefore we will convert the text into a bow or tfidf matrix 
metadata['overview'].head()

#checking for missing values 
metadata['overview'].isnull().any() #True 
#imputing missing values 
metadata[metadata['overview'].isnull()] = ""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import cosine_similarity

tfidf = TfidfVectorizer(stop_words='english')

tfidf_matrix = tfidf.fit_transform(metadata['overview'])
#checking shape 
tfidf_matrix.shape #75827 = vocabulary size = features size 

#Features names 
f_names = tfidf.get_feature_names()

#Getting cosine similarities 
cs1 = linear_kernel(tfidf_matrix, tfidf_matrix) #since it is tfidf, we can calculate the dot product. 
cs2 = cosine_similarity(tfidf_matrix, tfidf_matrix)

