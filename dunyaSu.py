import pandas as pd #lineer algebra
import numpy as np #data processing
import seaborn as sbn #visualization görselleştirme
import matplotlib.pyplot as plt #visualization görselleştirme
import plotly.express as px


import missingno as msno #kayıp veri analizi


from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV ,RepeatedStratifiedKFold ,train_test_split
from sklearn.metrics import precision_score,confusion_matrix

from sklearn import tree



df=pd.read_csv("water_potability.csv")
d =pd.DataFrame(df["Potability"].value_counts())


fig=px.pie(d,values="Potability", names=["Not Potable","Potable"],hole=0.35,opacity=0.8,
              labels={"label":"Potability","Potability":"Number of Samples"})



fig.update_layout(title = dict(text= "Pie Chart of Potability Feature")) #tablo başlığımız cls

fig.update_traces(textposition= "outside",textinfo="pecent+Label")  #figure üzerine gelindiğinde açılacak yazı 
fig.show() #figürü aç 


fig.write_html("icilebilirSu.html")  #figürü kaydetme 