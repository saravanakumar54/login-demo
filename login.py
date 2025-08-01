#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi, cgitb, pymysql

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="day2")
cur = con.cursor()
form = cgi.FieldStorage()

print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .log{
         height: 200px;
    width: 200px;
    background-color: orange;
     position:absolute;
     top:50%;
     left:50%;
     transform:translate(-50%,-50%);
    padding: 10px;
    border-radius: 20px;
        }
        .log h1 {
    font-family: sans-serif;
    margin-top: 10px;
    text-transform: uppercase;
    margin-left: 30px;
}
        .log button{
        margin-left:70px
        }
    #das{
    position:absolute;
    top:0px;
    left:0px;
    height:600px;
    width:250px;
    background-color:orange;
    font-size:10px;
    }
    
    </style>


</head>
<body > 
<div class="log">
<h1> login </h1>
<input type="text" name="user" placeholder="username"><br>
<input type="password" name="pass" placeholder="password"><br>
<button name="submit" onclick="fun()">login</button>
</div>
''')
a='''select * from intern_task'''
cur.execute(a)
aa=cur.fetchall()
for b in aa:

        print(f'''
                <div id="das" style="display:none">
                <h1> NAME:{b[1]} </h1>
                <h1> REFERRAL:{b[2]} </h1>
                <h1> DONATION:{b[3]}</h1>
        ''')
print('''
<script>
        function fun(){
            document.getElementById('das').style.display="block";
        }
</script>


''')





