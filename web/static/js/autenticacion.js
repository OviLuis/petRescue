
function verificarAutenticado () {
	if ( $.cookie('usuario_id') )
	{
		return true;
	}
	else
	{
		return false;
	}	
}

