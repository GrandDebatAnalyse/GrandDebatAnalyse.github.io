// Get the container element
var liContainer = document.getElementById("list_pres");
// Get all buttons with class="btn" inside the container
var lis = liContainer.getElementsByClassName("li_pres_subjects_text");

// Loop through the buttons and add the active class to the current/clicked button
for (var i = 0; i < lis.length; i++) {
  lis[i].addEventListener("click", function() {
    var current = liContainer.getElementsByClassName("active");
    if (current.length==0 || this!=current[0]) {
    	this.className += " active";
    }
    if (current.length==1){
    	current[0].className = current[0].className.replace(" active", "");
    }
  });
}