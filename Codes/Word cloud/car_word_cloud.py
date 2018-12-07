from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
#from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image
df=pd.read_csv("cleaned_carscom.csv",encoding="latin1")
df9=df[['make','model']]
df10=(df9.groupby(['fullN']).size()).reset_index()
df10.columns=['fullN','NO']
df11=df10.sort_values(by=['NO'], ascending=False).reset_index(drop=True)
df11=df11.set_index('fullN')
dt=df11.to_dict()["NO"]



text = df9.fullN.values
wine_mask = np.array(Image.open("c6.png"))
print(wine_mask)
def transform_format(val):
    if val == 0:
        return 255
    else:
        return val
# Transform your mask into a new one that will work with the function:
transformed_wine_mask = np.ndarray((wine_mask.shape[0],wine_mask.shape[1]), np.int32)

for i in range(len(wine_mask)):
    transformed_wine_mask[i] = list(map(transform_format, wine_mask[i]))


wordcloud = WordCloud(contour_width=1,mask=transformed_wine_mask,width = 1000, height = 500,max_words=70, background_color="white",collocations = False,).generate_from_frequencies(dt)
plt.figure(figsize=(20,10))
plt.imshow(wordcloud)
plt.axis("off")
#plt.savefig(t+".png", bbox_inches='tight')
#print(t+":")
plt.show()
