(function() {
    var video = document.getElementById('video'),
        canvas = document.getElementById('canvas'),
        context = canvas.getContext('2d'),
        vendorUrl = window.URL || window.webkitURL;
    
    navigator.getMedia = navigator.getUserMedia ||navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia;
    
    navigator.getMedia({
        video : true,
        audio : false
    }, function(stream) {
        video.src = vendorUrl.createObjectURL(stream);
        video.play();
    }, function(error) {
        
    });
    document.getElementById('capture').addEventListener('click', function() {
        context.drawImage(video, 0 , 0, 400, 300);
        var dataURL = canvas.toDataURL();
        $.post('{{ url_for("upload") }}',{'imgData':dataURL},function(respData)
        {
            
        });
    });
})();


/*3c6a3afd075f89a*/