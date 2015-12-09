function horizonGraph(containerDiv) {
  var m = [20, 20, 30, 20],
      w = 960 - m[1] - m[3],
      h = 500 - m[0] - m[2];

  var x,
      y,
      duration = 2000,
      delay = 500;

  var color = d3.scale.category10();

  var svg = containerDiv.append("svg")
      .attr("width", w + m[1] + m[3])
      .attr("height", h + m[0] + m[2])
    .append("g")
      .attr("transform", "translate(" + m[3] + "," + m[0] + ")");

  var stocks,
      symbols;

  // A line generator, for the dark stroke.
  var line = d3.svg.line()
      .interpolate("basis")
      .x(function(d) { return x(d.date); })
      .y(function(d) { return y(d.price); });

  // A line generator, for the dark stroke.
  var axis = d3.svg.line()
      .interpolate("basis")
      .x(function(d) { return x(d.date); })
      .y(h);

  // A area generator, for the dark stroke.
  var area = d3.svg.area()
      .interpolate("basis")
      .x(function(d) { return x(d.date); })
      .y1(function(d) { return y(d.price); });

  d3.csv("data/data_tweet.csv", function(data) {
    var parse = d3.time.format("%b-%d-%Y-%H").parse;

    // Nest stock values by symbol.
    symbols = d3.nest()
        .key(function(d) { return d.symbol; })
        .entries(stocks = data);

    // Parse dates and numbers. We assume values are sorted by date.
    // Also compute the maximum price per symbol, needed for the y-domain.
    symbols.forEach(function(s) {
      s.values.forEach(function(d) { d.date = parse(d.date); d.price = +d.price; });
      s.maxPrice = d3.max(s.values, function(d) { return d.price; });
      s.sumPrice = d3.sum(s.values, function(d) { return d.price; });
    });

    // Sort by maximum price, descending.
    symbols.sort(function(a, b) { return b.maxPrice - a.maxPrice; });

    var g = svg.selectAll("g")
        .data(symbols)
      .enter().append("g")
        .attr("class", "symbol");

    setTimeout(lines, duration);
  });

  function lines() {
    x = d3.time.scale().range([0, w - 60]);
    y = d3.scale.linear().range([h / 4 - 20, 0]);

    // Compute the minimum and maximum date across symbols.
    x.domain([
      d3.min(symbols, function(d) { return d.values[0].date; }),
      d3.max(symbols, function(d) { return d.values[d.values.length - 1].date; })
    ]);

    var g = svg.selectAll(".symbol")
        .attr("transform", function(d, i) { return "translate(0," + (i * h / 4 + 10) + ")"; });

    g.each(function(d) {
      var e = d3.select(this);

      e.append("path")
          .attr("class", "line");

      e.append("circle")
          .attr("r", 5)
          .style("fill", function(d) { return color(d.key); })
          .style("stroke", "#000")
          .style("stroke-width", "2px");

      e.append("text")
          .attr("x", 12)
          .attr("dy", ".31em")
          .text(d.key);
    });

    function draw(k) {
      g.each(function(d) {
        var e = d3.select(this);
        y.domain([0, d.maxPrice]);

        e.select("path")
            .attr("d", function(d) { return line(d.values.slice(0, k + 1)); });

        e.selectAll("circle, text")
            .data(function(d) { return [d.values[k], d.values[k]]; })
            .attr("transform", function(d) { return "translate(" + x(d.date) + "," + y(d.price) + ")"; });
      });
    }

    var k = 1, n = symbols[0].values.length;
    d3.timer(function() {
      draw(k);
      if ((k += 2) >= n - 1) {
        draw(n - 1);
        setTimeout(horizons, 500);
        return true;
      }
    });
  }
  function horizons() {
    svg.insert("defs", ".symbol")
      .append("clipPath")
        .attr("id", "clip")
      .append("rect")
        .attr("width", w)
        .attr("height", h / 4 - 20);

    var color = d3.scale.ordinal()
        .range(["#c6dbef", "#9ecae1", "#6baed6"]);

    var g = svg.selectAll(".symbol")
        .attr("clip-path", "url(#clip)");

    area
        .y0(h / 4 - 20);

    g.select("circle").transition()
        .duration(duration)
        .attr("transform", function(d) { return "translate(" + (w - 60) + "," + (-h / 4) + ")"; })
        .remove();

    g.select("text").transition()
        .duration(duration)
        .attr("transform", function(d) { return "translate(" + (w - 60) + "," + (h / 4 - 20) + ")"; })
        .attr("dy", "0em");

    g.each(function(d) {
      y.domain([0, d.maxPrice]);

      d3.select(this).selectAll(".area")
          .data(d3.range(3))
        .enter().insert("path", ".line")
          .attr("class", "area")
          .attr("transform", function(d) { return "translate(0," + (d * (h / 4 - 20)) + ")"; })
          .attr("d", area(d.values))
          .style("fill", function(d, i) { return color(i); })
          .style("fill-opacity", 1e-6);

      y.domain([0, d.maxPrice / 3]);

      d3.select(this).selectAll(".line").transition()
          .duration(duration)
          .attr("d", line(d.values))
          .style("stroke-opacity", 1e-6);

      d3.select(this).selectAll(".area").transition()
          .duration(duration)
          .style("fill-opacity", 1)
          .attr("d", area(d.values))
          .each("end", function() { d3.select(this).style("fill-opacity", null); });
    });

    //setTimeout(areas, duration + delay);
  }

}