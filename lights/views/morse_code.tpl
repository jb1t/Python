<!DOCTYPE html>
<html>
  <head>
    <title>Morse Code with LED Lights</title>
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
        <form role="form" action="/mc" method="POST">
            <div class="form-group">
                <label for="message">Type your message: </label>
                <textarea id="message" name="message" class="form-control" pattern="[A-Za-z0-9]*" rows="3">{{message}}</textarea>
                <div id="morse-code">{{encoded_message}}</div>
            </div>
            <button type="submit" class="btn btn-default btn-primary">Submit</button>
        </form>
     </div>
</div>

<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://code.jquery.com/jquery.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="static/js/bootstrap.min.js"></script>
</body>
</html>
