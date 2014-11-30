var main = function(){

	console.log('ready');


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
	var aux = ['http://localhost:8000/home', ''];


	}
	for (x in elementos)
		{
			console.log(elementos[x].children[0].href);

		}

}



$(document).ready(main);
$(document).ready(active);
