console.log(window.WebSocket)
var ws = new WebSocket('ws://127.0.0.1:8001');

ws.onopen = function(e){
    console.log("连接服务器成功");
}
ws.onclose = function(e){
    console.log("服务器关闭");
}
ws.onerror = function(){
    console.log("连接出错");
}
ws.onmessage = function(e){
    console.log(e.data)
}


$('#sendbutton').click(function () {
        let sender = document.getElementById("sender").value
        let msg = document.getElementById("msg").value
        ws.send(sender);
        $.post("/sendMsg",
        {
            sender:sender,
            msg:msg
        },
        function(data,status){
            alert("Data: " + data + "\nStatus: " + status);
        });
    })
