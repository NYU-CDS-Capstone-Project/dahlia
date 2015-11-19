function selectPie(infileObj, containerDiv){ 
  var r0 = d3.select('input[name="pieChart"]:checked').node().value;
  drawPie(infileObj[r0], containerDiv);

  d3.selectAll("input")
      .on("change", change);

  function change(){
    var radio = d3.select('input[name="pieChart"]:checked').node().value;
    drawPie(infileObj[radio], containerDiv); 
  }



 function drawPie(infile, containerDiv) {
  d3.csv(infile, function(data) {
    var piedata = data
          .map(function(d) {return{key:d.word, y:+d.count};})
          .sort(function(a,b) {return d3.descending(a.y,b.y);})
    var plotPiedata = piedata.slice(0,5);
    var other = d3.sum(piedata.slice(5,piedata.length), function(d) {return d.y;});
    plotPiedata.push({key: 'other', y: other});
    
    var height = 550;
    var width = 550;
    nv.addGraph(function() {
        var chart = nv.models.pieChart()
            .x(function(d) { return d.key })
            .y(function(d) { return d.y })
            .width(width)
            .height(height);

        containerDiv
            .datum(plotPiedata)
            .transition().duration(1200)
            .attr('width', width)
            .attr('height', height)
            .call(chart);

        return chart;
        });
    });
  };
}