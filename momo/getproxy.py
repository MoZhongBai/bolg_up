import requests
import json
from lxml import etree

def get_ip_poxy():
    ip_list = []
    totals = requests.get('http://blog.kristian.top:8899/api/v1/proxies').text
    tatols = json.loads(totals)
    servers = tatols['proxies']
    for server in servers:
        ip = server['ip']
        port = str(server['port'])
        prox = ip+':'+port
        ip_list.append(prox)
    return ip_list

def get_artical_list(personal_url):
    arcical_title = []
    artical_dict = {}
    all_html = requests.get(personal_url)
    all_html = etree.HTML(all_html.content.decode('utf-8'))
    titles = all_html.xpath('//div[@class="article-list"]//h4/a/text()')
    hrefs = all_html.xpath('//div[@class="article-list"]//h4/a/@href')
    for title in titles:
        if title != '\n        ':
            arcical_title.append(title.strip())
    for title,href in zip(arcical_title,hrefs):
        artical_dict[title] = href
    return arcical_title,artical_dict,hrefs

# if __name__ == "__main__":
#     titles,artical_dict = get_artical_list('https://blog.csdn.net/dfgdgfbb')