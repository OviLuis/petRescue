function getDatosEncontrados()
{
	$.ajax({
		url : "//"+window.location.host+"/api/encontrado/", 
        type : "GET",   
        success : function(json) {
            console.log("completo");
			creaDivs(json,"encontrados");
		
        },
        error : function(xhr,errmsg,err) {
        	alert(xhr.status + ": " + xhr.responseText);
        }
    })
	.done(function(json){
		
	})
	.always(function(){
		console.log("always")
		$("#loading").remove() 
	});
}

function sendDatosEncontrado(data) {
	//obtiene el csrftoken
	var csrftoken = $.cookie('csrftoken');
	//url de la peticion
	url = '//'+window.location.host+'/api/encontrado/';

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
		data: $("#formulario_encontrado").serialize()
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


function deleteEncontrado(id)
{
	var r = confirm("¿Está seguro que quiere eliminar?");
	if (r == true) {
	    	
		//obtiene el csrftoken
		var csrftoken = $.cookie('csrftoken');
		//url de la peticion
		url = '//'+window.location.host+'/api/encontrado/edit/'+id;

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
			console.log("encontrado eliminado");
			//$("#id-perd-"+id).remove()
		})
		.fail(function(error){
			console.log("fail")
			console.log("no se pudo borrar el perdido")
			
		})
		.always(function(){
			//console.log("completo")
			console.log("always");
		});

	} else {
	    
	}
}
