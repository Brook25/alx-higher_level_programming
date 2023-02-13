#!/usr/bin/node

req = require('request');

req.get(process.argv[2], function (error, resp, body) {
	if (error) console.log(error);
	const bod = JSON.parse(body);
	var all_usrs = {}; var j = 0; let i = 0;
	while (i < bod.length) {
		if (bod[i]['userId'] != j) {
			j += 1;
			all_usrs[j] = 0;}
		if (bod[i]['userId'] == j && bod[i]['completed'] === true)
			all_usrs[j] += 1;
		i += 1; }
	console.log(all_usrs); });
