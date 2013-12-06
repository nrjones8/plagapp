$(document).ready(function() {

    var lastClicked;

    function updateFeatureBox(text) {
        $('#feature_box').html(text);
    };

    $('.passage').click(function() {
        // Highlight the clicked passage
        if(lastClicked !== undefined) {
            lastClicked.css('color', 'black');
        }

        $(this).css('color', 'red');
        lastClicked = $(this);

        updateFeatureBox($(this).attr('features'));
    });
});