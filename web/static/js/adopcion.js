function getDatosAdopciones()
{
	$.ajax({
		url : "http://"+window.location.host+"/api/adopcion", 
        type : "GET",   
        success : function(json) {
            console.log("completo");
			
			var div_parent = $('#contenido');
		for (var i = 0, length = json.length; i < length ; i++ ) 
		    {
        		var data = $('<div><h2><span>'+ json[i]['nombre'] + '</span></h2>'+
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

/*
function creaDivs(json) {
	for (var i = 0, length = json.length; i < length ; i++ ) 
    {
        var div_parent = document.createElement("div");
        var node = document.createTextNode(json[i]['nombre']);
        div_parent.appendChild(node);
        document.getElementById("contenido").appendChild(div_parent);
    }
    
}*/


