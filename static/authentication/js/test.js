<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
$(document).ready(function() {
    $('#login-form').submit(function(event) {
        event.preventDefault(); // prevent default form submit
        $.ajax({
            url: "{% url 'login' %}", // your login view URL
            type: "POST",
            data: $('#login-form').serialize(), // serialize form data
            success: function(response) {
                if (response.success) {
                    alert("Login successful");
                    location.reload(); // reload page on successful login
                } else {
                    // login failed, display error message
                    $('.alert-danger').remove();
                    $('#login-form').before('<div class="alert alert-danger">' + response.error_message + '</div>');
                }
            },
            error: function(xhr, status, error) {
                // display error message
                $('.alert-danger').remove();
                $('#login-form').before('<div class="alert alert-danger">' + error + '</div>');
            }
        });
    });
});
</script>