# Spammer's Spaghetti
### Open chat screen and execute the code on developer console 

var message = "dudeRAH on spam";
var interval = 1  ;
var count = 10 ;
var notifyInterval = 5 ;
var i = 0 ;
var timer = setInterval(function(){
document.getElementsByClassName('composer_rich_textarea')[0].innerHTML = message;
	$('.im_submit').trigger('mousedown');
	i++;
	if( i  == count )
	clearInterval(timer); 
	if( i % notifyInterval == 0)
	console.log(i + ' MESSAGES SENT');
} , interval * 1000 ) ;
