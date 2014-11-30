function getDatosPerdidos()
{
	$.ajax({
		url : "http://"+window.location.host+"/api/perdido/", 
        type : "GET",   
        success : function(json) {
            console.log("completo");
            console.log(json);
		
		var div_parent = $('#contenido');
		for (var i = 0, length = json.length; i < length ; i++ ) 
		    {
		    	
        		var data = $('<div><h2><a href="">'+ json[i]['nombre'] + '</a></h2>'+
        							'<img src="{{MEDIA_URL}}{{mascota.'+json[i]['foto']+'}}">'+ 
        							'<p>'+ json[i]['descripcion'] + '</p>'+
        							'</div>');

				data.attr('class','child');
	
				div_parent.append(data);
			}
        },
        error : function(xhr,errmsg,err) {
        	alert(xhr.status + ": " + xhr.responseText);
        }
    })

	.done(function(json){
		console.log(json);
	});

}



function sendDatosPerdidos() {
	//obtiene el csrftoken
	var csrftoken = $.cookie('csrftoken');
	//url de la peticion
	url = 'http://'+window.location.host+'/api/perdido/';

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


