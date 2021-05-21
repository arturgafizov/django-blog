console.log('contact_us')

function getFileName () {

    var file = document.getElementById ('uploaded-file').value;

    file = file.replace (/\\/g, «/»).split ('/').pop ();

    document.getElementById ('file-name').innerHTML = 'Имя файла: ' + file;

}

