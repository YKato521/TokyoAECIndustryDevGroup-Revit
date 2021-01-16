import streamlit as st
import requests 
import numpy as np
import pandas as pd

BASE_URL = 'http://localhost:48884/route-sample/'

@st.cache
def get_title():
	url = BASE_URL + 'title'
	res= requests.get(url)
	if res.status_code == 200:
		return res.json()

@st.cache
def get_levels():
	name_list = []
	elevation_list = []
	url = BASE_URL + 'levels'
	res= requests.get(url)
	if res.status_code == 200:
		for l in res.json():
			name_list.append(l['name'])
			elevation_list.append(l['Elevation'])
		level_tuple = list(zip(name_list, elevation_list))
		chart_data = pd.DataFrame(
			level_tuple,
			columns = ['Level Name','Elevation'])
		return chart_data
@st.cache
def get_furnitures(option):
	url = BASE_URL + 'furniture'
	res= requests.get(url)
	if res.status_code == 200:
		if option == 'ファミリ':
			furniture_dict = res.json()['family']
		elif option == 'ファミリタイプ':
			furniture_dict = res.json()['family_type']
		chart_data = pd.DataFrame(
			furniture_dict.values(),
			index=furniture_dict.keys())
		return chart_data



# st.title(get_title())
st.subheader(" レベル表 ")
# st.dataframe(get_levels())
st.subheader(" 家具ファミリ別 ")
option = st.selectbox(
	'集計分類',
	('ファミリ', 'ファミリタイプ'))
st.bar_chart(get_furnitures(option))
