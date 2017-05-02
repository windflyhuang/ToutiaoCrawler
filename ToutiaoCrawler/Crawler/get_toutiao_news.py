# coding：utf-8
import requests
import json

from ToutiaoCrawler.Model.keyword import keyword
from ToutiaoCrawler.Model.news import News


# 关键词搜索
from ToutiaoCrawler.Utils.Util import insert_data


def keyword_search(keyword):
    url = 'http://www.toutiao.com/search_content/?offset=0&format=json&keyword= ' + keyword + '&autoload=true&count=200&cur_tab=2'

    toutiao_data = requests.get(url).text

    data = json.loads(toutiao_data)
    items = data['data']

    news_list = []
    link_head = 'http://toutiao.com'

    for n in items:
        if 'title' in n:
            news = News()
            news.title = n['title']
            news.tag = n['tag']
            news.source = n['source']
            news.source_url = link_head + n['source_url']
            # 两会关键词
            news.keyword = keyword
            # 今日头条自带关键词
            news.keywords = n['keywords']

            news_list.append(news)
            #print(news.title, news.source_url, news.source, news.keyword, news.keywords)

    return news_list


# 相关搜索
def related_search(keyword):
    related_url = 'http://www.toutiao.com/search/related/?keyword=' + keyword
    related_data = requests.get(related_url).text
    related = json.loads(related_data)['data']
    for n in related:
        print(n)
        keyword_search(n)

for k in keyword.keyword:
  news_list = keyword_search(k)
  print(len(news_list))
  insert_data(news_list)