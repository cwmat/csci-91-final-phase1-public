$(document).ready(function(){  
    $(".abt").click(function(e) {
        
        $('html, body').animate({
            scrollTop: $($.attr(this, 'href')).offset().top
        }, 800);
    });
    $(".svcs").click(function(e) {
        
        $('html, body').animate({
            scrollTop: $($.attr(this, 'href')).offset().top
        }, 800);
        });

    $(".pkgs").click(function(e) {
        
        $('html, body').animate({
            scrollTop: $($.attr(this, 'href')).offset().top
        }, 800);
    });
    $(".contact").click(function(e) {
        
        $('html, body').animate({
            scrollTop: $($.attr(this, 'href')).offset().top
        }, 800);
        $(".top-heading .card-header").effect( "pulsate", {times:5}, 3000 );
    });
    $('#contactSubmit').click(function(){
        $('#alertContact').show()
    })
    $('#newsletterSubmit').click(function(){
        $('#alertNL').show()
    }) 
});