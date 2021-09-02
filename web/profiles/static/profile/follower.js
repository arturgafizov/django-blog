console.log('follower')

$(function () {
  $('.follow-button').click(follow);
  $('#followersButton').click(followerApi);
  $('#followingButton').click(followerApi);
  $('#followersButtonShow').click(followerApiShow);
  $('#followingButtonShow').click(followerApiShow);
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


function modalRender(data) {
    let body = $('#followModalBody')
    body.empty()
    $.each(data, function (i){
      let template = `
      <div class="user">
        <p>
          <img src="${data[i].avatar}" class="avatar img-circle img-thumbnail" width=50px>
          <a href='${data[i].profile_url}'> ${data[i].full_name} </a>
          <button class="btn btn-primary btn-sm follow-button" data-href="${body.data('href')}" data-id='${data[i].id}'> ${data[i].follow} </button>
          <p>------------------------------------------------------</p>
        </p>
      </div>
      `
      body.append(template)
    })
    $('.follow-button').click(follow);
}




function followerApi() {
    console.log('click')
    let button = $(this);

    let url = button.data('href')
    console.log(url)

        $.ajax({
            type: "GET",
            url: url,

            success: function (data) {
              console.log(data, 'success')
              modalRender(data)
              $('#followModalTitle').text(button.text())
              $('#followerModal').modal('show')

            }

        })
}

function modalRenderShow(data) {
    let body = $('#followModalBodyShow')
    body.empty()
    $.each(data, function (i){
      let template = `
      <div class="user">
        <p>
          <img src="${data[i].avatar}" class="avatar img-circle img-thumbnail" width=50px>
          <a href='${data[i].profile_url}'> ${data[i].full_name} </a>
          <button class="btn btn-primary btn-sm follow-button" data-href="${body.data('href')}" data-id='${data[i].id}'> ${data[i].follow} </button>
          <p>------------------------------------------------------</p>
        </p>
      </div>
      `
      body.append(template)
    })
    $('.follow-button').click(follow);
}




function followerApiShow() {
    console.log('click')
    let button = $(this);

    let url = button.data('href')
    console.log(url)

        $.ajax({
            type: "GET",
            url: url,

            success: function (data) {
              console.log(data, 'success')
              modalRenderShow(data)
              $('#followModalTitleShow').text(button.text())
              $('#followerModalShow').modal('show')

            }

        })
}
