import itchat
import requests
import urllib
from bs4 import BeautifulSoup


def query(word):
    result = ''
    url = "http://dict.youdao.com/w/" + word  # urllib.urlencode(word)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    computer = soup.select('li[class="ptype_0 types"]')[
        0].select('span[class="title"]')[0]
    result += '计算机：' + computer.get_text()
    result += '\n\n'
    trans_list = soup.select(
        'div#phrsListTab > div.trans-container > ul')
    if(trans_list):
        lis = trans_list[0].find_all('li')
        for li in lis:
                result += li.contents[0]+'\n'

    sentences = soup.select('#bilingual ul li')
    for ss in sentences:
        result += '\n'
        for s in ss.find_all('p'):
            if(len(s.attrs) == 0):
                result += str.strip(s.get_text())
    return result


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    print(msg["Text"])
    txts = msg["Text"].split(' ')
    if(txts[0] == 'yd'):
        return query(txts[1])
    else:
        return "查询方式：yd 单词"


if __name__ == '__main__':
    # hotReload = True, 保持在线，下次运行代码可自动登录
    itchat.auto_login(hotReload=True)
    itchat.run()
#     print(query("time"))
