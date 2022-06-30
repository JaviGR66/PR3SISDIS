window.onload = function () {
  var url = document.location.href,
    params = url.split('?')[1].split('&'),
    resul = {}, tmp;
  for (var i = 0, l = params.length; i < l; i++) {
    tmp = params[i].split('=');
    resul[tmp[0]] = tmp[1];
  }


  if(resul.usuario === undefined){
    resul.usuario = "";
  }
  else{
    resul.usuario=resul.usuario.split("+").join(" ");
    console.log(resul.usuario);
  }
  if(resul.tag === undefined){
    resul.tag = "";
  }
  else {
    resul.tag=resul.tag.split("+").join(" ");
    console.log(resul.tag);

  }
  if(resul.vidname === undefined){
    resul.vidname = "";
  }
  else {
    resul.vidname=resul.vidname.split("+").join(" ");
    console.log(resul.vidname);

  }
  $(document).ready(function () {
    $.get("https://9wr1ip033i.execute-api.us-east-1.amazonaws.com/Apivideos", {
      Usuario: resul.usuario,
      Tag: resul.tag,
      Vidname: resul.vidname,
      op: "get"
    }, function (data) {
      let x = 0;
      if(data[0]===undefined){
        $("#vid_10").append("<p class='display-3' style='color: white'>Video No encontrado</p>>")
      }
      else {
        data.forEach(function (datas) {
          $("#vid_10").append("<div id='vid" + x + "' class='col-md-4 d-flex justify-content-center'>" +
            "<div class='card' style='width: 18rem;'> " +
            "<img src='null' class='card-img-top' alt='Card image cap' height='168' width='300'> " +
            "<div class='card-body'> <h5 style='color: black' class='card-title'" + x + ">" + datas.Vidname + "</h5></div><p class='card-text'>"
            + datas.Usuario + "<br><b>" + datas.Tag + "</b><br><i>" + datas.FechaSubido + "</i></p></div></div>");
          $("#vid" + x).click(function () {
            window.location.href = "./vidplayer.html?Usuario=" + datas.Usuario + "&Vidname=" + datas.Vidname
          });
          x++;
        });
      }
    });
  });
}
