function getDatosPerdido()
{
	var form_perdido = {
		nombre: $("#id_nombre").val(),
		raza: $("#id_raza").val(),
		edad: $("#id_edad").val(),
		especie: $("#id_especie").val(),
		sexo: $("#id_sexo").val(),
		descripcion: $("#id_descripcion").val(),
		fechaDesaparicion: $("#id_fechaDesaparicion").val(),
		dirDesaparicion: $("#id_dirDesaparicion").val(),
		foto: $("#id_foto").val()
		}
	console.log(form_perdido)
	return form_perdido;
}


function sendRequest (data) {
	var csrftoken = $.cookie('csrftoken');

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
	$("#test_perdido").click(function(){
	//$("#repotar_perdido_btn").click(function(){
		
		sendRequest(getDatosPerdido());
	});

});