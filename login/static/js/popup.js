$(document).ready(function() {
	$("#loginLink").click(function( event ){
		event.preventDefault();
    	$(".overlay").fadeToggle("fast");
  	});
	
	
	$(".lclose").click(function(){
		$(".overlay").fadeToggle("fast");
	});
	
	$(document).keyup(function(e) {
		if(e.keyCode == 27 && $(".overlay").css("display") != "none" ) { 
			event.preventDefault();
			$(".overlay").fadeToggle("fast");
		}
	});
});