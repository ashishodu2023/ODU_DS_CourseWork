#Import  necessary  libraries
import  pandas  as  pd
import  numpy  as  np
import  matplotlib.pyplot as  plt

#Read data  in  pandas   datframe
data  =  pd.read_csv("https://www.cs.odu.edu/~sampath/courses/data/brfss.csv",sep=',',encoding='UTF-8')
data.head()

#Select  necessary  fields
data.dropna(columns=['sex'],axis=1,inplace=True)

#Function to normalize the dataset
def  get_min_max(df):
  for   col in  df.columns:
    df[col]  =  (df[col] -df[col].min())/(df[col].max()-df[col].min())
  return  df

data_mix_max  = get_min_max(data)
#Show  normalized  data
data_mix_max.head()

#Draw  boxplot
data_mix_max.boxplot()