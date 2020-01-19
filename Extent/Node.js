// const Http = new XMLHttpRequest();

// Http.open("GET", url);
// Http.send();

// Http.onreadystatechange=function(){
//     if(this.readyState==4&&this.status==200){
//         console.log(Http.responseText)
//     }
// }



/*const https = require('https');

https.get("http://[Cruzhacks2020-1579379258579].appspot.com", (resp) => {
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


// */
// const currentURL = "I am a goofy goober"
// const https = require('https')

// const data = JSON.stringify({
//   todo: currentURL
// })

// const options = {
//   hostname: 'http://cruzhacks2020-1579379258579.appspot.com/',
// //   port: 443,
//   path: '/todos',
//   method: 'POST',
//   headers: {
//     'Content-Type': 'application/json',
//     'Content-Length': data.length
//   }
// }

// const req = https.request(options, (res) => {
//   console.log(`statusCode: ${res.statusCode}`)

//   res.on('data', (d) => {
//     process.stdout.write(d)
//   })
// })

// req.on('error', (error) => {
//   console.error(error)
// })

// req.write(data)
// req.end()


let url= "https://cruzhacks2020-1579379258579.appspot.com/"
const axios = require('axios').default;

function doGet() {
  axios.get(url)
  .then(function (response) {
    // handle success
    console.log(response);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .finally(function () {
    // always executed
  });
}

//doGet()


  axios.post("https://cruzhacks2020-1579379258579.appspot.com/form-example", {
    url: "www.youtube.com and i like puppies"
  })
  .then(function (response) {
    console.log(response.data);
  })
  .catch(function (error) {
    console.log(error);
  });



