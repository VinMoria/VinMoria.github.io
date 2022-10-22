function sendToServer(a, b){
        alert(a+": "+b)
    }

    function send(){
        sendToServer(document.getElementById("sender").value,
                        document.getElementById("msg").value)
        sendToServer("hhh", "ooo")
    }