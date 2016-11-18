var mybutton = document.getElementById('loadbutton');
mybutton.onclick = function() {
	var request;
	if (window.XMLHttpRequest) {
		request = new XMLHttpRequest();
	} else {
		request = new ActiveXObject("Microsoft.XMLHTTP");
	}
	request.open('GET', 'data.json');
	request.onreadystatechange = function() {
		if ((request.readyState===4) && (request.status===200)) {

			var items = JSON.parse(request.responseText);
			// console.log(items);

			var output = '<ul>';
			for (var key in items) {
				output += '<li>' + items[key].name + '</li>';
			}
			output += '</ul';
			document.getElementById('update').innerHTML = output;

			// console.log(request.responseXML.getElementsByTagName('name')[1].firstChild.modeValue);

			// var items = request.responseXML.getElementsByTagName('name');
			// var output = '<ul>';
			// for (var i = 0; i < items.length; i++) {
			// 	output += '<li>' + items[i].firstChild.nodeValue + '</li>';
			// }
			// output += '</ul>';
			// document.getElementById('update').innerHTML = output;

			// var modifyID = document.getElementById('update');
			// modifyID.innerHTML = request.responseText;

			// var modifyTag = document.getElementsByTagName('ul')[1].getElementsByTagName('li');
			// modifyTag[2].innerHTML = request.responseText;

			// var modifyTag = document.getElementsByTagName('li');

			// for(var i = 0; i < modifyTag.length; i++) {
			// 	modifyTag[i].innerHTML = request.responseText;
			// }
		}	
	}
	request.send();
} // loadAJAX