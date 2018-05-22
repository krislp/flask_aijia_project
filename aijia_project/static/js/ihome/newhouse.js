function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){

    $.get('/house/area_facility/', function (data) {
        var area_html_list = '';
        for (var i=0; i<data.area_list.length; i++){
            var area_html = '<option value="' + data.area_list[i].id + '">' + data.area_list[i].name + '</option>';
            area_html_list += area_html
        }
        $('#area-id').html(area_html_list);

        var facility_html_list = '';
        for (var i=0; i<data.facility_list.length; i++){
            var facility_html = '<li><div class="checkbox"><label>';
            facility_html += '<input type="checkbox" name="facility" value="'+ data.facility_list[i].id + '">' + data.facility_list[i].name;
            facility_html += '</label></div></li>';
            facility_html_list += facility_html
        }
        $('.house-facility-list').html(facility_html_list)
    })
});

$('#form-house-info').submit(function () {
    var facilities = [];
    $('input[name="facility"]:checked').each(function (i) {
        facilities[i] = $(this).val()
    });
    $.ajax({
        url: '/house/newhouse/',
        type: 'post',
        data: {
            'title': $('#title').val(),
            'price': $('#price').val(),
            'area_id': $('#area_id').val(),
            'address': $('#address').val(),
            'room_count': $('#room_count').val(),
            'acreage': $('#acreage').val(),
            'unit': $('#unit').val(),
            'capacity': $('#capacity').val(),
            'beds': $('#beds').val(),
            'deposit': $('#deposit').val(),
            'min_days': $('#min_days').val(),
            'max_days': $('#max_days').val(),
            'facilities': facilites
        },
        dataType: 'json',
        success: function (data) {
            alert(data.msg)
        },
        error: function (data) {
            alert('发布房源失败')
        }
    });
});
