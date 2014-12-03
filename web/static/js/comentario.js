function appendComentario(comentario)
{
	console.log("apend")
	//console.log(comentario.fechaPublicacion)
	
	var com_html = '<li id="id-cmt-'+comentario.id+'">';
	if(comentario.usuario.id == $.cookie('usuario_id') )
	{
		console.log("Autor")
		com_html += '<button type="button" class="close" data-toggle="tooltip" data-placement="top" title="Eliminar"><span aria-hidden="true" onclick=deleteComentario('+comentario.id+')>&times;</span><span class="sr-only">Close</span></button>';
	}
	com_html += '<h4>'+comentario.usuario.nombre+'</h4>'+
						'<p class="pull-right">'+jQuery.timeago(comentario.fechaPublicacion)+'</p>'+
					'</div>'+
						'<p>'+comentario.texto+'</p>'+
				'</li>';					
    					

	var data = $(com_html);


    $('#comentarios').append(data.timeago());

    $('#comentarios').append(data);
}

function deleteComentario(id)
{
	//obtiene el csrftoken
	var csrftoken = $.cookie('csrftoken');
	//url de la peticion
	url = '//'+window.location.host+'/api/comentario/edit/'+id;

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
		console.log("comentario eliminado");
		$("#id-cmt-"+id).remove()
	})
	.fail(function(error){
		console.log("fail")
		console.log("no se pudo borrar el comentario")
		
	})
	.always(function(){
		//console.log("completo")
		console.log("always");
	});
}

function sendComentario() {
	//obtiene el csrftoken
	var csrftoken = $.cookie('csrftoken');
	//url de la peticion
	url = '//'+window.location.host+'/api/comentario/edit/';

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
		url : "//"+window.location.host+"/api/comentario/"+idMascota+"/", 
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
