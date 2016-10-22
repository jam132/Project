// Checks if any of the feedback form field is left blank or not
// function feedback() {
// 	var n=document.getElementById("name").value;
// 	var e=document.getElementById("email").value;
// 	var m=document.getElementById("mob").value;
// 	var f=document.getElementById("feed").value;
// 	var error="";
	
// 	// For checking the name is filled or not
// 	if(n=="") {
// 		var div=document.getElementById("name");
// 		div.style.borderColor="rgb(248,66,66)";
// 		div.style.boxShadow="inset 0 1px 2px rgba(0, 0, 0, 0.1), 0 0 8px rgb(248,66,66)";
// 		div.style.backgroundImage="url(img/error.png)";
// 		div.style.backgroundPosition="right";
// 		div.style.backgroundRepeat="no-repeat";
		
// 		$(document).ready(function() {
// 			   $("form").effect( "shake", {times:1}, 150 );
// 		});
// 		error+="Please fill name<br>";
// 	}
	
// 	// For checking the email is filled or not	
// 	if(e=="") {
// 		var div1=document.getElementById("email");
// 		div1.placeholder="";
// 		div1.style.borderColor="rgb(248,66,66)";
// 		div1.style.boxShadow="inset 0 1px 2px rgba(0, 0, 0, 0.1), 0 0 8px rgb(248,66,66)";
// 		div1.style.backgroundImage="url(img/error.png)";
// 		div1.style.backgroundPosition="right";
// 		div1.style.backgroundRepeat="no-repeat";

// 		$(document).ready(function() {
// 			   $("form").effect( "shake", {times:1}, 150 );
// 		});
// 		error+="Please fill email<br>";
// 	}

// 	// For checking the contact is filled or not
// 	if(m=="") {
// 		var div2=document.getElementById("mob");
// 		div2.placeholder="";
// 		div2.style.borderColor="rgb(248,66,66)";
// 		div2.style.boxShadow="inset 0 1px 2px rgba(0, 0, 0, 0.1), 0 0 8px rgb(248,66,66)";
// 		div2.style.backgroundImage="url(../img/error.png)";
// 		div2.style.backgroundPosition="right";
// 		div2.style.backgroundRepeat="no-repeat";

// 		$(document).ready(function() {
// 			   $("form").effect( "shake", {times:1}, 150 );
// 		});
// 		error+="Please fill mobile number<br>";
// 	}
	
// 	// For checking the feedback is filled or not
// 	if(f=="") {
// 		var div3=document.getElementById("feed");
// 		div3.style.borderColor="rgb(248,66,66)";
// 		div3.style.boxShadow="inset 0 1px 2px rgba(0, 0, 0, 0.1), 0 0 8px rgb(248,66,66)";
// 		div3.style.backgroundImage="url(img/error.png)";
// 		div3.style.backgroundPosition="right";
// 		div3.style.backgroundRepeat="no-repeat";
		
// 		$(document).ready(function() {
// 			   $("form").effect( "shake", {times:1}, 150 );
// 		});
// 		error+="Please fill feedback";
// 	}
	
// 	// Displays the error message if any field left empty
// 	if(error!="") {
// 		document.getElementById("ferror").innerHTML= error;
// 		var div4=document.getElementById("ferror");
// 		div4.style.color="red";			 
// 		return false;
// 	}
// 	else {
// 		return true;
// 	}
// }

// For validating the name field
function checkname() {	
	var name = document.getElementById("name").value;
	var x =/^[\sA-Za-z]+$/;
	
	// if the name is not valid the field will be red otherwise blue
	if(name.match(x)) {
		var div=document.getElementById("name");
		div.style.borderColor= "#4195fc";
		div.style.boxShadow="inset 0 1px 2px rgba(0, 0, 0, 0.1), 0 0 8px #4195fc";
		return true;
	} 
	else {
		var div=document.getElementById("name");
		div.style.borderColor="rgb(248,66,66)";
		div.style.boxShadow="inset 0 1px 2px rgba(0, 0, 0, 0.1), 0 0 8px rgb(248,66,66)";
		div.style.backgroundImage="url(img/error.png)";
		div.style.backgroundPosition="right";
		div.style.backgroundRepeat="no-repeat";
			
		// Until the name is valid it will not move to the next field 
		popfrm.name.focus();
		return false;
	}
}

