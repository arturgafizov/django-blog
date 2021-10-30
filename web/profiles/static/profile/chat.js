console.log('chat')

$(function () {
  $('#chatButton').click(chatInit);

});


function chatInit() {
    console.log('click')
    let button = $(this);
    let jwt = localStorage.getItem('jwt')
    let url = button.data('href')
    let user_id = button.data('userid')
  console.log(button)
    console.log(user_id)
    url = url + '?jwt='+jwt + '&user_id=' + user_id
    window.open(url, '_blank').focus()

}
