var http = require('http');
var fs = require('fs');
var url = require('url');
var mysql  = require('mysql');
const querystring = require('querystring')

var connection = mysql.createConnection({
   host     : '127.0.0.1',
   user     : 'mysql',
   password : 'aVhzrzv0A<ht',
   port: '3306',
   database: 'moontalk'
});

connection.connect();

var ws = require("nodejs-websocket")
 
// Scream server example: "hi" -> "HI!!!"
var server = ws.createServer(function (conn) {
    console.log("New connection")
    conn.on("text", function (str) {
        console.log("Received "+str)
        conn.sendText(str.toUpperCase()+"!!!")
    })
    conn.on("close", function (code, reason) {
        console.log("Connection closed")
    })
}).listen(8001)

// 创建服务器
http.createServer( function (request, response) {
   // 解析请求，包括文件名
   var pathname = url.parse(request.url).pathname;

   // 输出请求的文件名
   console.log(pathname);
   console.log(request.method);

   let path,post
   // 从文件系统中读取请求的文件内容
   if(request.method == "GET"){
         path = request.url
         if(path!="/getMsg"){
         fs.readFile(pathname.substr(1), function (err, data) {
            if (err) {
               console.log(err);
               // HTTP 状态码: 404 : NOT FOUND
               // Content Type: text/html
               response.writeHead(404, {'Content-Type': 'text/html'});
            }else{
               // HTTP 状态码: 200 : OK
               // Content Type: text/html
               response.writeHead(200, {'Content-Type': 'text/html'});
      
               // 响应文件内容
               response.write(data.toString());
            }
            //  发送响应数据
            response.end();
         });
         }else{
            response.write(getLateset())
            response.end()
         }
   }else if(request.method=="POST"){
      let arr=[]
      path = request.url
      request.on('data',buffer=>{
            arr.push(buffer)
      })
      request.on('end',()=>{
            post = querystring.parse(Buffer.concat(arr).toString())
            if(path=='/sendMsg'){
               response.writeHead(200,{
                   "Content-Type":"text/plain;charset:utf-8"
               })
               let {sender, msg} = post
               //接收到发信人和信息
               sendToDatabase(sender, msg)
               console.log(sender+" "+msg)
            }
      })
   }

   function sendToDatabase(sender, msg){
      var date = new Date(); 
      sqldatetime = date.toISOString().slice(0, 19).replace('T', ' ');
      var  addSqlParams = [sender,msg,sqldatetime];
      var  addSql = 'INSERT INTO moontalk_msg(msg_sender,msg_content,time) VALUES(?,?,?)';
      connection.query(addSql, addSqlParams,function (err,result) {
         if(err){
            console.log('[INSERT ERROR] - ',err.message);
         }
      });
   }
   
   function getLateset(){
      var selectsql = "SELECT * FROM moontalk_msg ORDER BY msg_id DESC LIMIT 10;"
      connection.query(selectsql,function (err,result) {
         if(err){
            console.log('[INSERT ERROR] - ',err.message);
         }
         console.log(result)
         return result;
      });
   }
   
}).listen(8080);

// 控制台会输出以下信息
console.log('http://127.0.0.1:8080/html/index.html');