function appendComentario(comentario)
{
    $("#comentarios").append("<span>"+comentario.usuario+"</span>"
    	+"<span>"+comentario.texto+"</span>"
    	+"<span>"+comentario.fechaPublicacion+"</span>")
}


function sendComentario() {
	//obtiene el csrftoken
	var csrftoken = $.cookie('csrftoken');
	//url de la peticion
	url = 'http://'+window.location.host+'/api/comentario/edit/';

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
		data: $("#formulario_comentario").serialize()
	})
	.done(function(response){
		//$("#gretting").text(response)
		console.log("done");
		console.log(response)
		appendComentario(response)
	})
	.fail(function(error){
		console.log("fail")
		if(500 == error.status)
		{
			$('#msg-com-error').text('Debes iniciar session');
		}
		if (400 == error.status)
		{
			des = JSON.parse(error.responseText)
			$("#msg-com-error").text(des.texto)	
		}
		
	})
	.always(function(){
		//console.log("completo")
		console.log("always");
	});
}

function appendListaComentario (comentarios) {
	for (var i = comentarios.length - 1; i >= 0; i--) {
		appendComentario(comentarios[i])
	};
}

function getComentarios(idMascota)
{
	$.ajax({
		url : "http://"+window.location.host+"/api/comentario/"+idMascota+"/", 
        type : "GET",   
        success : function(json) {
        	//$("#comentarios").removeChilds()
			appendListaComentario(json);
			console.log(json)
        },
        error : function(xhr,errmsg,err) {
        	alert(xhr.status + ": " + xhr.responseText);
        }
    	});
}
