<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
$(document).ready(function(){
    $('.php-email-form').submit(function(e){
        e.preventDefault(); // Prevent the default form submission
        console.log('kl');
        var form = $(this);
        var formData = form.serialize(); // Serialize form data
        
        $.ajax({
            type: 'POST',
            url: form.attr('action'), // URL to submit the form
            data: formData,
            success: function(response){
                if(response.success){
                    // Display success message
                    form.find('.sent-message').fadeIn().html('Your message has been sent. Thank you!');
                    form.find('.error-message').hide();
                    form.find('.loading').hide();
                    form.trigger('reset'); // Reset the form
                } else {
                    // Display error message
                    form.find('.error-message').fadeIn().html('Error occurred. Please try again.');
                    form.find('.sent-message').hide();
                    form.find('.loading').hide();
                }
            },
            error: function(){
                // Display error message
                form.find('.error-message').fadeIn().html('Error occurred. Please try again.');
                form.find('.sent-message').hide();
                form.find('.loading').hide();
            }
        });
    });
});

