console.log('changePassword')

$(function () {
  $('#changePasswordForm').submit(password);
});

const error_class_name = "has-error"

function error_process(data) {
  $(".help-block").remove()
  console.log('error_process')
  let groups = ['#oldPasswordForm', '#new_password1Form', '#new_password2Form']
  for (let group of groups) {
    $(group).removeClass(error_class_name);
  }
  if (data.responseJSON.old_password) {
    help_block("#oldPasswordForm", data.responseJSON.old_password)
  }
  if (data.responseJSON.new_password1) {
    help_block("#new_password1Form", data.responseJSON.new_password1)
  }
  if (data.responseJSON.new_password2) {
    help_block("#new_password2Form", data.responseJSON.new_password2)
  }

}
function help_block(group, variable) {
  $(group).addClass(error_class_name);
  $(group).append('<div class="help-block">' + variable + "</div>");
}

function password(event) {
    event.preventDefault();
    console.log('click')
    let form = $(this);
    let data = form.serialize()
    $.ajax({
        url: form.attr('action'),
        type: "POST",
        data: data,
        success: function (data) {
            console.log(data, 'success')
        },
        error: function (data) {
            console.log('error', data)
            error_process(data);
        }
      })
}
