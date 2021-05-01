fetch('https://temperatur-api.herokuapp.com/simon')
  .then(response => response.json())
  .then(data => console.log(data));
