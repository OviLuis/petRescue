var main = function(){

	console.log('ready');
	console.log(window.location.href);
	console.log(window.location.pathname);
	
	$('.migasPan').append('<label>'+window.location.pathname+'</label>')

	/*$("#cat_perdidos").click(function() {
        getDatosPerdidos();
        return true;
    });*/



	//console.log($.cookie());

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
