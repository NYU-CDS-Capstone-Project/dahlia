$(document).ready(init);

function init() {
	drawCloud(d3.select('#word-cloud'));
	drawDash(d3.select('#dashboard'))
	drawHier(d3.select('#hier'));
	drawSunburst();

	$('.btn').click(function() {
		$('.btn').removeClass('active');
		$(this).addClass('active');
	});
}
