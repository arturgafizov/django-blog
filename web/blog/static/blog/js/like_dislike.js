console.log('like_dislike')


$(function () {
  $('#articleLike').click(like);
  $('#articleDislike').click(like);
});


function like(event) {
    event.preventDefault();
    console.log('click')
    let like = $(this);
    let data = {
      'object_id': like.data('id'),
      'model': like.data('model'),
      'vote': like.attr('data-vote'),
    }
    $.ajax({
        url: like.data('href'),
        type: "POST",
        data: data,
        success: function (data) {
            console.log(data, 'success')
            $('#likeCount').text(data.like_count)
            $('#dislikeCount').text(data.dislike_count)
        },
        error: function (data) {
            console.log('error', data)
            error_process(data);
        }
      })
}
