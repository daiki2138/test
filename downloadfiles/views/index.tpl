<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>テキストエディタ</title>
        <link rel="stylesheet" href="/static/css/style.css" type="text/css">
    </head>
    <body>
        <form method="POST" action="/write">
            <button type="submit">保存</button>    
            <button type=submit formaction="/open">展開</button> 
            <br>
            <input type="text" name="filename" value='{{file_name}}' placeholder="ファイル名を記入" class="filename">
            <br>
            <textarea name="text" placeholder="ここにテキストを記入" rows="40" cols="120" class="detail">{{text}}</textarea>  
        </form>
    </body>
</html>