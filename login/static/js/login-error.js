// For displaying the error message for invalid username or password will be shown in popup window
$(document).ready(function() {
	if($("#error").text().length>0){
    	$(".erroroverlay").fadeToggle("fast");
  	};
	
	
	$(".eclose").click(function(){
		$(".erroroverlay").fadeToggle("fast");
	});
	
	$(document).keyup(function(e) {
		if(e.keyCode == 27 && $(".erroroverlay").css("display") != "none" ) { 
			event.preventDefault();
			$(".erroroverlay").fadeToggle("fast");
		}
	});
});