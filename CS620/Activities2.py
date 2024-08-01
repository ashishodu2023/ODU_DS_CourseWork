#Necessary  libraries
import pandas as  pd
import  numpy   as   np

#Empty list  for  height
height  =[]
h = [159, 171, 158, 162, 162, 177, 160, 175, 168, 171, 178, 178, 173, 177, 164]
#Sorting  height in  ascending  order
h.sort()
#Creating  the  list  of  sorted  height
height=[value  for  value   in h ]
print(height)

#Empty  dictionary
data  =  {}
#Creating  dictionary  with  label as 'h'
data  =  {'h':height}
#Creating pandas dataframe using   data  dictionary
df = pd.DataFrame(data)
df.head(5)


#Function  for  systematic  sampling
def systematic_sampling(df, step): 
    idx = np.arange(0, len(df), step=step)
    sys_sample = df.iloc[idx]
    return sys_sample

#Example 1
sys_sample = systematic_sampling(df, 5)
# View sampled data frame
print(sys_sample)

#Example  2
sys_sample = systematic_sampling(df, 2)
# View sampled data frame
print(sys_sample)