function drawTable(infile, containerDiv, opt_n) {

    if (!containerDiv.empty()) {
        containerDiv.selectAll('*').remove();
    };
    var n = opt_n == null ? 10 : opt_n;
    var psv = d3.dsv("|", "text/plain");
    psv(infile, function(error, data) {
        var tweets = data
          .map(function(d) {return{count:+d.count,tweet:d.word};})
          .sort(function(a,b) {return d3.descending(a.count,b.count); })
          .slice(0,n);
    
    var Table = tabulate(tweets, ["count","tweet"]);
    // The table generation function
    function tabulate(data, columns) {
        var table = containerDiv.append("table")
                .attr("style", "margin-left: 50px", "margin-top:200px"),
            thead = table.append("thead"),
            tbody = table.append("tbody");

        // append the header row
        thead.append("tr")
            .selectAll("th")
            .data(columns)
            .enter()
            .append("th")
                .text(function(column) { return column; });

        // create a row for each object in the data
        var rows = tbody.selectAll("tr")
            .data(data)
            .enter()
            .append("tr");
        
        // create a cell in each row for each column
        var cells = rows.selectAll("td")
            .data(function(row) {
                return columns.map(function(column) {
                    return {column: column, value: row[column]};
                });
            })
            .enter()
            .append("td")
            .attr("style", "font-family: Courier") // sets the font style
                .html(function(d) { return d.value; });
        
        return table;
    };

    });
}

function slide(infile, containerDiv, tableDiv, textContainerDiv){ 
    containerDiv.call(d3.slider().axis(true).min(10)
        .on("slideend", function(evt, value) {
            drawTable(infile, tableDiv, value);
            textContainerDiv.text(value);  
        }));
};