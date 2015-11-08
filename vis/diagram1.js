 function drawDiagram(containerDiv) {
 	var margin = {top: 10, right: 30, bottom: 30, left: 30},
	    width = 960 - margin.left - margin.right,
	    height = 500 - margin.top - margin.bottom;

	var svg = containerDiv.append("svg")
	    .attr("width", width + margin.left + margin.right)
	    .attr("height", height + margin.top + margin.bottom);

	var data = [{x: 10, height: 100}, {x:20, height: 777}];
	var bars = svg.selectAll(".bar").data(data);

	bars.enter().append('rect');
	bars.exit().remove();
	bars.attr('x', function(element) {
		  return element.x;
		})
		.attr('y', 10)
	    .attr("width", 10)
	    .attr("height", function(element) {
	    	return element.height;
	    });
	};