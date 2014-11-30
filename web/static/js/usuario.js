function sendDatosRegistroUsuario() {
	//obtiene el csrftoken
	var csrftoken = $.cookie('csrftoken');
	//url de la peticion
	url = 'http://'+window.location.host+'/api/usuario/'

	//configura el csrftoken a la peticion ajax
	$.ajaxSetup({
    	beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
    	}
	});

	//peticion ajax
	$.ajax({
		type: 'POST',
		url: url,
		data: $("#formulario_registro_usuario").serialize()
	})
	.done(function(response){
		//$("#gretting").text(response)
		console.log("done")
	})
	.fail(function(error){
		//$("#gretting").text("Fail")	
		console.log("fail: "+ error.responseText)
		console.log(error)
	})
	.always(function(){
		//console.log("completo")
		console.log("always")
	})
}


function sendDatosLogin() {
	//obtiene el csrftoken
	var csrftoken = $.cookie('csrftoken');
	//url de la peticion
	url = 'http://'+window.location.host+'/api/auth/'

	//configura el csrftoken a la peticion ajax
	$.ajaxSetup({
    	beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
    	}
	});

	//peticion ajax
	$.ajax({
		type: 'POST',
		url: url,
		data: $("#formulario_login").serialize()
	})
	.done(function(response){
		$.cookie('usuario_id', response.id , { expires: 7, path: '/' });
		$.cookie('usuario_nombre', response.nombre , { expires: 7, path: '/' });
		$.cookie('usuario_email', response.email , { expires: 7, path: '/' });
		$("#login").remove()
		$("#registro").remove()
		
	})
	.fail(function(error){
		if(401 == error.status)
		{
			$('#msg-login-error').text('Datos de usuario Incorrectos');
		}

	})
	.always(function(){
		//console.log("completo")
		console.log("always")
	})
}
