function drawDash(ContainerDiv) {
    d3.json('./data/dashboard_data.json', function(error, freqData){
        if (error) throw error;
        // var r0 = d3.selectAll('input[type="checkbox"]:checked').node().value;
        var r0 = $('input:checkbox:checked').map(function() {
            return this.value;
        }).get();

        dashboard(ContainerDiv,freqData,r0);

        d3.selectAll('input[type="checkbox"]').on('change', change);

        function change(){
            var radio = $('input:checkbox:checked').map(function() {
                return this.value;
            }).get();
            dashboard(ContainerDiv, freqData,radio); 
        }
    })
}

function dashboard(ContainerDiv, freqData, checkedValue) { 
    var barColor = 'pink';
    var tagNameDup = [];

    // tagName: values for the "checked" checkbox
    var tagName = checkedValue;
    
    // console.log(tagName);
    
    freqData.forEach(function(d){
        tagNameDup.push(
            Object.keys(d.freq)
        );
    });

    // the updated data according to checkedValue
    fData = [];
    freqData.forEach(function(d){
        freq_temp = {};
        Object.keys(d.freq).forEach(function(g){
            if (tagName.indexOf(g) > -1) {
                freq_temp[g] = d.freq[g];
            }
        });
        fData.push(
            {State:d.State,freq:freq_temp}
        );

    }); 
    
    var colorTotal = d3.scale.category20().range();
    
    // colorful and colorList are made for the most original set of tags
    // not altered by checked values
    // so that when checked values change, the color of each tag
    // does not change 
    var colorful = colorTotal.slice(0, tagNameDup[0].length);
    var colorList = toObject(tagNameDup[0],colorful);

    function toObject(names, values) {
        var result = {};
        for (var i = 0; i < names.length; i++)
            result[names[i]] = values[i];
        return result;
    }

    function segColor(c){ 
        return colorList[c];
    }

    function sum( obj ) {
        var sum = 0;
        for( var el in obj ) {
            if( obj.hasOwnProperty( el ) ) {
                sum += parseFloat( obj[el] );
            }
        }
        return sum;
    }

    
    // compute total for each state.
    fData.forEach(function(d){
        //d.total=sum(d.freq);
        d.total=0;
        for (var element in tagName){
            var thisOne = tagName[element];
            d.total += d.freq[thisOne];
        }
    });
    
    // function to handle histogram.
    function histoGram(fD){
        var hG={},    hGDim = {t: 60, r: 0, b: 30, l: 0};
        hGDim.w = 500 - hGDim.l - hGDim.r, 
        hGDim.h = 300 - hGDim.t - hGDim.b;
            
        //create svg for histogram.
        var hGsvg = ContainerDiv.select("svg.histogram");
        if (hGsvg.empty()) {
            hGsvg = ContainerDiv.append('svg')
                .classed('histogram', true);
        }
        //hGsvg.selectAll('*').remove();

        hGsvg
            .attr("width", hGDim.w + hGDim.l + hGDim.r)
            .attr("height", hGDim.h + hGDim.t + hGDim.b).append("g")
            .attr("transform", "translate(" + hGDim.l + "," + hGDim.t + ")");

        // create function for x-axis mapping.
        var x = d3.scale.ordinal().rangeRoundBands([0, hGDim.w], 0.1)
                .domain(fD.map(function(d) { return d[0]; }));

        // Add x-axis to the histogram svg.
        hGsvg.select('g.x.axis').remove();
        hGsvg.append("g").attr("class", "x axis")
            .attr("transform", "translate(0," + hGDim.h + ")")
            .call(d3.svg.axis().scale(x).orient("bottom"));

        // Create function for y-axis map.
        var y = d3.scale.linear().range([hGDim.h, 20])
                .domain([0, d3.max(fD, function(d) { return d[1]; })]);

        // Create bars for histogram to contain rectangles and freq labels.
        var bars = hGsvg.selectAll("g.bar-group").data(fD, function(data) {
            return data[0];
        });

        var barsEntered = bars.enter().append('g')
            .classed('bar-group', true);

        //create the rectangles.
        barsEntered
            .append("rect")
            .attr("class", "bar")
            .on("mouseover", mouseover)// mouseover is defined below.
            .on("mouseout", mouseout);// mouseout is defined below.
            
        //Create the frequency labels above the rectangles.
        barsEntered
            .append("text")
            .attr("text-anchor", "middle");

        bars.exit().transition().remove();

        bars.select('rect')
            .on('mouseover',mouseover)
            .on('mouseout', mouseout)
            .transition()
            .attr("x", function(d) { return x(d[0]); })
            .attr("y", function(d) { return y(d[1]); })
            .attr("width", x.rangeBand())
            .attr("height", function(d) { return hGDim.h - y(d[1]); })
            .attr('fill', barColor);

        bars.select('text')
            .transition()
            .text(function(d){ return d3.format(",")(d[1])})
            .attr("x", function(d) { return x(d[0])+x.rangeBand()/2; })
            .attr("y", function(d) { return y(d[1])-5; })

        
        function mouseover(d){  // utility function to be called on mouseover.
            // filter for selected state.
            var st = fData.filter(function(s){ return s.State == d[0];})[0],
                nD = d3.keys(st.freq).map(function(s){ return {type:s, freq:st.freq[s]};});
            // call update functions of pie-chart and legend. 

            pC.update(nD);
            leg.update(nD);
        }
        
        function mouseout(d){    // utility function to be called on mouseout.
            // reset the pie-chart and legend. 
            pC.update(tF);
            leg.update(tF);
            // console.log(tF);
        }
        
        // create function to update the bars. This will be used by pie-chart.
        hG.update = function(nD, color){
            // update the domain of the y-axis map to reflect change in frequencies.
            y.domain([0, d3.max(nD, function(d) { return d[1]; })]);
            
            // Attach the new data to the bars.
            var bars = hGsvg.selectAll("g.bar-group").data(nD);
            
            // transition the height and color of rectangles.
            bars.select("rect").transition().duration(500)
                .attr("y", function(d) {return y(d[1]); })
                .attr("height", function(d) { return hGDim.h - y(d[1]); })
                .attr("fill", color);

            // transition the frequency labels location and change value.
            bars.select("text").transition().duration(500)
                .text(function(d){ return d3.format(",")(d[1])})
                .attr("y", function(d) {return y(d[1])-5; });            
        }        
        return hG;
    }
    
    // function to handle pieChart.
    function pieChart(pD){
        var pC ={},    pieDim ={w:250, h: 250};
        pieDim.r = Math.min(pieDim.w, pieDim.h) / 2;
                
        // create svg for pie chart.
        var piesvg = ContainerDiv.select("svg.piechart");
        if (piesvg.empty()) {
            piesvg = ContainerDiv.append('svg')
                .classed('piechart', true);
        }
        piesvg = piesvg
            .attr("width", pieDim.w)
            .attr("height", pieDim.h)
            .append("g")
            .attr("transform", "translate("+pieDim.w/2+","+pieDim.h/2+")");
        
        // create function to draw the arcs of the pie slices.
        var arc = d3.svg.arc().outerRadius(pieDim.r - 10).innerRadius(0);

        // create a function to compute the pie slice angles.
        var pie = d3.layout.pie().value(function(d) { return d.freq; });

        // Draw the pie slices.
        var pies = piesvg.selectAll("path").data(pie(pD), function(d) {
            return d.data.type;
        });

        var piesEntered = pies.enter();
        piesEntered.append('path')
            .each(function(d) { this._current = d; })
            .on("mouseover", mouseover)
            .on("mouseout", mouseout);

        pies.exit().remove();
        
        pies
            .style("fill", function(d) {
                return segColor(d.data.type);
            })
            .attr("d", arc);

        // create function to update pie-chart. This will be used by histogram.
        pC.update = function(nD){
            piesvg.selectAll("path").data(pie(nD)).transition().duration(500)
                .attrTween("d", arcTween);
        }
        // Utility function to be called on mouseover a pie slice.
        function mouseover(d){
            // call the update function of histogram with new data.
            hG.update(
                fData.map(function(v){ 
                    return [v.State,v.freq[d.data.type]];
                })
                ,segColor(d.data.type));
        }
        //Utility function to be called on mouseout a pie slice.
        function mouseout(d){
            // call the update function of histogram with all data.
            hG.update(fData.map(function(v){
                return [v.State,v.total];}), barColor);
        }
        // Animating the pie-slice requiring a custom function which specifies
        // how the intermediate paths should be drawn.
        function arcTween(a) {
            var i = d3.interpolate(this._current, a);
            this._current = i(0);
            return function(t) { return arc(i(t));    };
        }    
        return pC;
    }
    
    // function to handle legend.
    function legend(lD){
        var leg = {};
            
        // create table for legend.
        
        var legend = ContainerDiv.selectAll("table.legend");
        if (legend.empty()) {
            legend = ContainerDiv.append('table')
                .attr('class','legend');
        }
        
        // create one row per segment.
        var tr = legend.select('tbody').remove('tr').selectAll("tr").data(lD).enter();
        
        if (legend.select('tbody').empty()){
            tr = legend.append("tbody")
            .selectAll('tr')
            .data(lD)
            .enter()
            .append("tr");
        }

        // create the first column for each segment.
        tr.append("td").append("svg").attr("width", '16').attr("height", '16').append("rect")
            .attr("width", '16').attr("height", '16')
            .attr("fill",function(d){ return segColor(d.type); });
            
        // create the second column for each segment.
        tr.append("td").text(function(d){ return d.type;});

        // create the third column for each segment.
        tr.append("td").attr("class",'legendFreq')
            .text(function(d){ return d3.format(",")(d.freq);});

        // create the fourth column for each segment.
        tr.append("td").attr("class",'legendPerc')
            .text(function(d){ return getLegend(d,lD);})

        // Utility function to be used to update the legend.
        leg.update = function(nD){
            // update the data attached to the row elements.
            var l = legend.select("tbody").selectAll("tr").data(nD);

            // update the frequencies.
            l.select(".legendFreq").text(function(d){ return d3.format(",")(d.freq);});

            // update the percentage column.
            l.select(".legendPerc").text(function(d){ return getLegend(d,nD);});        
        }
        
        function getLegend(d,aD){ // Utility function to compute percentage.
            return d3.format("%")(d.freq/d3.sum(aD.map(function(v){ return v.freq; })));
        }

        return leg;
    }
    
    // calculate total frequency by segment for all state.
    var tF = tagName.map(function(d){
        return {type:d, freq: d3.sum(fData.map(function(t){ 
            return t.freq[d];})
        )}; 
    }); 

    // calculate total frequency by state for all segment.
    var sF = fData.map(function(d){return [d.State,d.total];});

    var hG = histoGram(sF), // create the histogram.
        pC = pieChart(tF), // create the pie-chart.
        leg= legend(tF);  // create the legend.
}
