var main = function(){
	
	console.log('ready');
	var currentPath = window.location.pathname;

	
	if ('/home/' === currentPath)
	{
		console.log('Inicio');
	}
	if ('/perdidos/' === currentPath)
	{
		console.log('Perdidos');
		inicializarPerdido();
		getDatosPerdidos();
	}
	if ('/adopciones/' === currentPath)
	{
		console.log('adopciones');
		inicializarAdopcion();
	}
	if ('/encontrados/' === currentPath)
	{
		console.log('encontrados');
		inicializarEncontrado();
	}
	

	

	/*$("#cat_perdidos").click(function() {
        getDatosPerdidos();
        return true;
    });*/

	inicializarPerdido();
	inicializarAdopcion();
	inicializarEncontrado();

}

function inicializarPerdido()
{
	$("#formulario_perdido").submit(function() {
		sendDatosPerdidos();
	});
}

function inicializarAdopcion()
{
	$("#formulario_adopcion").submit(function(){
        sendDatosAdopcion();
    });
}

function inicializarEncontrado(){
	
	$("#formulario_encontrado").submit(function(){
        sendDatosEncontrado();
    });
};


$(document).ready(main);
