function checkBoxes(infile, ContainedDiv){
	d3.json(infile, function(error, freqData){
        if (error) throw error;
        
        var tagNames = [];
        freqData.forEach(function(d){
        	tagNames.push(Object.keys(d.freq));
        })

        var tagName = tagNames[0]; 

        var parentElement = document.getElementById('dashboard');

        tagName.forEach(function(g){
        	var checkbox = document.createElement('input');
        	checkbox.type = "checkbox";
        	checkbox.name = "dashboard";
        	checkbox.value = g;
        	checkbox.checked = true; 

        	parentElement.appendChild(checkbox);
        	checkbox.checked = true;

        	var label = document.createElement('label');
        	label.innerHTML = g;
        	parentElement.appendChild(label);
        	// console.log(label);

		})
    })
}
