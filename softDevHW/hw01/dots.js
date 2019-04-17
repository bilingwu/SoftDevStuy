var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
ctx.fillStyle = "#FF0000";

var x1 = -1;
var x2 = -1;
var y1 = -1;
var y2 = -1;

var onClick = function(e){
    e.preventDefault();
    console.log("onClick");    
    ctx.beginPath();
    if (x1 == -1 && y1 == -1){
	x1 = e.offsetX;
	y1 = e.offsetY;
	ctx.arc(x1,y1,10,0,6.28);
    }
    else {
	x2 = e.offsetX;
	y2 = e.offsetY;
	ctx.moveTo(x1,y1);
	ctx.lineTo(x2,y2);
	ctx.closePath();
	ctx.stroke();
	ctx.beginPath();
	ctx.moveTo(x2,y2);
	ctx.arc(x2,y2,10,0,6.28);
	x1 = x2;
	y1 = y2;
    }
    ctx.closePath();
    ctx.fill(); 
}
canvas.addEventListener("click",onClick);

var button = document.getElementById("clear");

var clear = function(e){
    e.preventDefault();
    x1 = -1;
    y1 = -1;
    x2 = -1;
    y2 = -1;
    ctx.clearRect(0,0,538,538);
}

button.addEventListener("click",clear);
