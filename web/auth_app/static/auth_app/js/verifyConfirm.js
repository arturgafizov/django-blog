console.log('verifyConfirm')

$(function(){
  verifyEmail()
})

function verifyEmail() {
  let url = window.location.pathname
  console.log(url.split('/'))
  console.log(key = url.split('/')[3])
  $.ajax({
      url: '/auth/sign-up/verify/',
      type: 'post',
      data: {'key': url.split('/')[3]},
      success:function(data){
          console.log(data, 'success')
          let url = '/auth/login/'
          window.location.href=url
      },
      error: function (data) {
          console.log(data);
          }
     })

}
