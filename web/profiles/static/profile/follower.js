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
    $.ajax({
        url: follow.data('href'),
        type: "POST",
        data: data,
        success: function (data) {
            console.log(data, 'success')
            $('.caption').text(data.follow)

        },
        error: function (data) {
            console.log('error', data)

        }
      })
}

$(document).ready(function(){
    $('a#followButton').on('click', function () {
        if ($(this).text() == 'Follow') {
            $(this).text('Unfollow');
        }
        else {
            $(this).text('Follow');
        }
    });
});
