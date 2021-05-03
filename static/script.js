var request = new XMLHttpRequest();
function add_to_View(text)
{ let obj = JSON.parse(text);
  let count = Object.keys(obj).length;
  let activeElement = DynamicMJ.TEX;
  for (i = 0;i<count;i++)
  {
    activeElement.innerHTML = "\\["+obj[String(i)]+"\\]";
    MathJax.Hub.Queue(["Typeset",MathJax.Hub,activeElement]);
    let newElement = document.createElement("div");
    activeElement.parentNode.insertBefore(newElement , activeElement.nextSibling);
    activeElement = newElement;
  }
}

var DynamicMJ = {
    TEX: document.getElementById("TEX"),
  
    update: function () {
      let a = document.getElementById("A").value;
      let b = document.getElementById("B").value;
      let c = document.getElementById("C").value;
      url='/api/?'+"A="+a+"&B="+b+"&C="+c;
      request.open("GET", url);
      request.addEventListener('load', function(event) {
        if (request.status >= 200 && request.status < 300) {
           add_to_View(request.responseText)
        } else {
           console.warn(request.statusText, request.responseText);
        }
     });
      request.send();
    }
  };
