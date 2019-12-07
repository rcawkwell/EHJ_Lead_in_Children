var width = 800;
var height = 700;

var svg = d3.select('#map-svg')
    .attr('width', width)
    .attr('height', height)

var projection = d3.geoMercator()
    .center([-73.9142, 40.6782])
    .scale(170000)


var path = d3.geoPath()
    .projection(projection);

var url = "https://gist.githubusercontent.com/rcawkwell/31d562ef5b0c8b2a109de98cab2bda0e/raw/bbfc5a7474b0c760682fc9fd3ac4eaa95538fc6c/nyc_neighborhood_areas.geojson"

var csv_url = "https://gist.githubusercontent.com/rcawkwell/a210dcc16afbd473ffe3963880b507ff/raw/516d56af6c5494626368d6b46077e1c7234b5801/gistfile1.txt"
d3.csv(csv_url, function(lead_data){
       d3.json(url, function(error, data){
        for (var i = 0; i<data['features'].length; i++){
            if (!data['features'][i]['properties']['ntacode'].includes('BK')){
               delete data['features'][i]
            }
            else{
               for (var j=0; j<lead_data.length; j++){
                    var nta = lead_data[j]['ntacode'];
                    var lead_lvl = lead_data[j].lead_lvl;
                    if((data['features'][i]['properties']['ntacode']) == nta){
                        data['features'][i]['properties']['lead'] = lead_lvl;
                    }
               }
            }
       }
               
       console.log(data)
       p = svg.selectAll('path')
           .data(data.features)
           .enter()
           .append('path')
           .attr('d', path)
           .on("mouseover", mouseover)
           .on("mouseout", mouseout)
           .style("fill", determineColor)
           .style("stroke", 'black')
           .style("stroke-width", 2)
       }
       );
       
       });

function mouseover(d){
    d3.select(this).style('opacity', '0.5');
    var tooltiptext = d3.select("#info-box")
                      .html(d.properties.ntaname + " <br> Avg. Lead Level: " + d.properties.lead +" <br> What to grow:");
    console.log(d)
}

function mouseout(d){
    d3.select(this).style('opacity', '1');
}

function determineColor(d){
    //var color = d.properties.lead/500
    //console.log("color", color)
    var color = Math.random()*.9;
    return d3.interpolateViridis(color)
}

function changeText(txt){
  document.getElementById("info-resources").innerHTML = txt;
}

