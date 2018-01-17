$(document).ready(function(){
    x = '{{session['statusAnswer']}}';
    console.log(x);
    if (x == 'Too low!' || x == 'Too high!') {
        console.log('answer incorrect');
        // $('#playAgain').hide();
        $('#playAgain').css("display","none");
    } else {
        console.log('answer correct');
        // $('#submit').hide();
        $('#playAgain').css("display","show");
    }
});