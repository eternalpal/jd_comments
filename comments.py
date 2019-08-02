import requests
from lxml import etree
import json
import os
import random
import time

comment_path='jd_comment.txt' #评价文件保存的位置,和程序在同一个文件夹下


def get_comments_info(url):#获取商品评价信息,url为商品评论的链接    

    
    headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
            'Referer': 'https://item.jd.com/100003951612.html',
             
            }
    
    rec = requests.get(url=url,headers=headers,timeout=5)
    sleeptime=random.randint(0,5)#设置随机等待的秒数
    print('等待'+str(sleeptime)+'秒')
    time.sleep(sleeptime)

    comment = []
    if rec.status_code == 200:
        try:
            info = json.loads(rec.text) #评价信息
            info_list = info.get('comments')
            for info in info_list:
                comment.append(info.get('content').strip()) 
            print(comment)
        except:
            pass
            
    return comment

def save_txt(data):#保存评价内容到jd_comment.txt
    with open('jd_comment.txt', 'a') as f:
        f.write(data+'\n') 
        
if __name__ == '__main__':

    id=input("请输入要爬的商品id：")
    pages=input("请输入要爬取的评论页数：")

    if os.path.exists(comment_path):#若当前文件夹存在jd_comment.txt，则删除
        os.remove(comment_path)
    for page in range(0,int(pages)):#爬取评论页数
        url='https://sclub.jd.com/comment/productPageComments.action?productId={0}&score=0&sortType=5&page={1}&pageSize=10'.format(id,page)
        print('正在获取第{}页......'.format(page+1))
        for comment in get_comments_info(url):
            save_txt(comment)

        