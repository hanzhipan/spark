import urllib.request
import re


def get_html(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def get_data(html):
    data_re = r'<td class ="(normal|current) (.+) change_color col\d+ row(.+)" rank="(.+)?">(.+)?</td>'
    name_re = r'<td class ="normal player_name_out change_color col\d+ row\d+"><a href="/player/\d+.html" target="_blank">(.+)?</a></td>'
    data_re_com = re.compile(data_re)
    name_re_com = re.compile(name_re)
    data = re.findall(data_re_com, html.decode())
    name = re.findall(name_re_com, html.decode())

    return data, name
