console.log('changeProfile')

$(function () {
  $('#changeProfileForm').submit(profile);
  $('#avatarUpload').on('change', uploadAvatar);
});

const error_class_name = "has-error"

function error_process(data) {
  $(".help-block").remove()
  console.log('error_process')
  let groups = ['#first_nameGroup', '#last_nameGroup', '#mobileGroup', '#locationGroup']
  for (let group of groups) {
    $(group).removeClass(error_class_name);
  }
  if (data.responseJSON.first_name) {
    help_block("#first_nameGroup", data.responseJSON.first_name)
  }
  if (data.responseJSON.last_name) {
    help_block("#last_nameGroup", data.responseJSON.last_name)
  }
  if (data.responseJSON.mobile) {
    help_block("#mobileGroup", data.responseJSON.mobile)
  }
  if (data.responseJSON.location) {
    help_block("#locationGroup", data.responseJSON.location)
  }

}
function help_block(group, variable) {
  $(group).addClass(error_class_name);
  $(group).append('<div class="help-block">' + variable + "</div>");
}

function profile(event) {
    event.preventDefault();
    console.log('click')
    let form = $(this);
    let data = form.serialize()
    console.log(data)
    $.ajax({
        url: form.attr('method'),
        type: "PUT",
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

function uploadAvatar(e){
    e.preventDefault();
    console.log('change')
    let form=$(this)

    let formData = new FormData()
    let file = form[0].files
    formData.append('avatar', file[0])
    $.ajax({
        url: form.data('href'),
        type: 'POST',
        data: formData,
        contentType: false,
        processData: false,
        success: function (data){
            console.log('success', data)
            $('#avatar').attr('src', data.avatar)
        },
        error: function (data){
            console.log('error', data)
        }
    })


}
