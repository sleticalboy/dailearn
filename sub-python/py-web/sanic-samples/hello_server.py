import os

import sanic
from sanic import Sanic

app = Sanic('hello-server')


@app.get('/')
def index(request):
    response = '<h1>Welcom Here</h1>'
    response += '<ul>'
    for k, v in app.router.routes_all.items():
        api = v.uri.replace('<', '&lt;').replace('>', '&gt;')
        response += f"<li><a href='{v.uri}'>{api}</a></li>"
    response += '</ul>'
    return sanic.html(response)


# 上传文件
@app.route('/upload', methods=['POST'])
def upload_file(request):
    uploaded_file = request.files['file']
    if uploaded_file:
        file_path = os.path.join('uploads', uploaded_file.filename)
        uploaded_file.save(file_path)
        return sanic.text("File '{uploaded_file.filename}' uploaded successfully.")


# 列出所有文件
@app.route('/list')
def list_files(request):
    files = os.listdir('uploads')
    return sanic.json({'files': files})


# 删除文件
@app.route('/delete/<filename>')
def delete_file(request, filename):
    file_path = os.path.join('uploads', filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return sanic.text(f"File '{filename}' deleted successfully.")
    return sanic.text(f"File '{filename}' not found.")


if __name__ == '__main__':
    # 创建上传文件夹
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    print('start running...')
    # 运行 Sonic 应用
    app.run(port=9999, debug=True, dev=True)
    print('running...')
