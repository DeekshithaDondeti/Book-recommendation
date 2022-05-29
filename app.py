#importing libraries
import streamlit as st
import pickle
import pandas as pd
import numpy as np


#reading the dataset
books_dict = pickle.load(open('book_dict.pkl','rb'))
books=pd.DataFrame(books_dict)

st.title('Book Recommendation System')
def index_of_Title(Title): #giving an input(book name) and finding the index of the input in dataset.
    c=0
    for i in range(0,books.shape[0]):
        if(Title==books['bookTitle'][i]):
            c=i
            break
    return c
#Taking cosine similarity matrix of the index of the input entered.
def similar_matrix(cs,Title):
    c=index_of_Title(Title)
    result = list(cs[c])
    sort_index = np.argsort(result)
    p = list(sort_index)
    p.reverse()
    return p

#recommending the books based on the cosine similarity matrix of the entered input i.e recommending books with highest cosine similarity value of that index.
def recommend_books(Title):

    b = similar_matrix(cs, Title)
    recommedations=[]
    recommedation_images = []
    book_disc=[]
    book_url=[]
    book_author = []
    for i in b:
        recommedations.append(str(books['bookTitle'][i]))
        recommedation_images.append( books['bookImage'][i] )
        book_author.append( 'Author:'+ str(books['bookAuthors'][i]))
        book_disc.append(str(books['bookDesc'][i]))
        book_url.append(books['url'][i])
    return recommedations,recommedation_images,book_url,book_author,book_disc

cs = pickle.load(open('similarity.pkl','rb'))

#giving an input(book name) and finding the index of the input in dataset.
selected_input = st.selectbox(
    'Enter book title',
    books['bookTitle'].values)

if st.button('Search'): #creating a drop down box to select a book title from the provided book title in dataset
   t,f,g,h,i=recommend_books(selected_input)
   col1, col2 = st.columns(2)
   col3, col4 = st.columns(2)
   col5, col6 = st.columns(2)
#recommending books based on the book title entered
   with col1:
       st.image(f[0], width=200, clamp=True)
       with st.expander(t[0]):
           st.write(h[0])
           st.write(i[0])
           st.write(g[0])
   with col2:
       st.image(f[1], width=200, clamp=True)
       with st.expander(t[1]):
           st.write(h[1])
           st.write(i[1])
           st.write(g[1])
   with col3:
       st.image(f[2], width=200, clamp=True)
       with st.expander(t[2]):
           st.write(h[2])
           st.write(i[2])
           st.write(g[2])
   with col4:
       st.image(f[3], width=200, clamp=True)
       with st.expander(t[3]):
           st.write(h[3])
           st.write(i[3])
           st.write(g[3])
   with col5:
       st.image(f[4], width=200, clamp=True)
       with st.expander(t[4]):
           st.write(h[4])
           st.write(i[4])
           st.write(g[4])
   with col6:
       st.image(f[5], width=200, clamp=True)
       with st.expander(t[5]):
           st.write(h[5])
           st.write(i[5])
           st.write(g[5])

sorted_ratings = books.sort_values(['bookRating'], ascending=[False])#sorting dataset based on the rating column
sorted_ratings = sorted_ratings.reset_index(drop=True)#sorting the indexes dataset based on the rating column

def sorted_rating(sorted_ratings): #recommending books based on rating
    k = []
    l=[]
    m=[]
    n=[]
    t = 0
    for i in range(0,sorted_ratings.shape[0]):
        if (t < 5):
            k.append(sorted_ratings['bookTitle'][i])
            l.append(sorted_ratings['bookImage'][i])
            m.append(sorted_ratings['bookAuthors'][i])
            n.append(sorted_ratings['url'][i])

            t = t + 1

    return k,l,m,n

st.subheader('High Rated') #creating a row of high rated books
k,l,m,n=sorted_rating(sorted_ratings)
col1, col2, col3 ,col4 ,col5= st.columns(5)

with col1:
    st.image(l[0], width=100, clamp=True)
    with st.expander(k[0]):
        st.write(m[0])
        st.write(n[0])
