console.log('changeProfile')

$(function () {
  $('#changeProfileForm').submit(profile);
});

function profile(event) {
    event.preventDefault();
    console.log('click')
    let form = $(this);
    let formData = {
        "user": {
          'first_name': $("#first_nameGroup").val(),
          'last_name': $('#last_nameGroup').val(),
          'email': $('#emailGroup').val(),
        },
        'mobile': $('#mobileGroup').val(),
        'location': $('#locationGroup').val(),
    }
    console.log(formData)
    let method=form.attr('method')
    let path=form.attr('action')
    console.log(path, method)
    $.ajax({
        url: path,
        type: method,
        data: form.formData,
        success: function (data) {
            console.log(data, 'success')

        },
        error: function (data) {
            $("#first_nameGroup").addClass("has-error");
            $("#last_nameGroup").addClass("has-error");
            $("#mobileGroup").addClass("has-error");
            $("#mobileGroup").append(
              '<div class="help-block">' + data.responseJSON.mobile + "</div>"
            );
            $("#emailGroup").addClass("has-error");
            $("#emailGroup").append(
              '<div class="help-block">' + data.responseJSON.email + "</div>"
            );
            $("#locationGroup").addClass("has-error");
        }
      })
}
