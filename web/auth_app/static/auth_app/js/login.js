$(function () {
  // $(document).on("click", "a.login", login);
  $('#loginForm').submit(login);
  $('#forgotPasswordForm').submit(forgotPassword);
});


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
      $("#emailGroup").addClass("has-error");
      $("#passwordGroup").addClass("has-error");
      $("#passwordGroup").append(
        '<div class="help-block">' + data.responseJSON.email + "</div>"
      );
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
