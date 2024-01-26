import numpy as np
import pandas as pd

population=1000
rounds=40

val_min = 0
val_max = 1
variation = (val_max - val_min)/2
std_dev = variation/3
mean = (val_max + val_min)/2
# create a normal distribution of "smartness" in the population
dist_normal = np.random.normal(mean, std_dev,  population)
df = pd.DataFrame(dist_normal)
df.columns=['iq']
df.iq=round(df.iq,2)
df['wealth']=100   #everyone starts with 100
print(df)

life_events=pd.DataFrame()

df['luck']=0  # normal or lucky events after rounds of simulations
df['last5']=0  # normal or lucky events in the last 5 rounds
for i in range(rounds):
    events_array = np.random.randint(3, size=(population))

    events=pd.DataFrame(events_array)
    life_events['day{}'.format(i)]= events
    df['event']=events

    # like monopoly, everyone gets 100 into next round in the first half 
    if i <=(rounds/2):
        df.wealth=df.wealth.add(100)
    df.wealth = round(df.apply(lambda x: x.wealth*0.5 if x.event ==0  else x.wealth+100*(1+x.iq), axis=1),2)
    df.luck = df.apply(lambda x: x.luck if x.event ==0  else x.luck+1, axis=1)

    if i>=(rounds-5):
        df.last5 = df.apply(lambda x: x.last5 if x.event ==0  else x.last5+1, axis=1)


life_events['iq']=df['iq']
life_events['wealth']=df['wealth']
life_events['luck']=df['luck']
life_events['last 5']=df['last5']
life_events.to_csv("./life.csv")


# plot the diagram
import plotly.express as px

fig1 = px.histogram(df, x="wealth")
#fig.show()
fig2 = px.scatter(life_events,x="iq", y="wealth")
fig3 = px.scatter(life_events,x="luck",y="wealth")
fig4 = px.scatter(life_events,x="last 5",y="wealth")

with open('./life.html', 'w') as f:
    f.write(fig1.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(fig2.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(fig3.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(fig4.to_html(full_html=False, include_plotlyjs='cdn'))
