function addCat(){
    const data = JSON.stringify({
        catName: document.getElementById("catName").value,
        catGender: document.getElementById("catGender").value,
        catAge: document.getElementById("catAge").value
    })

    navigator.sendBeacon('http://127.0.0.1:5000/saveCat/', data)
    console.log(data);
}