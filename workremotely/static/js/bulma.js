$(document).ready(function () {
    // fades the notification
    setTimeout(function () {
        $('#message.notification').fadeOut();
    }, 4000);

    // optionally click de x to fade the notification before it auto fades
    $('.delete').on('click', function () {
        $('#message.notification').fadeOut();
    });    
});