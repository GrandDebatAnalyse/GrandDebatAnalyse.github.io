import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from os import path
import os
from nltk.corpus import stopwords
from PIL import Image
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from wordcloud import WordCloud


stpW = stopwords.words("french")
stpW += ['tous','les','aussi','plus','c\'est','France','etc','notamment','car', 'peut', 'être', 'devrait', 'peut être', 'doivent être', 'bonne chose', 'grand débat'
        'si','autre','autres','fait','non','donc','ainsi','surtout','alors','exemple',
         'comme','encore','dont','peut-être','cela','Oui','Non','Cest','ils','Ils','il','Il','Les','les','en', 'ça','LA','quil','Que','Si','si','faut','je','Je','chaque','dun','nest','doit']




d = os.getcwd()
text = open(path.join(d, 'data/AllTextTransEco.txt')).read()


mask =  np.array(Image.open(path.join(d, "leaf.jpg")))

wc = WordCloud(font_path="din/DINCondensed-Bold.ttf", background_color="white", max_words=55, mask=mask,
               stopwords=stpW, contour_width=3, contour_color='white')
wc.generate(text)

wc.to_file(path.join(d, "TranEco.png"))


plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()
