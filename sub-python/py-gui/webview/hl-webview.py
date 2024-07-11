import random
import time

import webview
from webview import Window


class JsApi:
    def __init__(self, window: Window = None):
        self.window = window
        pass

    def say_hello(self, name):
        # 模拟一个耗时操作
        print(f'Hello, {name}!')
        return f'Hello, {name}!'

    def exit_app(self):
        print('exit_app')
        self.window.destroy()
        exit(0)
        pass

    def min_window(self):
        print('min_window')
        self.window.minimize()
        pass

    def expose(self, window: Window):
        self.window = window
        window.expose(self.say_hello, self.exit_app, self.min_window)
        pass


class MainWindow:

    def __init__(self):
        self.api = JsApi()
        self.window = webview.create_window(title='新 UI', url='index.html', frameless=True,
                                            width=1080, height=720, background_color='#ffff00',
                                            resizable=False, draggable=True)
        pass

    def show(self):
        webview.start(func=self.api.expose, args=(self.window,), storage_path='testdata')
        pass


if __name__ == '__main__':
    gui = MainWindow()
    gui.show()
    pass
