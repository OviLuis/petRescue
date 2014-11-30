function getDatosPerdidos()
{
	$.ajax({
		url : "http://"+window.location.host+"/api/perdido/", 
        type : "GET",   
        success : function(json) {
            console.log("completo");
            console.log(json);		
			creaDivs(json);

			


        },
        error : function(xhr,errmsg,err) {
        	alert(xhr.status + ": " + xhr.responseText);
        }
    })
	.done(function(json){
		console.log(json);
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

	//peticion ajax
	$.ajax({
		type: 'POST',
		url: url,
		data: $("#formulario_perdido").serialize()
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
    	var data = $('<div class = "mascota row">'+
    					'<div class= "col-md-4">'+
    						'<img class="imagenMascota" src="/media/'+json[i]['foto']+'"/>'+
    					'</div>'+
    					'<div class = "col-md-8">'+	
    						'<h2>'+json[i]['nombre']+'</h2>'+
        					'<p>'+ json[i]['descripcion'] + '</p>'+
						'</div>'+
					 '</div>');
    	$('#contenido').append(data);
    	/*$('<div>').appendTo('#contenido').addClass("mascota col-md-4").attr('id', 'info'+i);
    	$('<img src="/media/'+json[i]['foto']+'"/>').appendTo('#info'+i).addClass('imagenMascota');
    	$('<p>').text('Descripcion: '+json[i]['descripcion']).appendTo('#info'+i);
    	$('<p>').text('Nombre: '+json[i]['nombre']).prependTo('#info'+i);*/
    }   
}
