function getDatosAdopciones()
{
	$.ajax({
		url : "//"+window.location.host+"/api/adopcion/", 
        type : "GET",   
        success : function(json) {
            console.log(json);
			creaDivs(json,"adopciones");
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


function sendDatosAdopcion() {
	//obtiene el csrftoken
	var csrftoken = $.cookie('csrftoken');
	//url de la peticion
	url = '//'+window.location.host+'/api/adopcion/';

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



