#Import  necessary  libraries
import  pandas  as  pd
import  numpy  as  np
import  matplotlib.pyplot as  plt
import  seaborn as  sns

url ='https://www.cs.odu.edu/~sampath/courses/data/brfss.csv'
brfss_data  =  pd.read_csv(url,sep=',',encoding='UTF-8')
brfss_data

# Clean dataframe
def  cleanBRFSSFrame(df):
  df.drop(columns=['sex'],axis=1,inplace=True)
  df.dropna(how='any', inplace=True)
  return  df
clean_brfss_data  =  cleanBRFSSFrame(brfss_data)

#Shoe  clean  dataset
clean_brfss_data

#Describe  weight  field
clean_brfss_data['weight2'].describe()

#Function to  quantiles.
def  get_qauntiles(df):
  qaunt_25=df['age'].quantile(.25)
  qaunt_50=df['age'].quantile(.5)
  qaunt_70=df['age'].quantile(.7)

  return  qaunt_25,qaunt_50,qaunt_70


qaunt_25,qaunt_50,qaunt_70= get_qauntiles(clean_brfss_data)
print(f'25th, 50th, 70th percentile of the age  are  {qaunt_25},{qaunt_50}  and  {qaunt_70}')


#Plot  voilin plot  for  heights
ax=sns.violinplot(clean_brfss_data['htm3'])
ax.set_xlabel('Voilinplot')
ax.set_ylabel('Height')
ax.set_title('Distribution of Height in BRFSS  data', fontsize=16);