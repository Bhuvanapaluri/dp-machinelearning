import streamlit as st
import numpy as np
import pandas as pd

st.title('THE FIRST APP')

with st.expander('The data'):
  #st.write('**Raw data**')

data= pd.readcsv('/Applications/office_iot.csv)




