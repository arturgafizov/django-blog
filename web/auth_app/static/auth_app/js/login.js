$(function () {
  // $(document).on("click", "a.login", login);
  $('#loginForm').submit(login);
  $('#forgotPasswordForm').submit(forgotPassword);
});

const error_class_name = "has-error"

function error_process(data) {
  $(".help-block").remove()
  console.log('error_process')
  let groups = ['#emailGroup', '#passwordGroup']
  for (let group of groups) {
    $(group).removeClass(error_class_name);
  }
  if (data.responseJSON.email) {
    help_block("#emailGroup", data.responseJSON.email)
  }
  if (data.responseJSON.password) {
    help_block("#passwordGroup", data.responseJSON.password)
  }

}
function help_block(group, variable) {
  $(group).addClass(error_class_name);
  $(group).append('<div class="help-block">' + variable + "</div>");
}

function login(e) {
  let form = $(this);
  e.preventDefault();
  $.ajax({
    url: form.attr("action"),
    type: "POST",
    dataType: 'json',
    data: form.serialize(),
    success: function (data) {
      location.reload();
    },
    error: function (data) {
      error_process(data);
    }
  })
}



function forgotPassword (event) {
    console.log('click')
    event.preventDefault()
    let form=$(this);
    let formData=form.serialize()
    console.log(formData)
    $.ajax({
      url: form.attr("action"),
      type: "POST",
      data:formData,
      success:function(data){
          console.log(data, 'success')
          },
      error: function (data) {
          console.log(data);
          $("#emailForgotGroup").addClass("has-error");
          $("#emailForgotGroup").append(
            '<div class="help-block">' + data.responseJSON.email + "</div>"
          );
          },
    })
}
