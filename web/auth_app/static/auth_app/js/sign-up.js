console.log('sing-up')

$(function(){
    $('#signUpForm').submit(signUp);
})

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
        error:function(data){
            console.log(data, 'error')
            if (data.responseJSON.email){
                $('#emailGroup').addClass('has-error')
                $('#emailGroup').append('<div class="help-block">' + data.responseJSON.email + '</div>')}
            if (data.responseJSON.password1){
                $('#password1Group').addClass('has-error')
                $('#password1Group').append('<div class="help-block">' + data.responseJSON.password1 + '</div>')}
            if (data.responseJSON.password2){
                $('#password2Group').addClass('has-error')
                $('#password2Group').append('<div class="help-block">' + data.responseJSON.password2 + '</div>')}
        }
    })
}
