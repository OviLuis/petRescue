function getDatosPerdidos()
{
	$.ajax({
		url : "http://"+window.location.host+"/api/perdido/", 
        type : "GET",   
        success : function(json) {
            console.log("completo");
            console.log(json);

			creaDivs(json.results,"perdidos");

        },
        error : function(xhr,errmsg,err) {
        	alert(xhr.status + ": " + xhr.responseText);
        }
    })
	.done(function(json){
	})
	.always(function  () {
		$("#loading").remove() 
	})
	;
}

function deletePerdido(id)
{
	//obtiene el csrftoken
	var csrftoken = $.cookie('csrftoken');
	//url de la peticion
	url = 'http://'+window.location.host+'/api/perdido/edit/'+id;

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
		console.log("perdido eliminado");
		$("#id-perd-"+id).remove()
	})
	.fail(function(error){
		console.log("fail")
		console.log("no se pudo borrar el perdido")
		
	})
	.always(function(){
		//console.log("completo")
		console.log("always");
	});
}




function sendDatosPerdidos(event) {
	//obtiene el csrftoken
	var csrftoken = $.cookie('csrftoken');
	//url de la peticion
	url = 'http://'+window.location.host+'/api/perdido/edit/';

	//configura el csrftoken a la peticion ajax
	$.ajaxSetup({
    	beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
    	}
	});

	console.log(event.target)

	var formData = $("#formulario_perdido").serialize();
    //include video thumb src
    	//formData += '&foto=' + $("#id_foto")[0].files[0]

		//formData = formData + '&foto=' + value;


	console.log(formData);

	//peticion ajax
	$.ajax({
		type: 'POST',
		url: url,
		data: formData
	})
	.done(function(response){
		//$("#gretting").text(response)
		console.log("done");
		$("#formulario_perdido").remove()
		$("#msg-success").append("<span>Publicado</span>")
		event.preventDefault();
	})
	.fail(function(error){
		//$("#gretting").text("Fail")	
		console.log("fail: "+ error.responseText);
				event.preventDefault();


	})
	.always(function(){
		//console.log("completo")
		console.log("always");
	});

}

function creaDivs(json, path) {
	
	var data="";

	for (var i = 0, length = json.length; i <length ; i++ ) 
    {

    	if(path=='encontrados' || path=='adopcion'){
    		console.log("entor");
    		data = $('<div class = "mascota col-md-4" id="id-post-'+json[i]['id']+'">'+
    					'<div class= "col-md-6">'+
    						'<a href="'+window.location.pathname + json[i]['id']+'"><img class="img-thumbnail imagenMascota img-responsive" alt ="foto '+json[i]['nombre']+'" src="/media/'+json[i]['foto']+'"/></a>'+
    					'</div>'+
    					'<div class = "col-md-6">'+	
    						'<a id="enlace" href="/perdidos/'+json[i]['id']+'"><h1>'+json[i]['nombre']+'</h1></a>'+
        					'<hr>'+
        					'<p>'+ json[i]['descripcion']+'</p>'+
						'</div>'+
					 '</div>');

    	}else if(path==='perdidos'){
    		data = $('<div class = "mascota col-md-4" id="id-perd-'+json[i]['id']+'">'+
    					'<div class= "col-md-6">'+
    						'<a href="'+window.location.pathname + json[i]['id']+'"><img class="img-thumbnail imagenMascota img-responsive" alt ="foto '+json[i]['nombre']+'" src="/media/'+json[i]['foto']+'"/></a>'+
    						'<figcaption>'+
    						 	'<a href="/reportarEncontrado">'+
        						'reportar como encontrada'+
        						'</a>'+	
    						 '</figcaption>'+
    					'</div>'+
    					'<div class = "col-md-6">'+	
    						'<a id="enlace" href="/perdidos/'+json[i]['id']+'"><h1>'+json[i]['nombre']+'</h1></a>'+
        					'<hr>'+
        					'<p>'+ json[i]['descripcion'] +'</p>'+
						'</div>'+
					 '</div>');	
    	}

    	//si el usuari que se encuentra autenticado es quien creó la publicacion

    	$('#contenido').append(data);

    }   

    // var next = $('<a href="'+ json[0]['next']+'">Página siguiente</a>')
    // 	$('#contenido').append(next);

    
}
