// console.log(window.innerHTML)

var margin =0.3;

var currentURL;
chrome.tabs.query({'active': true, 'windowId': chrome.windows.WINDOW_ID_CURRENT},
   function(tabs){
       currentURL=tabs[0].url;
      //alert(currentURL);
      
      if (currentURL.includes("fox")){
        margin=90;
        //alert(currentURL);
    }else if (currentURL.includes("nytimes")){
        marginl=10;
        //alert("left");
    }else  
        margin=0; 
        //alert("center");
    document.documentElement.style.setProperty('--element-position', margin+ '%')//change the 0.5 to the var margin

    const Http = new XMLHttpRequest();
    const url= "cruzhacks2020-1579379258579.appspot.com";
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange=function(){
        if(this.readyState==4&&this.status==200){
            console.log(Http.responseText)
        }
    }

   }   
);


    

