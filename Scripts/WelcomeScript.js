var images = [
    "http://localhost/NPG/Images/Web-Dark.png",
    "http://localhost/NPG/Images/Web-Light.png"
];

setInterval(animate, 400);
var x = 0;

function animate() {
    document.getElementById("img").src = images[x];
    x++;
    if (images.length == x) {
        x = 0;
    }
}
