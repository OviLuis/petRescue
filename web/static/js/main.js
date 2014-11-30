var main = function(){
	
	console.log('ready');

	/*$("#cat_perdidos").click(function() {
        getDatosPerdidos();
        return true;
    });*/


	console.log($.cookie());
	//si hay  un usuario autenticado -> elimino los formularios
	if (verificarAutenticado())
	{
		$("#login").remove()
		$("#registro").remove()		
	}

	/*$('#myButton').popover();*/

};



$(document).ready(main);
