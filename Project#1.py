import matplotlib.pyplot as mp
import pandas as pd
import numpy as np
import seaborn as sns
# read function
df = pd.read_csv(r'C:\Users\rocke\Desktop\Python\test.csv')
print(df)
ByRC=df.groupby(['ResponseName','RecommendationCount','Metacritic','PriceInitial','recomend/price'])["RecommendationCount"].agg(["sum"]).reset_index().sort_values(by="sum",ascending=False)
ByRC.head(250)
xvalues=df['ResponseName'].tolist()
y1values=df['Metacritic'].tolist()
y2values=df['PriceInitial'].tolist()
y3values=df['RecommendationCount'].tolist()



#method to divide the recomendation score by number
def outcome(rec,iprice):


	if iprice > 0 and iprice <=5:
		return rec/1


	elif iprice > 5 and iprice <= 10: 
	 	return rec/2

	elif iprice > 10 and iprice <= 20:
	 	return rec/3
	  

	elif iprice > 20 and iprice <= 35:
	 	return rec/4

	elif iprice > 35 and iprice <= 55:
	 	return rec/5

	elif iprice > 55:
	 	return rec/6


#create culumn of price group to recomendation score.
df['recomend/price']=df.apply(lambda x: outcome(x.RecommendationCount,x.PriceInitial), axis=1)

print(df)

#df.to_csv('test.csv')

# create graph of release to rec/Intial price

mp.figure(figsize=(20,8))
graph=sns.lineplot(x='ResponseName',y='recomend/price',palette="rocket",data=ByRC.head(50),linestyle="solid")
graph=sns.lineplot(x='ResponseName',y='RecommendationCount',palette="rocket",data=ByRC.head(50),linestyle="--")
graph.set_title('Top 50 Games by Recommendation Count')
mp.xticks(rotation=90)
mp.legend()
mp.ylabel ('number of recommendations')
mp.show()




# Bar grapgh of price catagorey 



bar=dict(zip(df.RecommendationCount,df.PriceInitial))

counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
counter6 = 0

for k,iprice in bar.items():


	if iprice > 0 and iprice <=5:
		counter1  = counter1 + k


	elif iprice > 5 and iprice <= 10: 
	 	counter2 = counter2 + k

	elif iprice > 10 and iprice <= 20:
	 	counter3 = counter3 + k
	  

	elif iprice > 20 and iprice <= 35:
	 	counter4 = counter4 + k

	elif iprice > 35 and iprice <= 55:
	 	counter5 = counter5 + k

	elif iprice > 55:
	 	counter6 = counter6 + k

priceRange = ['0-5','5-10','10-20','20-35','35-55','55 and over']
RecommendationCount = [counter1,counter2,counter3,counter4,counter5,counter6] 

ax = mp.bar (priceRange, RecommendationCount)
mp.bar_label(ax,fmt='%d')
mp.title ('Price range recommendations')
mp.xlabel ('Price ranges')
mp.ylabel ('number of recommendations')
mp.show()