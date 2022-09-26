import streamlit as st
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_iris
#import altair as alt
import plotly.express as px


iris_data = load_iris()
labels = iris_data.feature_names
targets = iris_data.target
print(labels)
df_form = pd.DataFrame(iris_data.data, columns = labels)
df_form['targets'] = targets
st.write("""
# Iris Dataset

This dataset describes the variation of sepal length & width along with petal length & width 
for 3 species namely Setosa, Versicolor and Virginica """)
#alt_handle = alt.Chart(df_form).mark_circle(size=60).encode(x='alcohol', y='malic_acid', 
# color='hue', tooltip=['ash', 'magnesium', 
# 'proanthocyanins']).interactive()
#st.altair_chart(alt_handle)


df = px.data.iris()
fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_length',
              color='species')
fig.show()
st.plotly_chart(fig, sharing="streamlit")
