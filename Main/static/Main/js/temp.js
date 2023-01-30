$(document).ready(function () {
    $(".datepicker").datepicker({
        changeYear: true, changeMonth: true, dateFormat: 'yy-mm-dd'
    });

    $(".save-form").focusout(function () {
        $(".save-form").submit();
    });

    $(".empty-form").focusout(function () {
        $(".empty-form").submit();
    })
});

