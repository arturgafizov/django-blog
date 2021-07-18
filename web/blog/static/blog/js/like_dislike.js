console.log('like_dislike')


$(function () {
  $('#articleLike').click(like);
  $('#articleDislike').click(like);
  $('.commentLike').click(comDislike);
  $('.commentDislike').click(comDislike);
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
        },
        error: function (data) {
            console.log('error', data)
            error_process(data);
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
            if (vote === 1 ){
              console.log('like', vote, data_id, like)
              $('#comLike_'+data_id).attr('style', 'background:blue');
              $('#comDislike_'+data_id).attr('style', 'background:#03A9F4')
            }
            else {
              console.log('dislike', vote, data_id, like)
              $('#comDislike_'+data_id).attr('style', 'background:#03A9F4')
              $('#comLike_'+data_id).attr('style', 'background:blue')
            }
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


// var color1 = $('.commentLike')[0];
// var color2 = document.getElementsByClassName('commentDislike')[0];
//
// function commentLike() {
//   if (color1.style.background == "blue") {
//     color1.style.background = "#03A9F4";
//   } else {
//     color1.style.background = "blue";
//   }
//   color2.style.background = "#03A9F4";
//   }
//
// function commentDislike() {
//     if (color2.style.background == "blue" ) {
//       color2.style.background = "#03A9F4";
//       }
//     else {
//       color2.style.background = "blue";
//       }
//     color1.style.background = "#03A9F4";
// }
