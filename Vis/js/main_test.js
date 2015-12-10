$(document).ready(init);

function init() {
	drawCloud('./data_o/word.csv', d3.select('#word-cloud'));
	showReel('./data_o/data_tweet.csv', d3.select('#showReel'));
	checkBoxes('./data_o/dashboard_data.json', d3.select('#dashboard'));
	drawDash('./data_o/dashboard_data.json', d3.select('#dashboard'));
	drawHier('./data_o/hier_bund.json', d3.select('#hier'));
	drawSunburst('./data_o/tweet_text.csv', "data_o/color_profile.json", d3.select("#chart"));
	drawTable('data_o/tweet.csv',d3.select('#table'));
	slide('data_o/result_tweet.txt', d3.select('#slider'),d3.select('#table'),d3.select('#sliderText'));
	stackedArea('data_o/data_tweet.json', d3.select('#horizonGraph svg'));

	var pieFiles = {'hashtag':'data_o/hashtag.csv',
	                'coordinates':'data_o/coordinates.csv',
	                'source':'data_o/source.csv',
	                'user':'data_o/mention.csv'}	
	selectPie(pieFiles, d3.select('#pie1'));
	$('.placeholders').hide(); 
	$('#plot1').show();

	
	$('#b1').click(function(){
		$('.placeholders').slideUp();
		$('#plot1').slideDown();
	});
	$('#b2').click(function(){
		$('.placeholders').slideUp();
		$('#plot2').slideDown();
	});
	$('#b3').click(function(){
		$('.placeholders').slideUp();
		$('#plot3').slideDown();
	});
	$('#b4').click(function(){
		$('.placeholders').slideUp();
		$('#plot4').slideDown();
	});
	$('#b5').click(function(){
		$('.placeholders').slideUp();
		$('#plot5').slideDown();
	});
	$('#b6').click(function(){
		$('.placeholders').slideUp();
		$('#plot6').slideDown();
	});
	$('#b7').click(function(){
		$('.placeholders').slideUp();
		$('#plot7').slideDown();
	});
	$('#b8').click(function(){
		$('.placeholders').slideUp();
		$('#plot8').slideDown();
	});

	$('#exp').click(function(){
		$('.placeholders').slideDown();
		var doc = new jsPDF();
		var specialElementHandlers = {
    	'#exp': function (element, renderer) {
        	return true;
        }
    };
        doc.fromHTML($('#main').html(), 15, 15, {
        	'width': 170,
            	'elementHandlers': specialElementHandlers
    	});
    	doc.save('Dahlia.pdf');
	});

	$('.nav-sidebar a').click(function() {
		$('.nav-sidebar a').removeClass('active');
		$(this).addClass('active');
	});
	$(function () {

    var specialElementHandlers = {
        '#editor': function (element,renderer) {
            return true;
        }
    };
});
}


