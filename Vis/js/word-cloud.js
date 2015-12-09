function drawCloud(infile, containerDiv) {
  var margin = {top: 20, right: 10, bottom: 20, left: 10};
  var width = 960 - margin.left - margin.right,
      height = 500 - margin.top - margin.bottom;
      scale = 700;

  //var nameScale = d3.scale.linear().range([10,150]);

  var fill = d3.scale.category20();
  d3.csv(infile, function(data) {
    var names = data
          .map(function(d) {return{text:d.word, size:+d.count/scale, count:+d.count};})
          .sort(function(a,b) {return d3.descending(a.size,b.size); })
          .slice(0,100);
    //nameScale.domain([
    //  d3.min(names, function(d) {return d.size;}),
    //  d3.max(names, function(d) {return d.size;})
    //  ]);

  d3.layout.cloud()
      .size([width,height])
      .words(names)
      .padding(1)
      .rotate(function() { return ~~(Math.random() * 2) * 90; })
      .font("Impact")
      .fontSize(function(d) { return d.size; })
      .on("end", draw)
      .start();
  });
  function draw(words) {
    containerDiv.append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
      .append("g")
        .attr("transform", "translate(" + (width / 2) + "," + (height / 2) + ")")
      .selectAll("text")
        .data(words)
      .enter().append("text")
        .style("font-size", function(d) { return d.size + "px"; })
        .style("font-family", "Impact")
        .style("fill", function(d, i) { return fill(i); })
        .attr("text-anchor", "middle")
        .attr("transform", function(d) {
          return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
        })
        .text(function(d) { return d.text; })
        .on("mouseover", mouseover)
        .on("mouseout", mouseout);
  };

  function mouseover(d){
    d3.select(this).style("font-size", d.size * 1.1 + "px");
    var offset = $(this).offset()
      //Update the tooltip position and value
    d3.select("#tooltip")
      .style("left", offset.left)
      .style("top", offset.top)
      .select("#value")
      .text(d.count);

    d3.select("#tooltip").classed("hidden", false);

  };
  function mouseout(d){
    d3.select(this).style("font-size", d.size / 1.1 + "px");
    d3.select("#tooltip").classed("hidden", true);
  };
}
