function selectPie(infileObj, containerDiv){ 
  var r0 = d3.select('input[name="pieChart"]:checked').node().value;
  drawPie(infileObj[r0], containerDiv);
  d3.selectAll("input").on("change", change);
  function change(){
    var radio = d3.select('input[name="pieChart"]:checked').node().value;
    drawPie(infileObj[radio], containerDiv); 
  }



 function drawPie(infile, containerDiv) {
  d3.csv(infile, function(error, data) {
    var piedata = data
          .map(function(d) {return{key:d.word, y:+d.count};})
          .sort(function(a,b) {return d3.descending(a.y,b.y);})
    var plotPiedata = piedata.slice(0,10);
    var other = d3.sum(piedata.slice(10,piedata.length), function(d) {return d.y;});
    plotPiedata.push({key: 'other', y: other});
    
    var margin = {top: 10, right: 10, bottom: 10, left: 10};
    var width = 960 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;
    nv.addGraph(function() {
        var chart = nv.models.pieChart()
            .x(function(d) { return d.key })
            .y(function(d) { return d.y })
            .width(width)
            .height(height);

        containerDiv
            .datum(plotPiedata)
            .attr('width', width)
            .attr('height', height)
            .call(chart);

        return chart;
        });
    });
  };
}