$(function () {


});

console.log('blog-list')



$(window).scroll(function () {
// End of the document reached?
    let pagination = $('#pagination')

    console.log(pagination.height() - $(this).height() , $(this).scrollTop())
    if (pagination.height() - $(this).height() <= $(this).scrollTop()) {
        $.ajax({
            type: "GET",
            url: pagination.attr('data-href'),
            success: function (data) {
              console.log(data)
            },
            error: function (req, status, error) {

            }
        });
    }
});
