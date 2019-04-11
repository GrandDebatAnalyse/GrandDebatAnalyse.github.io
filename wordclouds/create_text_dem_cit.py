import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

stpW = stopwords.words("french")
stpW += ['tous','les','aussi','plus','c\'est','France','etc','notamment','car', 'peut', 'être', 'devrait', 'peut être', 'doivent être', 'bonne chose', 'grand débat'
        'si','autre','autres','fait','non','donc','ainsi','surtout','alors','exemple',
         'comme','encore','dont','peut-être','cela','Oui','Non','Cest','ils','Ils','il','Il','Les','les','en', 'ça','LA','quil','Que','Si','si','faut','je','Je','chaque','dun','nest','doit']



cols = [i for i in range(11)]

df = pd.read_csv('data/DEMOCRATIE_ET_CITOYENNETE.csv', low_memory=False)
df.drop(df.columns[cols],axis=1,inplace=True)
text =  pd.Series(df.fillna('').values.tolist()).str.join(' ')
allTextQ1 = ' '.join(list(text.dropna()))
clean = [word for word in allTextQ1.split() if word not in stpW]
cleanQ = ' '.join(clean)

with open('data/AllTextDemCit.txt','w') as f:
    f.write(str(cleanQ))