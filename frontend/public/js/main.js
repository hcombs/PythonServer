var global;

var log = function(msg){
	global = msg;
  console.log(msg);
}

function loadDoc() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      log(this.responseText);
    }
  };
  xhttp.open("GET", "api/exercises?a=b", true);
  xhttp.send();
}