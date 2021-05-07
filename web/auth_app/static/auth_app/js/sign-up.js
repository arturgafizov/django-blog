console.log('sing-up')

$(function(){
    $('#signUpForm').submit(signUp);
})
const error_class_name = "has-error"

function error_process(data) {
  $(".help-block").remove()
  console.log('error_process')
  let groups = ['#emailGroup', '#password1Group', '#password2Group', '#firstNameGroup', '#lastNameGroup']
  for (let group of groups) {
    $(group).removeClass(error_class_name);
  }
  if (data.responseJSON.email) {
    help_block("#emailGroup", data.responseJSON.email)
  }
  if (data.responseJSON.password1) {
    help_block("#password1Group", data.responseJSON.password1)
  }
  if (data.responseJSON.password2) {
    help_block("#password2Group", data.responseJSON.password2)
  }
  if (data.responseJSON.first_name) {
    help_block("#firstNameGroup", data.responseJSON.first_name)
  }
  if (data.responseJSON.last_name) {
    help_block("#lastNameGroup", data.responseJSON.last_name)
  }
}
function help_block(group, variable) {
  $(group).addClass(error_class_name);
  $(group).append('<div class="help-block">' + variable + "</div>");
}


function signUp(event){
    event.preventDefault();
    console.log('click')
    let form=$(this);
    console.log(form)
    let formData=form.serialize()
    console.log(formData)
    let path=form.attr('action')
    let method=form.attr('method')
    console.log(path, method)
   $.ajax({
        url:path,
        type:method,
        data:formData,
        success:function(data){
            console.log(data, 'success')
        },
        error: function (data) {
              error_process(data);
            }
    })
}