with col2:
    st.image(l[1], width=100, clamp=True)
    with st.expander(k[1]):
        st.write(m[1])
        st.write(n[1])
with col3:
    st.image(l[2], width=100, clamp=True)
    with st.expander(k[2]):
        st.write(m[2])
        st.write(n[2])
with col4:
    st.image(l[3], width=100, clamp=True)
    with st.expander(k[3]):
        st.write(m[3])
        st.write(n[3])
with col5:
    st.image(l[4], width=100, clamp=True)
    with st.expander(k[4]):
        st.write(m[4])
        st.write(n[4])

def genre_Fiction(sorted_ratings):#recommending high rated books based on the Fiction genre
    a=[]
    b=[]
    c=[]
    d=[]
    for i in range(0,sorted_ratings.shape[0]):
        if(str(sorted_ratings['bookGenres'][i]).find('Fiction')!=-1):

            if(len(a)<5):
                a.append(sorted_ratings['bookTitle'][i])
                b.append(sorted_ratings['bookImage'][i])
                c.append(sorted_ratings['bookAuthors'][i])
                d.append(sorted_ratings['url'][i])

    return a,b,c,d


st.subheader('Fiction') #creating a row of genre with highted books of fiction genre
a,b,c,d=genre_Fiction(sorted_ratings)

col1, col2, col3 ,col4 ,col5= st.columns(5)

with col1:
    st.image(b[0], width=100, clamp=True)
    with st.expander(a[0]):
        st.write(c[0])
        st.write(d[0])
with col2:
    st.image(b[1], width=100, clamp=True)
    with st.expander(a[1]):
        st.write(c[1])
        st.write(d[1])
with col3:
    st.image(b[2], width=100, clamp=True)
    with st.expander(a[2]):
        st.write(c[2])
        st.write(d[2])
with col4:
    st.image(b[3], width=100, clamp=True)
    with st.expander(a[3]):
        st.write(c[3])
        st.write(d[3])
with col5:
    st.image(b[4], width=100, clamp=True)
    with st.expander(a[4]):
        st.write(c[4])
        st.write(d[4])

def genre_Fantasy(sorted_ratings):#recommending books based on genres-Fanstasy
    a=[]
    b=[]
    c=[]
    d=[]
    for i in range(len(sorted_ratings)):
        if(str(sorted_ratings['bookGenres'][i]).find('Fantasy')!=-1):

            if(len(a)<5):
                a.append(sorted_ratings['bookTitle'][i])
                b.append(sorted_ratings['bookImage'][i])
                c.append(sorted_ratings['bookAuthors'][i])
                d.append(sorted_ratings['url'][i])

    return a,b,c,d


st.subheader('Fantasy')#creating a row of genre with highted books of fantasy genre
p,q,r,s=genre_Fantasy(sorted_ratings)

col1, col2, col3 ,col4 ,col5= st.columns(5)

with col1:
    st.image(q[0], width=100, clamp=True)
    with st.expander(p[0]):
        st.write(r[0])
        st.write(s[0])
with col2:
    st.image(q[1], width=100, clamp=True)
    with st.expander(p[1]):
        st.write(r[1])
        st.write(s[1])
with col3:
    st.image(q[2], width=100, clamp=True)
    with st.expander(p[2]):
        st.write(r[2])
        st.write(s[2])
with col4:
    st.image(q[3], width=100, clamp=True)
    with st.expander(p[3]):
        st.write(r[3])
        st.write(s[3])
with col5:
    st.image(q[4], width=100, clamp=True)
    with st.expander(p[4]):
        st.write(r[4])
        st.write(s[4])

def genre_Biography(sorted_ratings):#recommending books based on genres-Biography
    a=[]
    b=[]
    c=[]
    d=[]
    for i in range(len(sorted_ratings)):
        if(str(sorted_ratings['bookGenres'][i]).find('Biography')!=-1):

            if(len(a)<5):
                a.append(sorted_ratings['bookTitle'][i])
                b.append(sorted_ratings['bookImage'][i])
                c.append(sorted_ratings['bookAuthors'][i])
                d.append(sorted_ratings['url'][i])

    return a,b,c,d


