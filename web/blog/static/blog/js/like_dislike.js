console.log('like_dislike')


$(function () {
  $('.articleLike').click(like);
  $('.articleDislike').click(like);
  $('.commentLike').click(comDislike);
  $('.commentDislike').click(comDislike);
});

function like(event) {
    event.preventDefault();
    console.log('click')
    let like = $(this);
    let vote = like.data('vote')
    let data = {
      'object_id': like.data('id'),
      'model': like.data('model'),
      'vote': like.attr('data-vote'),
    }
    let data_id = this.getAttribute('data-id');
    console.log(data_id)

    console.log(data)
    $.ajax({
        url: like.data('href'),
        type: "POST",
        data: data,
        success: function (data) {
            console.log(data, 'success')
            $('#likeCount').text(data.like_count)
            $('#dislikeCount').text(data.dislike_count)
            let count_dislike = (data.dislike_count)
            let count_like = (data.like_count)

            if (vote === 1 && data.like_status === 'liked'){
              console.log('like', vote, data_id, count_like)
              $('#articleLike_'+data_id).attr('style', 'background:blue');
              $('#articleDislike_'+data_id).attr('style', 'background:#03A9F4')
            }
            else if (vote === -1 && data.like_status === 'disliked'){
              $('#articleDislike_'+data_id).attr('style', 'background:blue');
              $('#articleLike_'+data_id).attr('style', 'background:#03A9F4')
            }
            else {
              console.log('dislike', vote, data_id, count_dislike)
              $('#articleDislike_'+data_id).attr('style', 'background:#03A9F4')
              $('#articleLike_'+data_id).attr('style', 'background:#03A9F4')
            }
        },
        error: function (data) {
            console.log('error', data)

        }
      })
}


function comDislike(event) {
    event.preventDefault();
    console.log('com_click')
    let like = $(this);
    let vote = like.data('vote')
    let data = {
      'object_id': like.data('id'),
      'model': like.data('model'),
      'vote': vote,
    }
    console.log(data)
    let data_id = this.getAttribute('data-id');
    console.log(data_id)

    $.ajax({
        url: like.data('href'),
        type: "POST",
        data: data,
        success: function (data) {
            console.log(data, 'success')
            $('#likeCount_'+data_id).text(data.like_count)
            $('#dislikeCount_'+data_id).text(data.dislike_count)
            let count_dislike = (data.dislike_count)
            let count_like = (data.like_count)

            if (vote === 1 && data.like_status === 'liked'){
              console.log('like', vote, data_id, count_like)
              $('#comLike_'+data_id).attr('style', 'background:blue');
              $('#comDislike_'+data_id).attr('style', 'background:#03A9F4')
            }
            else if (vote === -1 && data.like_status === 'disliked'){
              $('#comDislike_'+data_id).attr('style', 'background:blue')
              $('#comLike_'+data_id).attr('style', 'background:#03A9F4')
            }
            else {
              console.log('dislike', vote, data_id, count_dislike)
              $('#comDislike_'+data_id).attr('style', 'background:#03A9F4')
              $('#comLike_'+data_id).attr('style', 'background:#03A9F4')
            }
        },

        error: function (data) {
            console.log('error', data)
            error_process(data);
        }
      })
}





