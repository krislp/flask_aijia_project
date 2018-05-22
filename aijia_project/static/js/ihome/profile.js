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

    $(this).ajaxSubmit({
        url: '/user/user/',
        type: 'PUT',
        dataType: 'json',
        success:function (data) {
            if (data.code == 200){
                // attr 属性
                $('#user-avatar').attr('src', data.url)
            }
        },
        error:function (data) {
            alert('上传头像失败')
        }
    });
    return false;
});


$('#form-name').submit(function () {
    $('.error-msg').hide();
    var name = $('#user-name').val();
    $.ajax({
        url: '/user/user/',
        type: 'put',
        data: {'name': name},
        dataType: 'json',
        success:function (data) {
            if (data.code == 200) {

            }else{
                $('.error-msg').html('<i class="fa fa-exclamation-circle">用户名已经存在</i>');
                $('.error-msg').show()
            }
        },
        error:function (data) {
            alert('修改用户名失败')
        }
    });
    return false
});

