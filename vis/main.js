$(document).ready(init);

function init() {
	drawDiagram(d3.select('#d1'));
	drawDiagram(d3.select('#d2'));

	$('.btn').click(function() {
		$('.btn').removeClass('active');
		$(this).addClass('active');
	});
}
