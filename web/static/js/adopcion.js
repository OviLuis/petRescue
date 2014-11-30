function getDatosAdopciones()
{
	$.ajax({
		url : "http://"+window.location.host+"/api/adopcion", 
        type : "GET",   
        success : function(json) {
            console.log(json);
			creaDivs(json);
        },
        error : function(xhr,errmsg,err) {
        	alert(xhr.status + ": " + xhr.responseText);
        }
    })
	.done(function(json){
		
	});
}


function sendDatosAdopcion() {
	//obtiene el csrftoken
	var csrftoken = $.cookie('csrftoken');
	//url de la peticion
	url = 'http://'+window.location.host+'/api/adopcion/';

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
		data: $("#formulario_adopcion").serialize()
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

function creaDivs(json) {
	
	for (var i = 0, length = json.length; i <length ; i++ ) 
    {
    	$('<div>').appendTo('#contenido').addClass("mascota").attr('id', 'info'+i);
    	$('<img src="/media/'+json[i]['foto']+'"/>').appendTo('#info'+i).addClass('imagenMascota');
    	$('<p>').text('Descripcion: '+json[i]['descripcion']).appendTo('#info'+i);
    	$('<p>').text('Nombre: '+json[i]['nombre']).prependTo('#info'+i);
    }   
}


