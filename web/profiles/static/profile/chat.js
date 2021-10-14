console.log('chat')

$(function () {
  $('#chatButton').click(chatInit);

});


function chatInit() {
    console.log('click')
    let button = $(this);
    let jwt = localStorage.getItem('jwt')
    let url = button.data('href')
    url = url + '?jwt='+jwt
    window.open(url, '_blank').focus()

}
