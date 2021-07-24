console.log('follower')

$(function () {
  $('.caption').click(follow);

});


function follow(event) {
    event.preventDefault();
    console.log('click')

    let follow = $(this);
    let data = {
      'to_user': follow.data('id'),
    }

    console.log(data)
    let data_id = this.getAttribute('data-id');
    console.log(data_id)
    $.ajax({
        url: follow.data('href'),
        type: "POST",
        data: data,
        success: function (data) {
            console.log(data, 'success')
            $('.caption').text(data.follow_status)

        },
        error: function (data) {
            console.log('error', data)

        }
      })
}

$(document).ready(function(){
    $(' button#followButton').on('click', function () {
        if ($(this).text() == 'Follow') {
            $(this).text('Unfollow');
        }
        else {
            $(this).text('Follow');
        }
    });
});
