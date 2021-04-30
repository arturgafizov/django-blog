$(function () {
    $('#formReview').submit(leaveComment)

});

console.log('blog-detail')

function leaveComment(event){
    console.log('leave_comment')
    event.preventDefault()
    let form=$(this)
    console.log(form)
    data = form.serialize()
    console.log(data)
    let url=form.attr('action')
    let method=form.attr('method')
    console.log(url, method)
//    $.ajax({
//        url: url,
//        type: method,
//        data: data,
//        success: function (data){
//            console.log('success', data)
//            location.reload()
//        },
//        error: function (data){
//            console.log('error', data)
//        },
//    })
    $.post('/action', {query: 'test'}, function(data) {
    console.log(data); // ответ от сервера
    })
    .success(function() { console.log('Успешное выполнение'); })
    .error(function(jqXHR) { console.log('Ошибка выполнения'); })
    .complete(function() { console.log('Завершение выполнения'); });

}
