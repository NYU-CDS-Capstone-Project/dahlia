$(document).ready(init);

function init() {

	// var dashFile = {'WhyImNotVotingForHillary': 'WhyImNotVotingForHillary','Hillary2016':'Hillary2016',
	//  				'HillaryClinton':'HillaryClinton', 'Hillary':'Hillary',
	// 				'tcot':'tcot'}

	drawCloud("data_o/wordCount.csv", d3.select('#word-cloud'));
	showReel("data_o/data_tweet.csv", d3.select('#showReel'));
	checkBoxes(d3.select('#dashboard'));
	drawDash(d3.select('#dashboard'));
	drawHier("data_o/hier_bund.json",d3.select('#hier'));
	drawSunburst("data_o/color_profile.json", "data_o/tweet_text.csv");

	var pieFiles = {'hashtag':'data_o/hashCount.csv',
	                'geolocation':'data_o/locaCount.csv',
	                'source':'data_o/sourceCount.csv',
	                'user':'data_o/userCount.csv'}
	
	selectPie(pieFiles, d3.select('#pie1'));
	drawTable('data_o/result_tweet.txt',d3.select('#table'));

	slide(d3.select('#slider'), d3.select('#sliderText'));

	$('.nav-sidebar').click(function() {
		$('.nav-sidebar').removeClass('active');
		$(this).addClass('active');
	});
}
