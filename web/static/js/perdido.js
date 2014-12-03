function getDatosPerdidos()
{
	$.ajax({
		url : "http://"+window.location.host+"/api/perdido/", 
        type : "GET",   
        success : function(json) {
            console.log("completo");
            console.log(json.next);
             console.log(json);
			creaDivs(json.results);
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

function creaDivs(json) {
	
	for (var i = 0, length = json.length; i <length ; i++ ) 
    {
    	var data = $('<div class = "mascota col-md-4">'+
    					'<div class= "col-md-6">'+
    						'<a href="'+window.location.pathname + json[i]['id']+'"><img class="img-thumbnail imagenMascota img-responsive" alt ="foto '+json[i]['nombre']+'" src="/media/'+json[i]['foto']+'"/></a>'+
    					'</div>'+
    					'<div class = "col-md-6">'+	
    						'<a href="/perdidos/'+json[i]['id']+'"><h1>'+json[i]['nombre']+'</h1></a>'+
        					'<hr>'+
        					'<p>'+ json[i]['descripcion'] + '</p>'+
						'</div>'+
					 '</div>');


    	$('#contenido').append(data);

    	
    }   

    // var next = $('<a href="'+ json[0]['next']+'">Página siguiente</a>')
    // 	$('#contenido').append(next);

    
}
