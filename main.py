import requests
import json
import time
import pandas as pd

'''

test= requests.get('https://api.coingecko.com/api/v3/coins/list')
r=test.json()
lits=[]

with open('list.json','r') as f:
	json_data=json.load(f)

# print(json.dumps(json_data, indent="\t"))

for yoso in r:
	for tic in json_data["coin"]:
		if(yoso["symbol"]==tic):
			lits.append(yoso["id"])

with open("tic.json",'w') as outp:
	json.dump(lits,outp,indent='\t')

'''

'''
cp={"coins":[]}

with open('tic.json','r') as f:
	tics=json.load(f)

for i in range(len(tics)):
	real=requests.get("https://api.coingecko.com/api/v3/coins/"+tics[i]+"/market_chart?vs_currency=usd&days=30&interval=daily")
	print(tics[i], real)
	reals=real.json()["prices"]

	excp ={}
	excp["names"]=tics[i]
	excp["prices"]=reals
	cp["coins"].append(excp)
	time.sleep(0.01)

print('finish')


with open("text.json","w") as outp:
	json.dump(cp,outp,indent='\t')
'''

with open('text.json','r') as f:
	tics=json.load(f)

df = pd.DataFrame( tics["coins"]["names"])
df.to_csv('out.csv', header=True, index=True,encoding='ms949')