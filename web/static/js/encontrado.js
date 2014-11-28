function getDatosEncontrado()
{
	var form_encontrado = {
		nombre: $("#id_nombre").val(),
		raza: $("#id_raza").val(),
		edad: $("#id_edad").val(),
		especie: $("#id_especie").val(),
		sexo: $("#id_sexo").val(),
		descripcion: $("#id_descripcion").val(),
		fechaEncuentro: $("#id_fechaEncuentro").val(),
		dirEncuentro: $("#id_dirEncuentro").val(),
		foto: $("#id_foto").val()
		}
	console.log(form_encontrado)
	return form_encontrado;
}


function sendRequest (data) {
	//http://192.168.14.45/ajax2/server/main.php
	/*$.get("main.php", {lang: data}, function(response){
		$("#gretting").text(response)
	});*/

	url = 'http://'+window.location.host+'/api/perdido/'
	console.log(url)

	$.ajax({
		type: 'POST',
		url: url,
		data: data
	})
	.done(function(response){
		//$("#gretting").text(response)
		console.log("done")
	})
	.fail(function(error){
		//$("#gretting").text("Fail")	
		console.log("fail: "+ error.responseText)
		console.log(error)
	})
	.always(function(){
		//console.log("completo")
		console.log("always")
	})
}


$(document).ready(function(){
	$("#test_encontrado").click(function(){
	//$("#repotar_perdido_btn").click(function(){
		
		//sendRequest(getDatosPerdido());
		getDatosEncontrado()
	});

});