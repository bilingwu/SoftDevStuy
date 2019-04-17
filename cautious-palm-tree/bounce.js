var c = document.getElementById("slate");
var ctx = c.getContext("2d");
var balls = [];

var Colors = ["red", "green", "blue", "yellow", "orange", "purple"];

var getColor = function() {
    index = Math.floor(Math.random() * Colors.length);
    return Colors[index];
};

var getSpeed = function() {
    change = Math.floor(Math.random()*10)-5;
    if (change == 0) {
	change += 1;
    };
    return change;
};

var Ball = function() {
    var xpos = Math.floor(Math.random()*(c.width-100))+50;
    var ypos = Math.floor(Math.random()*(c.height-100))+50;
    var xchange = getSpeed();
    var ychange = getSpeed();
    var radius = (Math.random()*20 + 15);
    var color = getColor();

    var move = function() {

	if (xpos >= c.width-radius || xpos <= radius) {
	    xchange *= -1;
	}
	if (ypos >= c.height-radius || ypos <= radius) {
	    ychange *= -1;
	}
	console.log(xchange);
	xpos += xchange;
	ypos += ychange;
	ctx.beginPath();
	ctx.arc(xpos,ypos,radius,0,Math.PI * 2);
	ctx.fillStyle=color;
	ctx.fill();	
	ctx.stroke();
    }

    var getRadius = function() {
	return radius;
    };

    var setSpeed = function(x, y) {
	xchange = x;
	ychange = y;
    };
    
    return {
	xpos:xpos,
	ypos:ypos,
	xchange:xchange,
	ychange:ychange,
	radius:radius,
	color:color,
	move:move,
	getRadius:getRadius,
	setSpeed:setSpeed
    };
};

var moveAll = function() {
    counter = 0;
    ctx.clearRect(0,0,c.width,c.height);
    while (counter < balls.length){
	balls[counter].move();
	counter ++;
    }
    window.requestAnimationFrame(moveAll);
};

var addBall = function() {
    newBall = Ball();
    balls.push(newBall);
};

var removeBall = function() {
    balls.pop();
};

var clearBall = function() {
    balls = [];
};

var filter = function() {
    balls.filter(function(ball){
	return ball.getRadius() > 25;
    }).map(function(ball){
	ball.setSpeed(0,0);
    });
};

var unfilter = function() {
    balls.map(function(ball){
	var X = (Math.random() * 3);
	var Y = (Math.random() * 3);
	ball.setSpeed(X,Y);
    });
};

var flock = function() {
    balls.map(function (ball) {
	ball.setSpeed(1,1)
    });
};

abutton = document.getElementById("add");
abutton.addEventListener("click", addBall);

rbutton = document.getElementById("remove");
rbutton.addEventListener("click", removeBall);

cbutton = document.getElementById("clear");
cbutton.addEventListener("click", clearBall);

fbutton = document.getElementById("filter");
fbutton.addEventListener("click", filter);

dbutton = document.getElementById("unfilter");
dbutton.addEventListener("click", unfilter);

ebutton = document.getElementById("flock");
ebutton.addEventListener("click",flock);

window.requestAnimationFrame(moveAll);