st.subheader('Biography')#creating a row of genre with highted books of Biography genre
p,q,r,s=genre_Biography(sorted_ratings)

col1, col2, col3 ,col4 ,col5= st.columns(5)

with col1:
    st.image(q[0], width=100, clamp=True)
    with st.expander(p[0]):
        st.write(r[0])
        st.write(s[0])
with col2:
    st.image(q[1], width=100, clamp=True)
    with st.expander(p[1]):
        st.write(r[1])
        st.write(s[1])
with col3:
    st.image(q[2], width=100, clamp=True)
    with st.expander(p[2]):
        st.write(r[2])
        st.write(s[2])
with col4:
    st.image(q[3], width=100, clamp=True)
    with st.expander(p[3]):
        st.write(r[3])
        st.write(s[3])
with col5:
    st.image(q[4], width=100, clamp=True)
    with st.expander(p[4]):
        st.write(r[4])
        st.write(s[4])

def genre_Classics(sorted_ratings):#recommending books based on genre-Classics
    a=[]
    b=[]
    c=[]
    d=[]
    for i in range(len(sorted_ratings)):
        if(str(sorted_ratings['bookGenres'][i]).find('Classics')!=-1):

            if(len(a)<5):
                a.append(sorted_ratings['bookTitle'][i])
                b.append(sorted_ratings['bookImage'][i])
                c.append(sorted_ratings['bookAuthors'][i])
                d.append(sorted_ratings['url'][i])

    return a,b,c,d


st.subheader('Classics')#creating a row of genre with highted books of Classics genre
p,q,r,s=genre_Classics(sorted_ratings)

col1, col2, col3 ,col4 ,col5= st.columns(5)

with col1:
    st.image(q[0], width=100, clamp=True)
    with st.expander(p[0]):
        st.write(r[0])
        st.write(s[0])
with col2:
    st.image(q[1], width=100, clamp=True)
    with st.expander(p[1]):
        st.write(r[1])
        st.write(s[1])
with col3:
    st.image(q[2], width=100, clamp=True)
    with st.expander(p[2]):
        st.write(r[2])
        st.write(s[2])
with col4:
    st.image(q[3], width=100, clamp=True)
    with st.expander(p[3]):
        st.write(r[3])
        st.write(s[3])
with col5:
    st.image(q[4], width=100, clamp=True)
    with st.expander(p[4]):
        st.write(r[4])
        st.write(s[4])

def genre_History(sorted_ratings):#recommending books based on genres-History
    a=[]
    b=[]
    c=[]
    d=[]
    for i in range(len(sorted_ratings)):
        if(str(sorted_ratings['bookGenres'][i]).find('History')!=-1):

            if(len(a)<5):
                a.append(sorted_ratings['bookTitle'][i])
                b.append(sorted_ratings['bookImage'][i])
                c.append(sorted_ratings['bookAuthors'][i])
                d.append(sorted_ratings['url'][i])

    return a,b,c,d


st.subheader('History')#creating a row of genre with highted books of History genre
p,q,r,s=genre_History(sorted_ratings)

col1, col2, col3 ,col4 ,col5= st.columns(5)

with col1:
    st.image(q[0], width=100, clamp=True)
    with st.expander(p[0]):
        st.write(r[0])
        st.write(s[0])
with col2:
    st.image(q[1], width=100, clamp=True)
    with st.expander(p[1]):
        st.write(r[1])
        st.write(s[1])
with col3:
    st.image(q[2], width=100, clamp=True)
    with st.expander(p[2]):
        st.write(r[2])
        st.write(s[2])
with col4:
    st.image(q[3], width=100, clamp=True)
    with st.expander(p[3]):
        st.write(r[3])
        st.write(s[3])
with col5:
    st.image(q[4], width=100, clamp=True)
    with st.expander(p[4]):
        st.write(r[4])
        st.write(s[4])


