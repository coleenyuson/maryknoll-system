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
