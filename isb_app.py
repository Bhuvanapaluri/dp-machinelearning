import streamlit as st
import numpy as np
import pandas as pd

st.title('THE FIRST APP')

with st.expander('The data'):
  st.write('**Raw data**')
  data= pd.readcsv('https://raw.githubusercontent.com/dataprofessor/data/master/mushrooms.csv')
  df




