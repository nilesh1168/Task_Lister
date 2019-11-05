function deletet(taskid) {
    console.log(taskid);
    $.ajax({
        type: "post",
        url: "/deltask/"+taskid,
        success: function (response) {
            $('tr.'+taskid).hide();
            console.log("SUCCESSS!!!!")
        }
    });
}

