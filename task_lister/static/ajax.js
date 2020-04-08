        function deletet(taskid,url_del) {
    $.ajax({
        type: "post",
        url: url_del,
        success: function (response) {
            $('tr.'+taskid).hide();
            console.log("SUCCESSS!!!!")
        }
    });
}
