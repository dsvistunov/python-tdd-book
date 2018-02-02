window.Superlists = {};
window.Superlists.initialize = function () {
    $('input[name="text"]').on('keypress', function () {
        $('.has-error').hide();
    });
};
window.Superlists.clickhide = function () {
    $('input[name="text"]').click(function () {
        $('.has-error').hide();
    });
};

