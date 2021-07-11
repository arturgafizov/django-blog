console.log('like_dislike')


$(function () {
  $('#articleLike').click(like);
  $('#articleDislike').click(like);
  $('.commentLike').click(like);
  $('.commentDislike').click(like);
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
    console.log(data)
    $.ajax({
        url: like.data('href'),
        type: "POST",
        data: data,
        success: function (data) {
            console.log(data, 'success')
            $('#likeCount').text(data.like_count)
            $('#dislikeCount').text(data.dislike_count)
            $('#likeCountComment').text(data.like_count)
            $('#dislikeCountComment').text(data.dislike_count)
        },
        error: function (data) {
            console.log('error', data)
            error_process(data);
        }
      })
}


document.addEventListener("click", function(thenew)
  {
    articleLike = thenew . target. id;
    the_class = thenew . target.className;
    if(the_class == "social-like")
    {
      articleLike = document.getElementById(articleLike);
      if(articleLike .style . background == "blue")
      {
        articleLike .style . background = "#03A9F4";
      }
      else
      { var links = document.querySelectorAll(".social-like");
        links.forEach(link => {
          link.setAttribute("style", "background:#03A9F4");
        })
        articleLike .style . background = "blue";
      }
    }
  });

document.addEventListener("click", function(thenews)
  {
    articleDislike = thenews . target. id;
    the_class = thenews . target.className;
    if(the_class == "social-dislike")
    {
      articleDislike = document.getElementById(articleDislike);
      if(articleDislike .style . background == "blue")
      {
        articleDislike .style . background = "#03A9F4";
      }
      else
      { var links = document.querySelectorAll(".social-dislike");
        links.forEach(link => {
          link.setAttribute("style", "background:#03A9F4");
        })
        articleDislike .style . background = "blue";
      }
    }
  });

