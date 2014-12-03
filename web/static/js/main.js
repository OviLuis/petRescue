var main = function(){

	(function () {
  		$('[data-toggle="popover"]').popover();
	})
	();

	(function () {
	  $('[data-toggle="tooltip"]').tooltip()
	})
	();
			/*$("#cat_perdidos").click(function() {
        getDatosPerdidos();
        return true;
    });*/



	
};

var active = function()
{
	var elementos = document.getElementsByClassName('nav navbar-nav')[0].children;
	var localizacion = window.location.href;

	for (x in elementos)
		{
			if(localizacion == elementos[x].children[0].href)
				{
					elementos[x].setAttribute('class','active');
				}

		}
}




$(document).ready(main);
$(document).ready(active);
