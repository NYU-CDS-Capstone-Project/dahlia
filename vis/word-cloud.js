function drawCloud(containerDiv) {
  var width = 750,
      height = 500;

  //var nameScale = d3.scale.linear().range([10,150]);

  var fill = d3.scale.category20();
  d3.csv("data/nameInTweet.csv", function(data) {
    var names = data
          .map(function(d) {return{text:d.word, size:+d.count};})
          .slice(10,100);
    //nameScale.domain([
    //  d3.min(names, function(d) {return d.size;}),
    //  d3.max(names, function(d) {return d.size;})
    //  ]);
  
  d3.layout.cloud()
      .size([width,height])
      .words(names)
      .padding(5)
      .rotate(function() { return ~~(Math.random() * 2) * 90; })
      .font("Impact")
      .fontSize(function(d) { return (d.size/100); })
      .on("end", draw)
      .start();
  });
  function draw(words) {
    containerDiv.append("svg")
        .attr("width", width)
        .attr("height", height)
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
        .text(function(d) { return d.text; });
  };
}
