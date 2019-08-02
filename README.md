# jd_comments - 爬取京东商品评论信息

comments.py即为源代码，直接python运行即可。开始运行需要输入两个参数：商品id和评论页数，之后程序自动爬取，
内容保存在jd_comment.txt文件。

ciyun_jichu.py则是将爬取的评论通过词云展现出来，用的jieba中文分词，效果如下：

![词云效果](https://github.com/eternalpal/jd_comments/blob/master/jd_comment.jpg)

ciyun_textrank-extract_tags.py则思通过textrank/extract_tags两种方式提取关键词后，再用词云展现出来。
