function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}


$.get('/user/auths/', function (data) {
    if ('code' in data){
        $('.btn-success').hide();
        $('#id-card').val(data.id_card);
        $('#real-name').val(data.id_name);
    }
});


$('#form-auth').submit(function () {
    var id_card = $('#id-card').val();
    var id_name = $('#real-name').val();
    $.ajax({
        url: '/user/auths/',
        type: 'put',
        data: {'id_card': id_card, 'id_name': id_name},
        dataType: 'json',
        success: function (data) {
            if (data.code == '200'){
                $('#id-card').val(id_card);
                $('#real-name').val(id_name);
                $('.btn-success').hide();
            }else{
                $('#error-msg').html('<i class="fa fa-exclamation-circle"></i>' + data.msg)
            }
        },
        error: function (data) {
            alert('认证失败')
        }
    });
    return false
});

