$(document).ready(function(){  
    $("#abt").click(function(e) {
        
        $('html, body').animate({
            scrollTop: $($.attr(this, 'href')).offset().top
        }, 2000);
    });
    $("#svcs").click(function(e) {
        
        $('html, body').animate({
            scrollTop: $($.attr(this, 'href')).offset().top
        }, 2000);
        });

    $("#pkgs").click(function(e) {
        
        $('html, body').animate({
            scrollTop: $($.attr(this, 'href')).offset().top
        }, 2000);
    });
    $('nav ul li a').each(function() {
        var currentLocation = window.location.pathname;
        var thisLinksLocation = $(this).attr('href');
    
        if(currentLocation == thisLinksLocation) {
            $(this).addClass('active');
        }
    });
});