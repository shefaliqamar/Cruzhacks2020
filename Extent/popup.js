// console.log(window.innerHTML)
document.documentElement.style.setProperty('--element-position', .5+ '%')

/*var currentURL;
chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
    currentURL = tabs[0].url;
    alert();
});*/

/*function getCurrentURL(tab){
    currentURL=tab;
    alert(tab)
}*/
/*
//document.getElementById("url").innerHTML = currentURL;

const https = require('https');

https.get('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY', (resp) => {
  let data = '';

  // A chunk of data has been recieved.
  resp.on('data', (chunk) => {
    data += chunk;
  });

  // The whole response has been received. Print out the result.
  resp.on('end', () => {
    console.log(JSON.parse(data).explanation);
  });

}).on("error", (err) => {
  console.log("Error: " + err.message);
});
*/