function playFile(obj) {
  var sound = document.getElementById('sound');
  var reader = new FileReader();
  reader.onload = (function(audio) {return function(e) {audio.src = e.target.result;};})(sound);
  reader.addEventListener('load', function() {
    document.getElementById("sound")
  });
  reader.readAsDataURL(obj.files[0]);
 var file = obj.files[0];
    // This code is only for demo ...
    console.log("name : " + file.name);
    console.log("size : " + file.size);
    console.log("type : " + file.type);
    console.log("date : " + file.lastModified);
}