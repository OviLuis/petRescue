
$(document).ready(mostrar);


function mostrar(){
	$("#perdidos").click(function() {
                    
                    $.ajax({
                        url : "http://"+window.location.host+"/api/perdido", 
                        type : "GET",   
                        //dataType: "json",                
                        
                        success : function(json) {
                            $('result').append( 'Server Response: ' + json.server_response);
                            console.log(json);
                            //creaDivs();
                            
                        },
                        error : function(xhr,errmsg,err) {
                            alert(xhr.status + ": " + xhr.responseText);
                        }
                    });
                    ///return false;
            });
}


function creaDivs() {


    var element = document.getElementById("perdidos");
   // for (var i = 0, length = json.length; i <length ; i++ ) 
    //{
        var marco = "hola";
        var div = document.createElement("div");
        var node = document.createTextNode(marco);
        div.appendChild(node);
        element.appendChild(div);
        console.log( "este es el json");

   // }
    

}