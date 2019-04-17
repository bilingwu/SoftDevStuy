var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
ctx.fillStyle = "#FF0000";

var height = 538;
var width = 538;
var requestID;

var stopAnimation = function(){
    window.cancelAnimationFrame(requestID);
};

var logo = new Image();
logo.src = "dvd.png";

var x = 100;
var y = 237;
var down = true;
var right = false;

var startDVD = function(){
    ctx.clearRect(0,0,width,height);
    ctx.drawImage(logo,x,y,100,100);
    if (x == 0 || x + 1100 == width)
	right = !right;
    if (y == 0 || y + 100 == height)
	down = !down;
    if (right)
	x = x+1;
    else
	x = x-1;
    if (down)
	y = y+1;
    else
	y = y-1;
    requestID = window.requestAnimationFrame(startDVD);
};

var stopButton = document.getElementById("stop");
stopButton.addEventListener("click", stopAnimation);

var dvdButton = document.getElementById("dvd");
dvdButton.addEventListener("click", startDVD );
