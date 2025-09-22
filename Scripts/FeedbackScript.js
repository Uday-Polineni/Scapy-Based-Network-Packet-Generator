function feedbackSubmitted(){

    var feedbackPerson = document.forms["feedback-form"]["feedback-person-id"].value;
    var feedback = document.forms["feedback-form"]["comments"].value;

    if(!feedbackPerson){
        alert('please enter your name or email');
        return false;
    }
    if(!feedback){
        alert('please provide some feedback');
        return false;
    }
    if(feedback.length < 50){
        alert('your feedback should contain minimum 50 characters.');
        return false;
    }
    return true;
}