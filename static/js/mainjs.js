$(document).ready(function() {
    $('#tabs a').click(function (e) {
        e.preventDefault();
        $(this).tab('show');
    });
	test = function () {
		$('#pick').click(function(event) {
			alert('aaa');	
		});
	}
})
