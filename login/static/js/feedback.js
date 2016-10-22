$(document).ready(function() {
	$("#feedbackLink").click(function( event ){
		event.preventDefault();
    	$(".wrapper").fadeToggle("fast");
  	});
	
	
	$(".fclose").click(function(){
		$(".wrapper").fadeToggle("fast");
	});
	
	$(document).keyup(function(e) {
		if(e.keyCode == 27 && $(".wrapper").css("display") != "none" ) { 
			event.preventDefault();
			$(".wrapper").fadeToggle("fast");
		}
	});
});