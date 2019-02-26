$(document).ready(function () {
    $('#mnu').click(function () {
        $('html,body').animate({
            scrollTop: $(".menu").offset().top},
            'slow');
    })
    $('#abt').click(function () {
        $('html,body').animate({
            scrollTop: $(".about").offset().top},
            'slow');
    })
    $('#evnt').click(function () {
        $('html,body').animate({
            scrollTop: $(".event").offset().top},
            'slow');
    })
    $('#mrch').click(function () {
        $('html,body').animate({
            scrollTop: $(".merch").offset().top},
            'slow');
    })
    $('#mdia').click(function () {
        $('html,body').animate({
            scrollTop: $(".med").offset().top},
            'slow');
    })
});