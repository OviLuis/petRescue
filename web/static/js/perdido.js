function getDatosPerdidos()
{
	$.ajax({
		url : "http://"+window.location.host+"/api/perdido", 
        type : "GET",   
        success : function(json) {
            console.log("completo");
			creaDivs(json);
        },
        error : function(xhr,errmsg,err) {
        	alert(xhr.status + ": " + xhr.responseText);
        }
    })
	.done(function(json){
		
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

function creaDivs(json) {

	var div_parent = $('#contenido');

	for (var i = 0, length = json.length; i < length ; i++ ) 
    {
        var messageChild = $("<div><h1><span> json[i]['especie'] </span></h1></div>");
		messageChild.attr('class','child');
	
		div_parent.append(messageChild);

		console.log(jason[i]);
        //var node2 = document.createTextNode(json[i]['especie']);
        //var node = document.createTextNode(json[i]['nombre']);
        
        //div_parent.appendChild(node2);
        //div_parent.appendChild(node);
        
        //document.getElementById("contenido").appendChild(div_parent);
    }
    
}
