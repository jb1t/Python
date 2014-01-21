<!DOCTYPE html>
<html>
  <head>
    <title>LED Lights</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap -->
    <link href="static/css/bootstrap.min.css" rel="stylesheet">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->
  </head>
<body>

<div class="container">
    <div class="jumbotron">
        <div>Repeat Count: <span id="repeatCount"></span></div>
        <input style="width: 100%" type="range" id="repeatSlider" min="1" max="50" step="1" value="5">
        <div>Light On Duration: <span id="lightOnDuration"></span></div>
        <input style="width: 100%" type="range" id="lightOnSlider" min="0.01" max="1" step="0.01" value="0.25">
        <div>Light Off Duration: <span id="lightOffDuration"></span></div>
        <input style="width: 100%" type="range" id="lightOffSlider" min="0.01" max="1" step="0.01" value="0.25">
        <br/>
        <p>
            <a class="btn btn-lg btn-info btn-block" href="#" role="button" id="cycle">Cycle</a>
        </p>
        <p>
            <a class="btn btn-lg btn-info btn-block" href="#" role="button" id="blink">Blink</a>
        </p>
        <p>
            <a class="btn btn-lg btn-danger btn-block" href="#" role="button" id="red">Red</a>
        </p>
        <p>
            <a class="btn btn-lg btn-warning btn-block" href="#" role="button" id="yellow">Yellow</a>
        </p>
        <p>
            <a class="btn btn-lg btn-success btn-block" href="#" role="button" id="green">Green</a>
        </p>
        <p>
            <a class="btn btn-lg btn-default btn-block" href="#" role="button" id="off">Off</a>
        </p>
     </div>
</div>
<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://code.jquery.com/jquery.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="static/js/bootstrap.min.js"></script>
     <script>
  $(function() {
    var repeatValue = 1;
    var offDuration = 0.25;
    var onDuration = 0.25;

    if(navigator.userAgent.match(/Android/i)){
      window.scrollTo(0,1);
    }

    $( "#repeatSlider" ).change(function(event, ui) {
	  repeatValue = this.value;
	  $("#repeatCount").html(repeatValue);
	});

    $( "#lightOnSlider" ).change(function(event, ui) {
	  onDuration = this.value;
	  $("#lightOnDuration").html(onDuration);
	});

    $( "#lightOffSlider" ).change(function(event, ui) {
	  offDuration = this.value;
	  $("#lightOffDuration").html(offDuration);
	});

    $( "a.btn" ).click(function(){
      var buttonId = $(this).attr("id");
      if(buttonId == "cycle" || buttonId == "blink")
        var url = "/" + buttonId + "/" + repeatValue + "/" + onDuration + "/" + offDuration;
      else
        var url = "/" + buttonId;
      jQuery.ajax(url);
    });

});
  </script>
</body>
</html>
