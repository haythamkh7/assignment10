function validate(){
    var firstname = document.getElementById("firstname").value;
    var lastName = document.getElementById("lastName").value;
    var phone = document.getElementById("phone").value;
    var email = document.getElementById("email").value;
    var subject = document.getElementById("subject").value;
    var message = document.getElementById("message").value;
    var error_message = document.getElementById("error_message");
    
    error_message.style.padding = "10px";
    
    var text;
    if(firstname.length < 1){
      text = "Please Enter valid firstname";
      error_message.innerHTML = text;
      return false;
    }
    if(lastName.length < 1){
      text = "Please Enter Correct lastName";
      error_message.innerHTML = text;
      return false;
    }
    if(email.indexOf("@") == -1 || email.length < 6){
        text = "Please Enter valid Email";
        error_message.innerHTML = text;
        return false;
      }
    if(subject.length < 5){
        text = "Please Enter Correct subject";
        error_message.innerHTML = text;
        return false;
      }
    if(isNaN(phone) || phone.length != 10){
      text = "Please Enter valid Phone Number";
      error_message.innerHTML = text;
      return false;
    }
    
    if(message.length <= 20){
      text = "Please Enter More Than 140 Characters";
      error_message.innerHTML = text;
      return false;
    }
    alert("Form Submitted Successfully!");
    return true;
  }