# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re

wiki = pd.read_csv('/Users/y-unus/Documents/FS2022_Classes/CMSE830 - Foundations of DS/Projects/train_1.csv')

header  = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title('Work in Progress!')
    st.text('Here I am currently trying to find a trend in the dataset for page visits based on \n language')
    
with dataset:
    st.header('Wiki Traffic Forecasting Dataset')
    st.text('As the dataset contains articles which are URLs, relevant information has to stripped \n from these strings')
    st.write(wiki.head(12))
    
with features:
    st.header('Features available in the dataset')
    st.text('The language feature consists of 8 langugaes. Unfortunately, the language set is not \n as diverse as I had hoped')
    
    def get_language(page):
        res = re.search('[a-z][a-z].wikipedia.org',page)
        if res:
            return res[0][0:2]
        return 'na'

    wiki['Language'] = wiki.Page.map(get_language)

    from collections import Counter

    print(Counter(wiki.Language))
    
    lang_sets = {}
    lang_sets['en'] = wiki[wiki.Language=='en'].iloc[:,0:-1]
    lang_sets['ja'] = wiki[wiki.Language=='ja'].iloc[:,0:-1]
    lang_sets['de'] = wiki[wiki.Language=='de'].iloc[:,0:-1]
    lang_sets['na'] = wiki[wiki.Language=='na'].iloc[:,0:-1]
    lang_sets['fr'] = wiki[wiki.Language=='fr'].iloc[:,0:-1]
    lang_sets['zh'] = wiki[wiki.Language=='zh'].iloc[:,0:-1]
    lang_sets['ru'] = wiki[wiki.Language=='ru'].iloc[:,0:-1]
    lang_sets['es'] = wiki[wiki.Language=='es'].iloc[:,0:-1]

    sums = {}
    for key in lang_sets:
        sums[key] = lang_sets[key].iloc[:,1:].sum(axis=0) / lang_sets[key].shape[0]

    days = [r for r in range(sums['en'].shape[0])]
    
    for key in sums:
        st.line_chart(wiki, x = days, y = sums[key])

with model_training:
    st.header('Coming Soon... to a classroom near you!')