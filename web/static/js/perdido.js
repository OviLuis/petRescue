function getDatosPerdidos()
{
	$.ajax({
		url : "http://"+window.location.host+"/api/perdido/", 
        type : "GET",   
        success : function(json) {
            console.log("completo");
			creaDivs(json);
			console.log("perdidos");
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
	console.log("creaDivs");
	for (var i = 0, length = json.length; i <length ; i++ ) 
    {
    	console.log(json[i]['descripcion']);
        $('<p>').text(json[i]['nombre']).prependTo('#contenido').addClass("mascota");
    }
    
    
}
