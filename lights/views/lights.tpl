<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>LEDs lights</title>
  <link rel="stylesheet" href="http://code.jquery.com/ui/1.10.3/themes/smoothness/jquery-ui.css">
  <script src="http://code.jquery.com/jquery-1.9.1.js"></script>
  <script src="http://code.jquery.com/ui/1.10.3/jquery-ui.js"></script>
  <link rel="stylesheet" href="/resources/demos/style.css">
  <script>
  $(function() {
    var repeatValue = 1;
    var offDuration = 0.25;
    var onDuration = 0.25;

    if(navigator.userAgent.match(/Android/i)){
      window.scrollTo(0,1);
    }

    $( "#repeatSlider" ).slider({
	max: 50, 
	min: 1, 
	change: function(event, ui) {
	  repeatValue = ui.value;
	  $("#cycle").attr("href", "/cycle/" + repeatValue);
	  $("#blink").attr("href", "/blink/" + repeatValue);
	},
	slide: function(event, ui) {
	  $("#repeatCount").html(ui.value);
	}
    });

    $( "#lightOnSlider" ).slider({
	max: 1, 
	min: 0.01, 
	step: 0.01,
	change: function(event, ui) {
	  onDuration = ui.value;
	},
	slide: function(event, ui) {
	  $("#lightOnDuration").html(ui.value);
	}
    });

    $( "#lightOffSlider" ).slider({
	max: 1, 
	min: 0.01, 
	step: 0.01,
	change: function(event, ui) {
	  offDuration = ui.value;
	},
	slide: function(event, ui) {
	  $("#lightOffDuration").html(ui.value);
	}
    });

    $( "button" ).click(function(){
      var buttonId = $(this).attr("id");
      if(buttonId == "cycle" || buttonId == "blink")
        var url = "/" + buttonId + "/" + repeatValue + "/" + onDuration + "/" + offDuration;
      else
        var url = "/" + buttonId;
      jQuery.ajax(url);
    });

});
  </script>
</head>
<body>

<div>Repeat Count:<span id="repeatCount"></span></div>
<div id="repeatSlider"></div>
<div>Light On Duration:<span id="lightOnDuration"></span></div>
<div id="lightOnSlider"></div>
<div>Light Off Duration:<span id="lightOffDuration"></span></div>
<div id="lightOffSlider"></div>
<button type="button" id="cycle">cycle</button>
<button type="button" id="blink">blink</button>
<button type="button" id="red">red</button>
<button type="button" id="yellow">yellow</button>
<button type="button" id="green">green</button>
<button type="button" id="off">off</button>

</body>
</html>
