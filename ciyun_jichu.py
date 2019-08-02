import jieba.analyse
#import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator

f=open('jd_comment.txt','r')  
contents=f.read()

cut_text = " ".join(jieba.lcut(contents))

wc = WordCloud(font_path='/usr/share/fonts/winfonts/simfang.ttf',
               background_color='White',
               max_words=1000,
               width=1000,
               height=500,
               #mask=graph,
               scale=1,
               #stopwords=['']#
               )
#font_path：设置字体，max_words：出现的最多词数量，mask参数=图片背景，必须要写上，另外有mask参数再设定宽高是无效的

wc.generate(cut_text)

#plt.imshow(wc)

#plt.axis("off")#取消坐标
#plt.show()
wc.to_file("jd_comment.jpg")