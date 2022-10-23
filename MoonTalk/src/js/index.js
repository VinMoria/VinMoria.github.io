$('#sendbutton').click(function () {
        alert("click")
        let sender = document.getElementById("sender").value
        let msg = document.getElementById("msg").value
        $.post("/msg",
        {
            sender:sender,
            msg:msg
        },
        function(data,status){
            alert("Data: " + data + "\nStatus: " + status);
        });
    //     if(msg!=""){
    //         $.ajax({
    //             url: "/js/index",
    //             data: {
    //                 sender: $('#sender').val(),
    //                 msg: $('#msg').val()
    //             },
    //             dataType: "json",
    //             success(res) {
    //                 if (res.err) {
    //                     alert(res.msg)
    //                 } else {
    //                     alert("login success(from js)")
    //                 }
    //             }
    //         })
    //     }
    })