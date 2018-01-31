$(function() {
    //Displaying the Enrollment Table
    $.ajax({
        url: '{% url "enrollment-table" student.student_ID %}',
        type: 'get',
        dataType: 'json',
        success: function(data) {
            $(".enrollment-table").html(data.html_form);
            console.log('henlo');
        }
    });

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

});

$(function() {
    //Displaying the Student Table
    $.ajax({
        url: '{% url "student-table" %}',
        type: 'get',
        dataType: 'json',
        success: function(data) {
            $("#student_listings").html(data.html_form);
        }
    });

    $(".js-create-student").click(function() {
        $.ajax({
            url: '{% url "student-create" %}',
            type: 'get',
            dataType: 'json',
            beforeSend: function() {
                $("#createStudentProfileModal").modal("show");
            },
            success: function(data) {
                $("#createStudentProfileModal .modal-content").html(data.html_form);
            }
        });
    });

    $("#createStudentProfileModal").on("submit", ".js-student-create-form", function() {
        var form = $(this);
        $.ajax({
            url: '{% url "student-create" %}',
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function(data) {
                if (data.form_is_valid) {
                    location.reload()
                }
                else {
                    console.log(data.form_is_valid);
                    $("#createStudentProfileModal .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    });

});
