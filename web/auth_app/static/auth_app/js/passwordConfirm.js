console.log('verifyConfirm')



$(function(){
    $('#passwordConfirmForm').submit(verifyPassword);
});

const error_class_name = "has-error"

function error_process(data) {
  $(".help-block").remove()
  console.log('error_process')
  let groups = ['#new_passwordGroup1', '#new_passwordGroup2']
  for (let group of groups) {
    $(group).removeClass(error_class_name);
  }
  if (data.responseJSON.new_password1) {
    help_block("#new_passwordGroup1", data.responseJSON.new_password1)
  }
  if (data.responseJSON.new_password2) {
    help_block("#new_passwordGroup2", data.responseJSON.new_password2)
  }
}
function help_block(group, variable) {
  $(group).addClass(error_class_name);
  $(group).append('<div class="help-block">' + variable + "</div>");
}


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
//            $("#new_passwordGroup1").addClass("has-error");
//            $("#new_passwordGroup1").append(
//              '<div class="help-block">' + data.responseJSON.new_password1 + "</div>");
//            $("#new_passwordGroup2").addClass("has-error");
//            $("#new_passwordGroup2").append(
//              '<div class="help-block">' + data.responseJSON.new_password2 + "</div>");
              error_process(data);
          }
       })
}
