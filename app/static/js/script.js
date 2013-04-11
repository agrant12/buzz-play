jQuery(document).ready(function(){
	$me = $('.me');

	$me.toggle(function(){
		$('header').animate({'top' : '500px'});
		$('.profile').animate({'margin-top': '0'});
	},
	function() {
		$('header').animate({'top' : '0px'});
		$('.profile').animate({'margin-top': '-500px'});
	});
});


