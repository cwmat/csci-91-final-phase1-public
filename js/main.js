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
  });