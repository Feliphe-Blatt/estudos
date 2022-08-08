const char MAIN[] PROGMEM = R"=====(

<!DOCTYPE html>
<html lang="pt-BR" class="js-focus-visible">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Esp-32 LED</title>
    <style>
      *{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }
      body {
        max-width: 100%;
        overflow-x: auto;
        padding: 15px;
        background-image: url(https://preview.redd.it/c3uhsgo1vx541.jpg?auto=webp&s=a45b583ebf921d3ad1649e77ad05e55226140120);
        background-size: cover;
        background-position: top center;
        background-attachment: fixed;
        font-family: sans-serif;
      }

      #cabecalho {
        background-color: rgba(0, 0, 0, 0.39);
        color: azure;
        padding: 10px;
        width: 560px;
        display: list-item;
      }
      #painel {
        background-color: rgba(0, 0, 0, 0.39);
        color: azure;
        padding: 10px;
        width: 560px;
        display: flex;
        justify-content: center;
      }
      #painel label {
        cursor: pointer;
      }
      #painel button {
        padding: 3px;
        transition: all 300ms ease-in-out;
      }
      #painel button:hover {
        background-color: rgba(0, 0, 0, 0.5);
        color: azure;
        font-size: 40px;
      }
    </style>
  </head>
  <body onload="process()">
    <header id="cabecalho">
      <h1>Controle do LED built-in do Esp-32</h1>
      <h2>
        Data:
        <div id="data">mm/dd/yyyy</div>
        Hora:
        <div id="hora">00:00:00</div>
      </h2>
    </header>
    <main id="painel">
      <label for="btnled"><b>LED:</b></label>
      <button type="button" id="btnled" onclick="botaoled()">Ligar</button>
    </main>
  </body>

  <script type="text/javascript">
    // global variable visible to all java functions
    var xmlHttp = createXmlHttpObject();

    // function to create XML object
    function createXmlHttpObject() {
      if (window.XMLHttpRequest) {
        xmlHttp = new XMLHttpRequest();
      }
      else {
        xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
      }
      return xmlHttp;
    }

    function botaoled() {
      var xhttp = new XMLHttpRequest();
      var message;
      xhttp.open("PUT", "LED", false);
      xhttp.send();
    }

    // function to handle the response from the ESP
    function response() {
    var message;
    var barwidth;
    var currentsensor;
    var xmlResponse;
    var xmldoc;
    var dt = new Date();
    var color = "#e8e8e8";

      // get the xml stream
      xmlResponse = xmlHttp.responseXML;

      // get host date and time
      document.getElementById("hora").innerHTML = dt.toLocaleTimeString();
      document.getElementById("data").innerHTML = dt.toLocaleDateString();

      xmldoc = xmlResponse.getElementsByTagName("LED");
      message = xmldoc[0].firstChild.nodeValue;
      if (message == 0) {
        document.getElementById("btnled").innerHTML = "Ligar";
      }
      else {
        document.getElementById("btnled").innerHTML = "Desligar";
      }
    }

    function process() {
      if (xmlHttp.readyState == 0 || xmlHttp.readyState == 4) {
        xmlHttp.open("PUT", "xml", true);
        xmlHttp.onreadystatechange = response;
        xmlHttp.send(null);
      }
      // you may have to play with this value, big pages need more porcessing time, and hence
      // a longer timeout
      setTimeout("process()", 50);
    }
  </script>
</html>

)=====";
