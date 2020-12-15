baseUrl = "https://widgets.cryptocompare.com/";
var scripts = document.getElementsByClassName("btc-converter");
var embedder = scripts[scripts.length - 1];
var cccTheme = { "General": {}, "Form": {} };
(function() {
    var appName = encodeURIComponent(window.location.hostname);
    if (appName == "") { appName = "local"; }
    var s = document.createElement("script");
    s.type = "text/javascript";
    s.async = true;
    var theUrl = baseUrl + 'serve/v1/coin/converter?fsym=BTC&tsyms=USD,EUR,GBP';
    s.src = theUrl + (theUrl.indexOf("?") >= 0 ? "&" : "?") + "app=" + appName;
    embedder.parentNode.appendChild(s);
})();