// JavaScript Document
$(document).ready(function() {

    "use strict";

    $(".booking-form").submit(function(e) {
        e.preventDefault();
        var firstname = $(".firstname");
        var lastname = $(".lastname");
        var email = $(".email");
        var phone = $(".phone");
        var service = $(".service");
        var staff = $(".staff");
        var date = $(".date");
        var flag = false;
        if (firstname.val() == "") {
            firstname.closest(".form-control").addClass("error");
            firstname.focus();
            flag = false;
            return false;
        } else {
            firstname.closest(".form-control").removeClass("error").addClass("success");
        } if (lastname.val() == "") {
            lastname.closest(".form-control").addClass("error");
            lastname.focus();
            flag = false;
            return false;
        } else {
            lastname.closest(".form-control").removeClass("error").addClass("success");
        } if (email.val() == "") {
            email.closest(".form-control").addClass("error");
            email.focus();
            flag = false;
            return false;
        } else {
            email.closest(".form-control").removeClass("error").addClass("success");
        } if (phone.val() == "") {
            phone.closest(".form-control").addClass("error");
            phone.focus();
            flag = false;
            return false;
        } else {
            phone.closest(".form-control").removeClass("error").addClass("success");
        } if (service.val() == "") {
            service.closest(".form-control").addClass("error");
            service.focus();
            flag = false;
            return false;
        } else {
            service.closest(".form-control").removeClass("error").addClass("success");
        } if (staff.val() == "") {
            staff.closest(".form-control").addClass("error");
            staff.focus();
            flag = false;
            return false;
        } else {
            staff.closest(".form-control").removeClass("error").addClass("success");
        } if (date.val() == "") {
            date.closest(".form-control").addClass("error");
            date.focus();
            flag = false;
            return false;
        } else {
            date.closest(".form-control").removeClass("error").addClass("success");
            flag = true;
        }
        var dataString = "firstname=" + firstname.val() + "&lastname=" + lastname.val() + "&email=" + email.val() + "&phone=" + phone.val() + "&service=" + service.val() + "&staff=" + staff.val() + "&date=" + date.val();
        $(".loading").fadeIn("slow").html("Loading...");
        $.ajax({
            type: "POST",
            data: dataString,
            url: "php/bookingForm.php",
            cache: false,
            success: function (d) {
                $(".form-control").removeClass("success");
                    if(d == 'success') // Message Sent? Show the 'Thank You' message and hide the form
                        $('.loading').fadeIn('slow').html('<font color="#48af4b">Mail sent Successfully.</font>').delay(3000).fadeOut('slow');
                         else
                        $('.loading').fadeIn('slow').html('<font color="#ff5607">Mail not sent.</font>').delay(3000).fadeOut('slow');
                                }
        });
        return false;
    });
    $("#reset").on('click', function() {
        $(".form-control").removeClass("success").removeClass("error");
    });
    
})



