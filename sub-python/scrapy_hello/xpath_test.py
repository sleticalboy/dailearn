from parsel.csstranslator import GenericTranslator

_translator = GenericTranslator()


def run_main():
    print(_translator.css_to_xpath('div.hello', prefix=''))
    print(_translator.css_to_xpath('div.image_container>a::attr(href)', prefix=''))
    pass


if __name__ == '__main__':
    run_main()
    pass
