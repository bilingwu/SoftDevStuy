var Democrat = {
  "Alabama": 53,
  "Alaska": 16,
  "Arizona": 75,
  "Arkansas": 32,
  "California": 475,
  "Colorado": 66,
  "Connecticut": 55,
  "Delaware": 21,
  "Florida": 214,
  "Georgia": 102,
  "Hawaii": 25,
  "Idaho": 23,
  "Illinois": 156,
  "Indiana": 83,
  "Iowa": 44,
  "Kansas": 33,
  "Kentucky": 55,
  "Louisiana": 51,
  "Maine": 25,
  "Maryland": 95,
  "Massachusetts": 91,
  "Michigan": 130,
  "Minnesota": 77,
  "Mississippi": 36,
  "Missouri": 71,
  "Montana": 21,
  "Nebraska": 25,
  "Nevada": 35,
  "New Hampshire": 24,
  "New Jersey": 126,
  "New Mexico": 34,
  "New York": 257,
  "North Carolina": 107,
  "North Dakota": 18,
  "Ohio": 143,
  "Oklahoma": 38,
  "Oregon": 61,
  "Pennsylvania": 189,
  "Rhode Island": 24,
  "South Carolina": 53,
  "South Dakota": 20,
  "Tennessee": 67,
  "Texas": 222,
  "Utah": 33,
  "Vermont": 16,
  "Virginia": 95,
  "Washington": 101,
  "West Virginia": 29,
  "Wisconsin": 86,
  "Wyoming": 14
};

var DemocratAllotted = [
  "Iowa", "New Hamphsire", "Nevada", "South Carolina", "Alabama", "Arkansas",
  "Colorado", "Georgia", "Massachuetts", "Minnesota", "Oklahoma", "Tennessee",
  "Texas", "Vermont", "Viginia", "American Somoa", "Democrats Abroad",
  "Kansas", "Louisiana", "Nebraska", "Maine", "Michigan", "Mississippi",
  "Northern Mariana Islands", "Florida", "Illinois", "Missouri",
  "North Carolina", "Ohio"
];

var Republican = {
  "Alabama": 50,
  "Alaska": 28,
  "Arizona": 58,
  "Arkansas": 40,
  "California": 172,
  "Colorado": 37,
  "Connecticut": 28,
  "Delaware": 16,
  "Florida": 99,
  "Georgia": 76,
  "Hawaii": 19,
  "Idaho": 32,
  "Illinois": 69,
  "Indiana": 57,
  "Iowa": 44,
  "Kansas": 40,
  "Kentucky": 46,
  "Louisiana": 46,
  "Maine": 23,
  "Maryland": 38,
  "Massachusetts": 42,
  "Michigan": 59,
  "Minnesota": 38,
  "Mississippi": 40,
  "Missouri": 52,
  "Montana": 27,
  "Nebraska": 36,
  "Nevada": 30,
  "New Hampshire": 23,
  "New Jersey": 51,
  "New Mexico": 24,
  "New York": 95,
  "North Carolina": 72,
  "North Dakota": 28,
  "Ohio": 66,
  "Oklahoma": 43,
  "Oregon": 28,
  "Pennsylvania": 71,
  "Rhode Island": 19,
  "South Carolina": 50,
  "South Dakota": 29,
  "Tennessee": 58,
  "Texas": 155,
  "Utah": 40,
  "Vermont": 16,
  "Virginia": 49,
  "Washington": 44,
  "West Virginia": 34,
  "Wisconsin": 42,
  "Wyoming": 29
};

var RepublicanAllotted = [
  "Iowa", "New Hamphsire", "South Carolina", "Nevada", "Alabama", "Alaska",
  "Arkansas", "Georgia", "Massachuetts", "Minnesota", "Oklahoma",
  "Tennessee", "Texas", "Vermont", "Virginia", "Kansas", "Kentucky",
  "Louisiana", "Maine", "Puerto Rico", "Hawaii", "Idaho", "Michigan",
  "Mississippi", "Washington DC", "Guam", "Wyoming",
  "Florida", "Illinois", "Missouri", "North Carolina",
  "Northern Mariana Islands", "Ohio"
];

var DemocratDelegates = d3.values(Democrat);
var DemocratStates = d3.keys(Democrat);

var DemocratScale = d3.scale.linear()
  .domain([0, d3.max(DemocratDelegates)])
  .range([150, window.innerWidth/2 - 50]);

d3.select(".democrat.chart")
    .selectAll("div")
    .data(DemocratStates)
    .enter().append("div")
    .style("width", function(d) {
      return DemocratScale(Democrat[d]) + "px";
    })
    .text(function(d) {
      return Democrat[d] + ": " + d;
    })
    .style("background-color", function(d) {
      if (DemocratAllotted.indexOf(d) === -1) {
        return "lightblue";
      } else {
        return "blue";
      }
    });

var RepublicanDelegates = d3.values(Republican);
var RepublicanStates = d3.keys(Republican);

var RepublicanScale = d3.scale.linear()
  .domain([0, d3.max(RepublicanDelegates)])
  .range([150, window.innerWidth/2 - 50]);

d3.select(".republican.chart")
  .selectAll("div")
  .data(RepublicanStates)
  .enter().append("div")
  .style("width", function(d) {
    return RepublicanScale(Republican[d]) + "px";
  })
  .text(function(d) {
    return d + ": " + Republican[d];
  })
  .style("background-color", function(d) {
    if (RepublicanAllotted.indexOf(d) === -1) {
      return "red";
    } else {
      return "lightpink";
    }
  });
