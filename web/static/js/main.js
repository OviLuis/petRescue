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
		//html para login y registro
		$("#login").remove()
		$("#registro").remove()		
	}

};



$(document).ready(main);
