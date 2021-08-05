console.log('follower')

$(function () {
  $('.follow-button').click(follow);

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
            follow.text(data.follow_status)

        },
        error: function (data) {
            console.log('error', data)

        }
      })
}

$(window).scroll(function () {
    // End of the document reached?
    let url = window.location.pathname
    console.log(url)
    if ($(document).height() - $(this).height() == $(this).scrollTop()) {

        $.ajax({
            type: "GET",
            url: "/profiles/profile/2",
            contentType: "application/json; charset=utf-8",
            data: ' ',
            dataType: "json",
            success: function (msg) {
                if (msg.d) {
                    $(".row").append(msg.d);

                }
            },
            error: function (req, status, error) {
                  alert("Error try again");
            }
        });
    }
});
