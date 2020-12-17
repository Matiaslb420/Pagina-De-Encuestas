let textarea_cantidad = 2
function add(){
	if(textarea_cantidad < 10){
		let li = document.createElement("li");
		let input = document.createElement("input")
		textarea_cantidad += 1
		input.type = "text";
		input.name = "respuesta" + textarea_cantidad;
		input.placeholder = "Respuesta";
		input.maxLength = 40; 
		console.log(input)
		li.id = "textarea"+ textarea_cantidad
		li.append(input);
		let ol = document.getElementById("agregar_textarea");
		ol.appendChild(li);
	}
}

function remove(){
	if(textarea_cantidad > 2){
		document.getElementById("agregar_textarea").removeChild(document.getElementById("textarea"+ textarea_cantidad))
		textarea_cantidad -= 1
	}
	
}
