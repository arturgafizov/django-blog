console.log('post_create1')

$(function () {
    $('#createArticleForm').submit(postCreate);

});


function postCreate(event){
//    console.log('post_create')
    event.preventDefault()
    let form=$(this)
//    console.log(form)
    data = form.serialize()
    console.log(data)
//    var data = $('#createArticleForm').data();
    let dataList = data.split("&");
    console.log(dataList)
    let keys = Object.keys(dataList)
    console.log(keys)
    let formData = new FormData()
    console.log(form[0].files)
    formData.append('image', form[0].files[0])
//    formData.append('title',data['title']
    let url=form.attr('action')
    let method=form.attr('method')
//    console.log(url, method)
    console.log(formData)
    $.ajax({
        url: url,
        type: method,
        data: data,
        contentType: false,
        processData: false,
        success: function (data){
            console.log('success', data)
        },
        error: function (data){
            console.log('error', data)
            $("#categoryGroup").addClass("has-error");
            $("#titleGroup").addClass("has-error");
            $("#contentGroup").addClass("has-error");
            $("#fileGroup").addClass("has-error");
        },
    })
}
