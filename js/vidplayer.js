window.onload = function () {
  var url = document.location.href,
    params = url.split('?')[1].split('&'),
    data = {}, tmp;
  for (var i = 0, l = params.length; i < l; i++) {
    tmp = params[i].split('=');
    data[tmp[0]] = tmp[1];
  }
  $.get("https://9wr1ip033i.execute-api.us-east-1.amazonaws.com/Apivideos", {
    Usuario: data.Usuario,
    Tag: "",
    Vidname: decodeURIComponent(data.Vidname),
    op: "get"
  }, function (data) {
    console.log(data);
    $("body").append(
      "<div class=\"video embed-responsive embed-responsive-16by9 \"> " +
      "<video class=\"embed-responsive-item \" controls>" +
      "<source src='"+data[0].Ruta+"'></video>" +
      "</div>  <hr> <p style='color: white' class='display-4'>"+data[0].Vidname+"</p>")
  });
}
