console.log('post_create1')

$(function () {
    $('#createArticleForm').submit(postCreate);

});

const error_class_name = "has-error"

function error_process(data) {
  $(".help-block").remove()
  console.log('error_process')
  let groups = ['#categoryGroup', '#titleGroup', '#contentGroup', '#fileGroup']
  for (let group of groups) {
    $(group).removeClass(error_class_name);
  }
  if (data.responseJSON.category) {
    help_block("#categoryGroup", data.responseJSON.category)
  }
  if (data.responseJSON.title) {
    help_block("#titleGroup", data.responseJSON.title)
  }
  if (data.responseJSON.content) {
    help_block("#contentGroup", data.responseJSON.content)
  }
  if (data.responseJSON.file) {
    help_block("#fileGroup", data.responseJSON.file)
  }

}
function help_block(group, variable) {
  $(group).addClass(error_class_name);
  $(group).append('<div class="help-block">' + variable + "</div>");
}

function postCreate(event){
    event.preventDefault()
    let form=$(this)
    let formData = new FormData(form[0])
    let url=form.attr('action')
    let method=form.attr('method')
    console.log(formData)
    $.ajax({
        url: url,
        type: method,
        data: formData,
        contentType: false,
        processData: false,
        success: function (data){
            console.log('success', data)
        },
        error: function (data){
            error_process(data);
        },
    })
}
