console.log('verifyConfirm')



$(function(){
    $('#passwordConfirmForm').submit(verifyPassword);
});

function verifyPassword(event) {
    event.preventDefault();
    let form=$(this);
    let url = window.location.pathname
    console.log(url.split('/'))
    console.log(uid = url.split('/')[3])
    console.log(token = url.split('/')[4])
    let formData = {
        'new_password1': $("#new_password1").val(),
        'new_password2': $('#new_password2').val(),
        'uid': url.split('/')[3],
        'token': url.split('/')[4],
    }
    console.log(formData)
    $.ajax({
        url: form.attr('action'),
        type: 'POST',
        data: formData,
        success:function(data){
            console.log(data, 'success')
            let url = '/auth/login/'
            window.location.href=url
        },
        error: function (data) {
            console.log(data);
            }
       })
}
