baseUrl = "https://widgets.cryptocompare.com/";
var scripts = document.getElementsByClassName("btcbar");
var embedder = scripts[scripts.length - 1];
var cccTheme = { "General": { "background": "#000", "priceText": "#fff", "enableMarquee": true }, "Currency": { "color": "#fff" } };
(function() {
    var appName = encodeURIComponent(window.location.hostname);
    if (appName == "") { appName = "local"; }
    var s = document.createElement("script");
    s.type = "text/javascript";
    s.async = true;
    var theUrl = baseUrl + 'serve/v3/coin/header?fsyms=BTC,ETH,XMR,LTC,DASH&tsyms=USD,EUR,GBP';
    s.src = theUrl + (theUrl.indexOf("?") >= 0 ? "&" : "?") + "app=" + appName;
    embedder.parentNode.appendChild(s);
})();