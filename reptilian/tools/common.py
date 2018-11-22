#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/8 1:08 AM
# @Author  : Nikky
# @Site    : 
# @File    : common.py
import hashlib, re, requests


def make_md5(str):
    m = hashlib.md5()
    m.update(str.encode('utf-8'))
    return m.hexdigest()


def get_md():
    url = "https://www.aigupiao.com/Dynamic/others?m_u_id=296904"
    result = requests.get(url)
    md = ""
    try:
        md = re.findall('var _Libs={"md":"(.*?)"}', result.text, re.S)[0]
    except:
        pass
    return md or None


def send_msg(url,data):
    requests.post(
        url,
        json=data
    )

def remove_html(html):
    dr = re.compile(r'<[^>]+>', re.S)
    dd = dr.sub('', html)
    return dd



if __name__ == '__main__':
    print(remove_html("【周五交易计划】继续只看创投，其余忽略。创投概念几个注意点：<br /><br />1、光洋股份11天10板，作为最佳小盘先锋，强封的资金格局不错，盘后却突发大额减持，极似恒立实业，玩得666，明日弱转强的预期基本消失了。<br /><br />2、市北高新作为高度龙头和外高桥的图形记忆，5日线趋势运行、每日新高，明日应出加速，但能否顶住不确定。另一中军鲁信创投延续筹码沉淀蓄势，明日反弹概率较大。日内龙头张江高科，资金每天都发动不同的大盘标的做冲锋，并不利于情绪的有效回拢。<br /><br />3、转势板群兴玩具为2波龙头气势，并引发高标企稳，分时和当初四川双马的2波首板相似，奈何炸板，明日如果反包上板，则应给予较多重视。<br /><br />4、连板标的前排普路通、赛象科技、华平股份、全新好、恒大高新，首板海泰发展。<br /><br />继续观察创投情绪，择机套利。<br /><br />龙神团队，今日唯一开仓新光圆成2%+，为安逸组套利操作。敢死队唯一持仓鲁信创投，继续坚守一下。"))
