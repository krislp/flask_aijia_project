function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$('#form-avatar').submit(function () {
    alert('1');

    $.ajax({
        url: '/user/user/',
        type: 'PUT',
        data: {'avatar': avatar},
        dataType: 'json',
        success:function () {
            alert('success')
        },
        error:function () {
            
        }
    })
})

