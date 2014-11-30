// function creaDivs(json) {

// 	console.log("esto es creaDivs");

// 	//var div_parent = $('#contenido');

// 	for (var i = 0, length = json.length; i < length ; i++ ) 
//     {
        
//         //var node2 = document.createTextNode(json[i]['especie']);
//         var node = document.createTextNode(json[i]['especie']);
        
//         //div_parent.appendChild(node2);
//         div_parent.appendChild(node);
        
//         document.getElementById("contenido").appendChild(div_parent);
//     }
    
// }


function getDatosPerdidos()
{
	$.ajax({
		url : "http://"+window.location.host+"/api/perdido", 
        type : "GET",   
        success : function(json) {
            console.log("completo");
            console.log(json);
		
		var div_parent = $('#contenido');
		for (var i = 0, length = json.length; i < length ; i++ ) 
		    {
		    	
        		var messageChild = $('<div><h2><span>'+ json[i]['nombre'] + '</span></h2>'+
        							'<img src="{{MEDIA_URL}}{{mascota.'+json[i]['foto']+'}}">'+ 
        							'<p>'+ json[i]['descripcion'] + '</p>'+
        							'</div>');

				messageChild.attr('class','child');
	
				div_parent.append(messageChild);
			}
        },
        error : function(xhr,errmsg,err) {
        	alert(xhr.status + ": " + xhr.responseText);
        }
    })
	
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


