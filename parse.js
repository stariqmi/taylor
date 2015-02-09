var net = require('net');
var request = require('request');
var cheerio = require('cheerio');

// Create a tcp server
// on a new connection
var server = net.createServer(function(conn) {
	conn.setEncoding('utf8');

	console.log('-> client connected');
	conn.on('end', function() {
		console.log('-> client disconnected');
	});

	// When new data comes in
	conn.on('data', dealWithData);
});

// Listen on port 8080
server.listen('8080', function() {
	console.log('-> TCP Server listening on port 8080');
});

function dealWithData(data) {
	console.log('-> data received');
	// console.log(data);

	// Data is a URL, make a request and parse the HTML
	var data = data.split('<=>');
	var address = data[0];
	var href = data[1];

	request(href, function(err, res, body) {
		var $ = cheerio.load(body);
		var info = $($('tr')[8]).children().first().text();
		var lines = info.split('\n');
		info = [];
		for (var i = 0; i < lines.length; i++) {
			info.push(lines[i].trim());
		};
		var result = {
			query: address, 
			name: info[1],
			address: info[2],
			city: info[3].split(',')[0],
			state: info[3].split(',')[1].trim().split(' ')[0],
			zip: info[3].split(',')[1].trim().split(' ')[1]
		};

		console.log(result);
	});
}