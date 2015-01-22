$(document).ready(function() {
    $('#submit').click(function() {
        document.domain = 'ihaveablog.com';
        $.ajax({ url: "http://www.ihaveablog.com:5000/test", success: function(){
            alert('success');
          }});
    })
})


