fetch('https://temperature-sensor-calculator.herokuapp.com/simon')
  .then(response => response.json())
  .then(data => console.log(data));
document.getElementById("number").innerHTML = 10;
