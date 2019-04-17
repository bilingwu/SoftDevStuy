var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
ctx.fillStyle = "#FF0000";

var height = 538;
var width = 538;
var radius = 0;
var ballooning = true;

var drawCircle = function(){
    ctx.clearRect(0,0,width,height);
    if (radius == 0)
	ballooning = true;
    else if (radius == width/2)
	ballooning = false;
    if (ballooning)
	radius = radius+1;
    else
	radius = radius-1;
    ctx.beginPath();
    ctx.arc(width/2,height/2,radius,0,6.28);
    ctx.closePath();
    ctx.fill();
    window.requestAnimationFrame( drawCircle );
};

var button = document.getElementById("circle");
button.addEventListener( "click", drawCircle );
