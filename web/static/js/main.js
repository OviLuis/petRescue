var main = function(){

	console.log('ready');

	(function () {
		console.log('popover');
  		$('[data-toggle="popover"]').popover();
	})
	();
			/*$("#cat_perdidos").click(function() {
        getDatosPerdidos();
        return true;
    });*/



	//console.log($.cookie());

	console.log($.cookie());
	//si hay  un usuario autenticado -> elimino los formularios



	/*$('#myButton').popover();*/


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
