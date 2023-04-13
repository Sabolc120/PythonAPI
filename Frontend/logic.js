var url = "http://127.0.0.1:5000/checkCats";
var id = "checkCats"

async function creator(url, id){
    var request = await new XMLHttpRequest()

    request.open('GET', url, true)
    request.onload = function () {
            // Begin accessing JSON data here
    var data = JSON.parse(this.response)
    checkCats(data, request, id);
    }
    request.send()
}

function checkCats(data, request, id) {
    if (id == "checkCats") {
      if (request.status >= 200 && request.status < 400) {
        var mainContainer = document.getElementById(id);
        mainContainer.innerHTML = ""; // clear the container
        data.forEach((query) => {
          var div = document.createElement("tr");
          div.innerHTML =
          "<td>" +
          query.id +
          "</td><td><input id='catName" +
          query.id +
          "' placeholder='" +
          query.catName +
          "' value='" +
          query.catName +
          "'/></td><td><input id='catGender" +
          query.id +
          "' placeholder='" +
          query.catGender +
          "' value='" +
          query.catGender +
          "'/></td><td><input id='catAge" +
          query.id +
          "' placeholder='" +
          query.catAge +
          "' value='" +
          query.catAge +
          "'/></td>" +
          "<td><button class='btn btn-light' onclick='editCat(" +
          query.id +
          ")'>Update</button></div></td>" +
          "<td><button class='btn btn-light' onclick='adoptCat(" +
          query.id +
          ")'>Adopt</button></div></td>";
          mainContainer.appendChild(div);
        });
      } else {
        console.log("error");
      }
    }
  }

function adoptCat(id){
  const data = JSON.stringify({
    id: parseInt(id)
  })
  navigator.sendBeacon("http://127.0.0.1:5000/adoptCat", data)
}

function editCat(id){
  const data = JSON.stringify({
    id: id,
    catName: document.getElementById("catName"+id).value,
    catGender: document.getElementById("catGender"+id).value,
    catAge: document.getElementById("catAge"+id).value
  })
  navigator.sendBeacon("http://127.0.0.1:5000/editCatData", data)
}

async function loadTable(){
await creator(url, id);
}
loadTable()