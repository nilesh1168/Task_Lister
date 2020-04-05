function deletet(taskid) {
    console.log(taskid);
    $.ajax({
        type: "post",
        url: '{{ url_for("deltask",t_id='+taskid+') }}',
        success: function (response) {
            $('tr.'+taskid).hide();
            console.log("SUCCESSS!!!!")
        }
    });
}

