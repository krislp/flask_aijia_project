function logout() {
    $.get("/api/logout", function(data){
        if (0 == data.errno) {
            location.href = "/";
        }
    })
}

$(document).ready(function(){
    $.get('/user/user/', function (data) {
        if (data.code == 200){
            $('#user-avatar').html(data.user.avatar);
            $('#user-name').html(data.user.name);
            $('#user-mobile').html(data.user.phone);
        }
    })
})