from bottle import route, request, run, template,  static_file
import os
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR,'static')

@route('/static/css/<filename>')
def return_static(filename=""):
    return static_file(filename, root = f'{STATIC_DIR}/css')
@route('/')
def root():
    return template('index',text="",file_name="")

@route('/open',method='POST')
def openfile():
    return template('search')

@route('/write', method='POST')
def write():
    filename = request.forms.get('filename')
    text = request.forms.get('text')
    file_names =filename+".txt"
    file_name ="./text/"+filename+".txt"
    path = "./text"
    files = os.listdir(path)
    if files==[]:
        with open(file_name,"w",encoding='UTF-8',newline='') as file:
                for i in text:
                    file.write(i)
                return filename + "に" + text + "を保存完了"
    else:
        for i in files:
            if i == file_names:
                return '<a>すでに同じ名前のテキストファイルがあります。<br>他のファイル名に変更してください。<br>テキストエディタに戻る場合は<a href="/">ここ</a>から</a>'
            else:
                file_names =i+".txt"
                file_name ="./text/"+filename+".txt"
                with open(file_name,"w",encoding='UTF-8',newline='') as file:
                    for i in text:
                        file.write(i)
                    return filename + "に" + text + "を保存完了"

@route('/read', method='POST')
def read():
    filename = request.forms.get('filename')
    file_name = filename + ".txt"
    path = "./text"
    files = os.listdir(path)
    for i in files:
        if i == file_name:
            files="./text/"+i
            with open(files,"r") as file:
                textdetail = file.read()
                return template('index', text=textdetail,file_name=i[:4])
    return '<a>検索したファイル名はありませんでした。<br>もう一度検索する場合は<a href="/open">ここ</a>から<br>テキストエディタに戻る場合は<a href="/">ここ</a>から戻ってください。</a>'


run(host='localhost', port=8080) 
