function sendDatosUsuario() {
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
		data: $("#formulario_usuario").serialize()
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
		//$("#gretting").text(response)
		console.log("done")
		$.cookie('nombre', 'mi nombre', { expires: 7, path: '/' });
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
