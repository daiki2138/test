<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>検索</title>
        <link rel="stylesheet" href="/static/css/style.css" type="text/css">
    </head>
    <body>
        <form method="POST" action="/read">
            <div>
                <input type="text" name="filename" placeholder="検索したいファイル名を記入" size=25 >
                <button type="submit">検索</button> 
            <div>
        </form>
    </body>
</html>