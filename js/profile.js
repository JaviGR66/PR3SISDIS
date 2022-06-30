window.onload = function () {
  $.get("https://9wr1ip033i.execute-api.us-east-1.amazonaws.com/Apivideos", {
    Usuario: sessionStorage.getItem('Usuario'),
    Tag: "",
    Vidname: "",
    op: "get"
  }, function (data) {
    console.log(data);
    let x=0;
    data.forEach(function (datas) {
      console.log(datas);
      $("#table").append("<tr id='tr"+x+"'><td>"+sessionStorage.getItem("Usuario")+"</td><td>" +
        ""+datas.Vidname+"</td>" +
        "<td>"+datas.Tag+"</td><td>"+datas.Size+"</td><td>"+datas.Ruta+"</td><td>"+datas.FechaSubido+"</td>" +
        "<td><button class='btn btn-danger' id='btn"+x+"'>delete</button></td></tr>");
      $("#btn"+x).click(function () {
        $.get("https://9wr1ip033i.execute-api.us-east-1.amazonaws.com/Apivideos",{
            Usuario: sessionStorage.getItem("Usuario"),
            Vidname: datas.Vidname,
            Extension: datas.Extension,
            op:"delete"
          }
        ).done(function( msg ) {
          alert( "Vid Deleted: " + msg );
          $("tr"+x).remove();
        });
      });
      x++;
    });
  });
}
