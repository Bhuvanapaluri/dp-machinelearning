import streamlit as st
import numpy as np
import pandas as pd

st.title('THE FIRST APP')

with st.expander('The data'):
  st.write('**Raw data**')
  df= pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/mushrooms.csv')
  df

  st.write('**class and color**')
  class_raw = df[['gill-size', 'gill-spacing']]
  class_raw

  with st.expander('Data visualization'):
  st.scatter_chart(data=df, x='gill-size', y='gill-spacing', color='pink')



