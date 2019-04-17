var pollData;
var liesData;

var displayTrump = function() {
    pollData = [
	{"x":"0", "y":"31.1"},
	{"x":"1", "y":"35.7"},
	{"x":"2", "y":"37.6"},
	{"x":"3", "y":"37.4"},
	{"x":"4", "y":"42.4"}
    ];
    liesData = [
	{"x": "1", "y":"10"},
	{"x": "2", "y":"23"},
	{"x": "3", "y":"37"},
	{"x": "4", "y":"50"},
	{"x": "5", "y":"72"}
    ]
    Clear("#pollGraph");
    Clear("#liesGraph");
    InitChart(pollData, "#pollGraph");
    InitChart(liesData, "#liesGraph");
};

var displayCruz = function() {
    pollData = [
	{"x":"0", "y":"11.6"},
	{"x":"1", "y":"15.3"},
	{"x":"2", "y":"16.9"},
	{"x":"3", "y":"18.7"},
	{"x":"4", "y":"26.7"}
    ];
    liesData = [
	{"x": "1", "y":"7"},
	{"x": "2", "y":"23"},
	{"x": "3", "y":"37"},
	{"x": "4", "y":"50"},
	{"x": "5", "y":"72"}
    ]
    Clear("#pollGraph");
    Clear("#liesGraph");
    InitChart(pollData, "#pollGraph");
    InitChart(liesData, "#liesGraph");
};


var displayClinton = function() {
    pollData = [
	{"x":"0", "y":"55.6"},
	{"x":"1", "y":"55.6"},
	{"x":"2", "y":"52.3"},
	{"x":"3", "y":"50.3"},
	{"x":"4", "y":"51.4"}
    ];
    liesData = [
	{"x": "1", "y":"4"},
	{"x": "2", "y":"8"},
	{"x": "3", "y":"12"},
	{"x": "4", "y":"16"},
	{"x": "5", "y":"20"}
    ]
    Clear("#pollGraph");
    Clear("#liesGraph");
    InitChart(pollData, "#pollGraph");
    InitChart(liesData, "#liesGraph");
};

var displaySanders = function() {
    pollData = [	
	{"x":"0", "y":"31.2"},
	{"x":"1", "y":"31.0"},
	{"x":"2", "y":"35.3"},
	{"x":"3", "y":"38.8"},
	{"x":"4", "y":"41.4"}
    ];
    liesData = [
	{"x": "1", "y":"2"},
	{"x": "2", "y":"2"},
	{"x": "3", "y":"3"},
	{"x": "4", "y":"3"},
	{"x": "5", "y":"4"}
    ]
    Clear("#pollGraph");
    Clear("#liesGraph");
    InitChart(pollData, "#pollGraph");
    InitChart(liesData, "#liesGraph");
};

$('li').click(function(e) {
    e.preventDefault();
    $('li').removeClass('active');
    if(this.id == "trump") {
	displayTrump();
    }
    else if (this.id == "cruz") {
	displayCruz();
    }
    else if (this.id == "clinton") {
	displayClinton();
    }
    else {			// Sanders
	displaySanders();
    }
    $(this).addClass('active');
});

function InitChart(lineData, location) {
    var vis = d3.select(location),
	WIDTH = 500,
	HEIGHT = 500,
	MARGINS = {
	    top: 20,
	    right: 20,
	    bottom: 20,
	    left: 50
	},
	xRange = d3.scale.linear().range([MARGINS.left, WIDTH - MARGINS.right]).domain(
	    [d3.min(lineData, function (d) {
		return d.x;
	    }),
	     d3.max(lineData, function (d) {
		 return d.x;
	     })
	    ]),
	
	
	yRange = d3.scale.linear().range([HEIGHT - MARGINS.top, MARGINS.bottom]).domain(
	    [d3.min(lineData, function (d) {
		return d.y;
	    }),
	     d3.max(lineData, function (d) {
		 return d.y;
	     })
	    ]),
	
	xAxis = d3.svg.axis()
	.scale(xRange)
	.tickSize(5)
	.tickSubdivide(true),
	
	yAxis = d3.svg.axis()
	.scale(yRange)
	.tickSize(5)
	.orient("left")
	.tickSubdivide(true);
    
    
    vis.append("svg:g")
	.attr("class", "x axis")
	.attr("transform", "translate(0," + (HEIGHT - MARGINS.bottom) + ")")
	.call(xAxis);
    
    vis.append("svg:g")
	.attr("class", "y axis")
	.attr("transform", "translate(" + (MARGINS.left) + ",0)")
	.call(yAxis);
    
    vis.append("text")
	.attr("x", 500)
	.attr("y", 500)
	.text("Months");
    
    
    var lineFunc = d3.svg.line()
	.x(function (d) {
	    return xRange(d.x);
	})
	.y(function (d) {
	    return yRange(d.y);
	})
	.interpolate('linear');
    
    vis.append("svg:path")
	.attr("d", lineFunc(lineData))
	.attr("stroke", "blue")
	.attr("stroke-width", 2)
	.attr("fill", "none");
    
}

function Clear(location){
    var vis = d3.select(location);
    vis.selectAll("*").remove();
}
//InitChart(pollData,'#pollGraph');
