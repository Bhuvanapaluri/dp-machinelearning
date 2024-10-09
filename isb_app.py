import streamlit as st
import numpy as np
import pandas as pd

st.title('THE FIRST APP')

with st.expander('The data'):
  st.write('**Raw data**')
  df= pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/mushrooms.csv')
  df

  st.write('**class and color**')
  class_raw = df[['class', 'color']]
  class_raw



