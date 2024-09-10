import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')


movies=movies.merge(credits,on='title')

#genres
#id
#keywords
#title
#overview
#cast
#crew//director

movies=movies[['movie_id','title','overview','genres','keywords','cast','crew']]

movies.isnull().sum()

movies.duplicated().sum()

movies.dropna(inplace=True)
import ast #aaplyakad ji geners aahe ti string madhe aahe manun tyala aapn list madhe 
#convert karu shakto ast.literal_eval() function ne
def convert(obj):
  L=[]
  for i in ast.literal_eval(obj):
    L.append(i['name'])
  return L

movies['genres']=movies['genres'].apply(convert)
movies['keywords']=movies['keywords'].apply(convert)

def convert3(obj):
  L=[]
  counter=0
  for i in ast.literal_eval(obj):
    if counter !=3:
      L.append(i['name'])
      counter=counter+1
    else:
      break
  return L

movies['cast']=movies['cast'].apply(convert3)
def fetch_director(obj):
  L=[]
  for i in ast.literal_eval(obj):
    if i['job']=='Director':
      L.append(i['name'])
      break
  return L

movies['crew']=movies['crew'].apply(fetch_director) 

movies['overview']=movies['overview'].apply(lambda x:x.split())


movies['genres']=movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])
movies['keywords']=movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
movies['cast']=movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
movies['crew']=movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])

movies['tags']=movies['overview']+movies['genres']+movies['keywords']+movies['cast']+movies['crew']

new_df=movies[['movie_id','title','tags']]

new_df['tags']=new_df['tags'].apply(lambda x:" ".join(x))

new_df['tags']=new_df['tags'].apply(lambda x:x.lower()) 
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()

def stem(text):
  y=[]
  for i in text.split():
    y.append(ps.stem(i))
  return " ".join(y)

new_df['tags']=new_df['tags'].apply(stem)

from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=5000,stop_words='english')


vectors =cv.fit_transform(new_df['tags']).toarray()

cv.get_feature_names_out()
from sklearn.metrics.pairwise import cosine_similarity
cosine_similarity(vectors)

similarity=cosine_similarity(vectors)

def recommend(movie):
  movie_index=new_df[new_df['title']==movie].index[0]
  distances=similarity[movie_index]
  movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
  for i in movies_list:
    print(new_df.iloc[i[0]].title)
    
    
# print(recommend('Avatar'))



