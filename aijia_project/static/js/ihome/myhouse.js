$(document).ready(function(){
    $(".auth-warn").show();

    $.get('/house/auth_house/', function (data) {
        if (data.code == '2000'){
            $('#houses-list').hide();
        }else{
            $('.auth-warn').hide();
        }
    })
})