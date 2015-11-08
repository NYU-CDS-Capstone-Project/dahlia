$(document).ready(init);

function init() {
	drawCloud(d3.select('#word-cloud'));

	$('.btn').click(function() {
		$('.btn').removeClass('active');
		$(this).addClass('active');
	});
}
