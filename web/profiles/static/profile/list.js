console.log('profile-list')


function pageRender(data, pagination) {
    $.each(data, function (i){
      let template = `
        <div class="row" id="myScroll">
              <div class="span12">
              <ul class="thumbnails">
                      <li class="span5 clearfix">
                        <div class="thumbnail clearfix">
                          <a href="${data[i].url, data[i].id}" >
                            <img src="${data[i].avatar}" width="150" height="150" alt="IMAGE NOT FOUND" class="pull-left span2 clearfix" style='margin-right:10px'>
                          </a>

                          <div class="caption"  class="pull-left">
                            <button class="btn btn-primary icon  pull-right follow-button" data-href="/follow/" data-id="${data[i].id}" >
                                ${data[i].follow}</button>
                            <h4>
                            <a href="#" >${data[i].first_name} ${data[i].last_name}</a>
                            </h4>
                            <small><b>RG: </b>99384877</small>
                          </div>
                        </div>
                      </li>
                  </ul>
              </div>
        </div>
      `
      pagination.append(template)
    })
     $('.follow-button').click(follow);
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
            },
            error: function (req, status, error) {

            }
        });
    }
});
