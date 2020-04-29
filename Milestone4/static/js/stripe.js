$(function() {
    $("#payment-form").submit(function(){
        let form = this;
        let card = {
            number: $("#id_credit_card_number").val(),
            expMonth: $("#id_expiry_month").val(),
            expYear: $("#id_expiry_year").val(),
            cvc: $("#id_cvv").val()
        };

    Stripe.createToken(card, function(status, response) {
        if (status === 200) {
            /*
            Additional Defensive checks in place to combat Stripe accepting
            12-digit cards as success cards and CVV fields as blank, solution
            by Slack user & fellow Student DaveL:
            https://code-institute-room.slack.com/archives/CGWQJQKC5/p1588176675461500?thread_ts=1588174304.457600&cid=CGWQJQKC5
             */
            if ($("#id_credit_card_number")[0].value.length != 16) {
                    showStripeErrors("Your card number is incorrect");
                } else if ($("#id_cvv")[0].value.length != 3) {
                    showStripeErrors("Your card's security code is invalid.");
                } else {
                    $("#credit-card-errors").hide();
                    $("#id_stripe_id").val(response.id);

                    // Prevent CC details from being submitted to the server
                    $("#id_credit_card_number").removeAttr("name");
                    $("#id_cvv").removeAttr("name");
                    $("#id_expiry_month").removeAttr("name");
                    $("#id_expiry_year").removeAttr("name");

                    form.submit();
                }
        } else {
            showStripeErrors(response.error.message);
        }
    });
    return false;
    });
});

function showStripeErrors(errorText){
    // Display errors to user
    $("#stripe-error-message").text(errorText);
    $("#credit-card-errors").show();
    $("#validate_card_btn").attr("disabled", false);
}