// For validating the email field
function checkemail() {	
	var email = document.getElementById("email").value;
	var at="@";
	var dot=".";
	var lat=email.indexOf(at);
	var lstr=email.length;
	var ldot=email.indexOf(dot);
	
	// if the email is not valid the field will be red otherwise blue
	if (email.indexOf(at)==-1 || email.indexOf(at)==0 || email.indexOf(at)==lstr) {
		var div=document.getElementById("email");
		div.style.borderColor="rgb(248,66,66)";
		div.style.boxShadow="inset 0 1px 2px rgba(0, 0, 0, 0.1), 0 0 8px rgb(248,66,66)";
		div.style.backgroundImage="url(img/error.png)";
		div.style.backgroundPosition="right";
		div.style.backgroundRepeat="no-repeat";
		alert("Email Id must contain '@' symbol");

		// Until the email is valid it will not move to the next field 			
		popfrm.email.focus();
		return false;
	}
	else if (email.indexOf(dot)==-1 || email.indexOf(dot)==0 || email.indexOf(dot)==lstr) {
		var div=document.getElementById("email");
		div.style.borderColor="rgb(248,66,66)";
		div.style.boxShadow="inset 0 1px 2px rgba(0, 0, 0, 0.1), 0 0 8px rgb(248,66,66)";
		div.style.backgroundImage="url(img/error.png)";
		div.style.backgroundPosition="right";
		div.style.backgroundRepeat="no-repeat";
			
		alert("Email id must contain '.' symbol");

		// Until the email is valid it will not move to the next field 
		popfrm.email.focus();
		return false;
	} 
	else {
		var div=document.getElementById("email");
		div.style.borderColor= "#4195fc";
		div.style.boxShadow="inset 0 1px 2px rgba(0, 0, 0, 0.1), 0 0 8px #4195fc";
		return true;
	}
}
		
// For validating the contact field
function checkmob() {
	var mobile = document.getElementById("mob").value;
	var numbers = /^[0-9]+$/;    
	
	// if the contact is not valid the field will be red otherwise blue
	if(mobile.match(numbers) && mobile.length==10) {
		var div=document.getElementById("mob");
		div.style.borderColor= "#4195fc";
		div.style.boxShadow="inset 0 1px 2px rgba(0, 0, 0, 0.1), 0 0 8px #4195fc";
		return true;
	} 
	else {
		var div=document.getElementById("mob");
		div.style.borderColor="rgb(248,66,66)";
		div.style.boxShadow="inset 0 1px 2px rgba(0, 0, 0, 0.1), 0 0 8px rgb(248,66,66)";
		div.style.backgroundImage="url(img/error.png)";
		div.style.backgroundPosition="right";
		div.style.backgroundRepeat="no-repeat";
			
		// Until the contact is valid it will not move to the next field 
		popfrm.mob.focus();
		return false;
	}
}

// For validating the feedback field
function checkfeed() {	
	var name = document.getElementById("feed").value;
	var x =/^[\sA-Za-z]+$/;
	
	// if the feedback is not valid the field will be red otherwise blue
	if(name.match(x))
	{
		var div=document.getElementById("feed");
		div.style.borderColor= "#4195fc";
		div.style.boxShadow="inset 0 1px 2px rgba(0, 0, 0, 0.1), 0 0 8px #4195fc";
		return true;
	} 
	else {
		var div=document.getElementById("feed");
		div.style.borderColor="rgb(248,66,66)";
		div.style.boxShadow="inset 0 1px 2px rgba(0, 0, 0, 0.1), 0 0 8px rgb(248,66,66)";
		div.style.backgroundImage="url(img/error.png)";
		div.style.backgroundPosition="right";
		div.style.backgroundRepeat="no-repeat";

		// Until the feedback is valid the user can't submit the form			
		popfrm.feed.focus();
		return false;
	}
}
