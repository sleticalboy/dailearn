import webview

if __name__ == '__main__':
    webview.create_window('Hello world', 'https://pywebview.flowrl.com/')
    webview.start(debug=True, gui='gtk')
    pass
