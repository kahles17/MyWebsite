function Test(log)
{
    document.getElementById("number").innerHTML = log;
}

const Http = new XMLHttpRequest();
const url='/simon';
Http.open("GET", url);
Http.send();
answer =Http.responseText
Http.onreadystatechange = (e) => {
  Test(Http.responseText);
}
