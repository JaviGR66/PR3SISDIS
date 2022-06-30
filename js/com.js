
$(document).ready(function () {
  $.get("https://9wr1ip033i.execute-api.us-east-1.amazonaws.com/Apivideos", {
    Usuario: "",
    Tag: "",
    Vidname: "",
    op: "get"
  }, function (data) {
    console.log(data);
    let x=0;
    data.forEach(function (datas) {
      $("#vid_10").append("<div id='vid" + x + "' class='col-md-4 d-flex justify-content-center '>" +
        "<div class='card' style='width: 18rem; margin-bottom: 10px;'> " +
        "<img src='null' class='card-img-top' alt='Card image cap' height='168' width='300'> " +
        "<div class='card-body'> <h5 style='color: black' class='card-title'" + x + ">" + datas.Vidname + "</h5></div><p class='card-text'>"
        + datas.Usuario + "<br><b>" + datas.Tag + "</b><br><i>" + datas.FechaSubido + "</i></p></div></div>");
      $("#vid"+x).click(function () { window.location.href= "./vidplayer.html?Usuario="+datas.Usuario+"&Vidname="+datas.Vidname});
      x++;
    });
  });
});

