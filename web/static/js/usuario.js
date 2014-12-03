function sendDatosRegistroUsuario() {
	//obtiene el csrftoken
	var csrftoken = $.cookie('csrftoken');
	//url de la peticion
	url = 'http://'+window.location.host+'/api/usuario/';

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
		console.log("done");
	})
	.fail(function(error){
		//$("#gretting").text("Fail")	
		console.log("fail: "+ error.responseText);
		console.log(error);
	})
	.always(function(){
		//console.log("completo")
		console.log("always");
	});
}


function sendDatosLogin() {
	//obtiene el csrftoken
	var csrftoken = $.cookie('csrftoken');
	//url de la peticion
	url = 'http://'+window.location.host+'/api/auth/';

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
		console.log("autenticado");
		location.reload();		
	})
	.fail(function(error){
		if(401 == error.status)
		{
			$('#msg-login-error').text('Datos de usuario Incorrectos').addClass("alert alert-danger col-md-6");
		}

	})
	.always(function(){
		//console.log("completo")
		console.log("always");
	});
}


function logout() {
	//obtiene el csrftoken
	var csrftoken = $.cookie('csrftoken');
	//url de la peticion
	url = 'http://'+window.location.host+'/api/auth/';

	//configura el csrftoken a la peticion ajax
	$.ajaxSetup({
    	beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
    	}
	});

	//peticion ajax
	$.ajax({
		type: 'DELETE',
		url: url
	})
	.done(function(response){
		//$("#gretting").text(response)
		console.log("done");
		$.removeCookie('usuario_id');
		$.removeCookie('usuario_nombre');
		$.removeCookie('usuario_email');

		location.reload();
	})
	.fail(function(error){
		//$("#gretting").text("Fail")	
		console.log("fail: "+ error.responseText);
		console.log(error);
	})
	.always(function(){
		//console.log("completo")
		console.log("always");
	});
}


function getDatosUsuario()
{
	$.ajax({
		url : "http://"+window.location.host+"/api/usuario/edit/"+$.cookie('usuario_id'), 
        type : "GET",   
        success : function(json) {
            console.log("completo");
			console.log(json)
		},
        error : function(xhr,errmsg,err) {
        	alert(xhr.status + ": " + xhr.responseText);
        }
    })
	.done(function(json){
	})
	.always(function  () {
	})
	;
}