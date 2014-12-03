function appendComentario(comentario)
{
	var data = $('<li>'+
						'<button type="button" class="close" data-toggle="tooltip" data-placement="top" title="Eliminar"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>'+
    					'<h4>'+$.cookie('usuario_nombre')+'</h4>'+
						'<p class="pull-right">'+jQuery.timeago(comentario.fechaPublicacion)+'</p>'+
					'</div>'+
						'<p>'+comentario.texto+'</p>'+
				'</li>'
    			);
    $('#comentarios').append(data);
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
		$("#id_texto").val("")
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
        	$("#comentarios").empty()
			appendListaComentario(json);
			console.log(json)
			if (0 == json.length) 
			{
				console.log("vacio")
				$("#comentarios").append("<span>No hay comentarios<span>")
			};
			$("#ver_comentarios").remove()

        },
        error : function(xhr,errmsg,err) {
        	alert(xhr.status + ": " + xhr.responseText);
        }
    	});
}
