import re

from parsel.csstranslator import GenericTranslator

_translator = GenericTranslator()


def run_main():
    print(_translator.css_to_xpath('div.hello', prefix=''))
    print(_translator.css_to_xpath('div.image_container>a::attr(href)', prefix=''))
    pass


if __name__ == '__main__':
    # run_main()
    raw = '''<script >show_comment_content('　　广告和推书请发在此楼，格式：发表书评点击“宣传”，输入书号+加30内字评论自荐语。<br>　　 提示：出价最高的书评将置顶显示，热书下面的广告，有利于提高曝光度，其它位置打书籍广告，一律小黑屋。',7933);</script>'''
    print(raw)
    p = re.compile(r'<script >show_comment_content\((.+?)(,\d.+?)\);</script>')
    for comment, _ in p.findall(raw):
        print(comment.replace('　', '').replace('<br>', ''))
    pass
