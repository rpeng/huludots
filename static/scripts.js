function activate($elem) {
    $elem.removeClass('clickable');
    $elem.addClass('activated');
    $elem.off('click', makeMove);
}

function makeMove(event) {
    var $elem = $(event.target);
    activate($elem);

    var data = {
        x: $elem.data('x'),
        y: $elem.data('y'),
        orientation: $elem.data('ori')
    };
    $.post('move/', data, showMove);
}

function showMove(data) {
    var x = data['x'];
    var y = data['y'];
    var ori = data['orientation'];
    var xSelector = '[data-x="' + x + '"]';
    var ySelector = '[data-y="' + y + '"]';
    var oriSelector = '[data-ori="' + ori + '"]';
    $edge = $('.clickable').filter(oriSelector).filter(xSelector).filter(ySelector);
    console.log($edge);
    activate($edge);
}

$(function() {
    $('.clickable').click(makeMove);
});
