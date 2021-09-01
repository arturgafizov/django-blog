$(function () {


});

console.log('blog-list')


function pageRender(data, pagination) {
    // const { format } = require('date-fns')
    // const day =format(new Date(),'do.MMM.yyyy');
    $.each(data, function (i){
      let template = `
    <div class="row">
      <div class="col-md-12 post">
        <div class="row">
          <div class="col-md-12">
            <h4>
              <strong>
                <a href="${data[i].url}" class="post-title"> ${data[i].title}</a>
              </strong>
            </h4>
          </div>
        </div>
        <div class="row">
          <div class="col-md-12 post-header-line">
            <span class="glyphicon glyphicon-user"></span>by <a href="#">${data[i].author.full_name}</a> |
            <span class="glyphicon glyphicon-calendar"></span> ${data[i].updated} |
            <span class="glyphicon glyphicon-comment"></span><a href="#">${data[i].comments_count} Comments</a> |
            <i class="icon-share"></i><a href="#">39 Shares</a> |
            <span class="glyphicon glyphicon-tags"></span> Tags: <a href="#">
            <span class="label label-info">Snipp</span></a> <a href="#">
            <span class="label label-info">UI</span></a> <a href="#">
            <a class="social-like" id="articleLike">
                <span class="like"><i class="glyphicon glyphicon-thumbs-up"></i></span>
                <span class="count" >${data[i].likes}</span>
            </a>
            &nbsp;
            <a class="social-dislike" id="articleDislike">
                <span class="dislike" >${data[i].dislikes}</span>
                <span class="like"><i class="glyphicon glyphicon-thumbs-down"></i></span>
            </a>
          </div>
        </div>
        <div class="row post-content"><br>
          <div class="col-md-3">
            <a href="#">
              <img
                src="${data[i].image}" width="150" height="150"
                alt="image" class="img-responsive">
            </a>
          </div>
          <div class="col-md-9">
            <span class="not">${data[i].content}</span>

            <p>
              <a class="btn btn-read-more" href="${data[i].url}">Read more</a>
            </p>

          </div>
        </div>
      </div>
    </div>
      `
      pagination.append(template)
    })
}

let requestedNewPage = false

$(window).scroll(function () {
// End of the document reached?
    let pagination = $('#pagination')

    // console.log(pagination.height() - $(this).height() , $(this).scrollTop())
    if (pagination.height() - $(this).height() <= $(this).scrollTop() && !requestedNewPage) {
        requestedNewPage = true

        $.ajax({
            type: "GET",
            url: pagination.attr('data-href'),
            success: function (data) {
              console.log(data)
              pageRender(data.results, pagination)

              if (data.next) {
                  pagination.attr('data-href', data.next)
                  requestedNewPage = false
              }
              // window.location.href = pagination.attr('data-href')

            },
            error: function (req, status, error) {

            }
        });
    }
});

