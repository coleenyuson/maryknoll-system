function enrollmentTable() {
    $.ajax({
        url: '{% url "enrollment-table" student.student_ID %}',
        type: 'get',
        dataType: 'json',
        success: function(data) {
            $(".enrollment-table").html(data.html_form);
            console.log('henlo');
        }
    });
}
$(".js-create-registration").click(function() {
    $.ajax({
        url: '{% url "enrollment-create" student.student_ID%}',
        type: 'get',
        dataType: 'json',
        beforeSend: function() {
            $("#addModal").modal("show");
        },
        success: function(data) {
            $("#addModal .modal-content").html(data.html_form);
        }
    });
});

$("#addModal").on("submit", ".enrollment-form", function() {
    var form = $(this);
    $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function(data) {
            if (data.form_is_valid) {
                location.reload()
            }
            else {
                $("#enrollment-modal .modal-content").html(data.html_form);
            }
        }
    });
    return false;
});
