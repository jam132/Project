// Checks if any of the username or password field is left blank or not
function login() {
	var u=document.getElementById("username").value;
	var p=document.getElementById("password").value;
	var error="";
	
	// For checking the username is filled or not
	if(u=="" ) {
		var div=document.getElementById("username");
		div.placeholder="";
		div.style.borderColor="rgb(248,66,66)";
		div.style.boxShadow="inset 0 1px 2px rgba(0, 0, 0, 0.1), 0 0 8px rgb(248,66,66)";
		div.style.backgroundImage="url(img/error.png)";
		div.style.backgroundPosition="right";
		div.style.backgroundRepeat="no-repeat";
		
		$(document).ready(function() {
			   $("form").effect( "shake", {times:1}, 150 );
		});
		error="Please enter your username and password";
	}

	// For checking password is filled or not		
	if(p=="") {
		var div1=document.getElementById("password");
		div1.placeholder="";
		div1.style.borderColor="rgb(248,66,66)";
		div1.style.boxShadow="inset 0 1px 2px rgba(0, 0, 0, 0.1), 0 0 8px rgb(248,66,66)";
		div1.style.backgroundImage="url(img/error.png)";
		div1.style.backgroundPosition="right";
		div1.style.backgroundRepeat="no-repeat";
		
		$(document).ready(function() {
			   $("form").effect( "shake", {times:1}, 150 );
		});
		error="Please enter your username and password";
	}
	
	// Displays the error message if any field left empty
	if(error!="") {
		document.getElementById("lerror").innerHTML= error;
		var div1=document.getElementById("lerror");
		div1.style.color="red";		 
		return false;
	} 
	else {
		return true;
	}
	
}
	
// For validating the username field
function checkusername() {	
	var u=document.getElementById("username").value;
	
	// if the username is not valid the field will be red otherwise blue
	if(u=="") {
		var div1=document.getElementById("username");
		div1.style.borderColor="rgb(248,66,66)";
		div1.style.boxShadow="inset 0 1px 2px rgba(0, 0, 0, 0.1), 0 0 8px rgb(248,66,66)";
		div1.style.backgroundImage="url(img/error.png)";
		div1.style.backgroundPosition="right";
		div1.style.backgroundRepeat="no-repeat";
		
		// Until the username is valid it will not move to the next field 
		loginfrm.username.focus();
		return false;
	} 
	else {
		var div=document.getElementById("username");
		div.style.borderColor= "#4195fc";
		div.style.boxShadow="inset 0 1px 2px rgba(0, 0, 0, 0.1), 0 0 8px #4195fc";
		return true;
	}
}

// For validating the password field
function checkpass() {	
	var p=document.getElementById("password").value;
	
	// if the password is not valid the field will be red otherwise blue
	if(p=="") {
		var div1=document.getElementById("password");
		div1.style.borderColor="rgb(248,66,66)";
		div1.style.boxShadow="inset 0 1px 2px rgba(0, 0, 0, 0.1), 0 0 8px rgb(248,66,66)";
		div1.style.backgroundImage="url(img/error.png)";
		div1.style.backgroundPosition="right";
		div1.style.backgroundRepeat="no-repeat";
		
		// Until the password is valid the user can't submit the form		 
		loginfrm.password.focus();
		return false;
	} 
	else {
		var div=document.getElementById("password");
		div.style.borderColor= "#4195fc";
		div.style.boxShadow="inset 0 1px 2px rgba(0, 0, 0, 0.1), 0 0 8px #4195fc";
		return true;
	}
}
