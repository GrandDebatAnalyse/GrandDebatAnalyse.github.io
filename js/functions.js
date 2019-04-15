
///==================================/////
///For the presentation
// Get the container element
var liContainer = document.getElementById("list_pres");
// Get all buttons with class="btn" inside the container
var lis = liContainer.getElementsByClassName("li_pres_subjects_text");

// Loop through the buttons and add the active class to the current/clicked button
for (var i = 0; i < lis.length; i++) {
  lis[i].addEventListener("click", function() {
    var current = liContainer.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
    var currentTextRight = document.getElementById("text_pres_right").getElementsByClassName("active");
    currentTextRight[0].className = currentTextRight[0].className.replace(" active", "");

    var liContainerRight = document.getElementById("text_pres_right");
    var RightDivToChange = liContainerRight.getElementsByClassName(this.id)[0]
    RightDivToChange.className += " active";
  });
}

///==============================///
////// For the BarPLot Section   //////
// Get the container element
var liContainer_BarPlots = document.getElementById("list_BarPlots");
// Get all buttons with class="btn" inside the container
var div_BarPlots = liContainer_BarPlots.getElementsByClassName("li_BarPlots_subjects_text");

// Loop through the buttons and add the active class to the current/clicked button
for (var i = 0; i < div_BarPlots.length; i++) {
  div_BarPlots[i].addEventListener("click", function() {
    var current = liContainer_BarPlots.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
    var currentTextRight = document.getElementById("text_BarPlots_right").getElementsByClassName("active");
    currentTextRight[0].className = currentTextRight[0].className.replace(" active", "");

    var liContainerRight = document.getElementById("text_BarPlots_right");
    var RightDivToChange = liContainerRight.getElementsByClassName(this.id)[0]
    RightDivToChange.className += " active";
  });
}