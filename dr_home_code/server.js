var express = require('express');
var bodyparser = require("body-parser");
var app = express();
var fs = require('fs');
var spawn = require("child_process").spawn;
var http = require('http');
var server = http.createServer(app);
var return_name,num_str='';
var path = require('path');
var spawn = require("child_process").spawn;
//var process = spawn('python',["path/to/script.py", arg1, arg2, ...]);


app.use(bodyparser.json());
app.use(bodyparser.urlencoded({extended : true}));
app.use(express.static(path.join(__dirname)));



app.get('/', function(req, res){
	//res.send('Hello');
	console.log('GET Received');
	var process = spawn('python3',["user_disease_fetch.py",]);
	res.send("Thank you for using the app \n The usage is ip:port/data/choice/input");	
	console.log('Server accessed by Client');
});

app.get('/data/:choice/:input', function (req, res) {  // ip:port/data/lskdnsknn;asnfg;%2
  	//res.sendFile( __dirname + "/try.txt");
  	var process = spawn('python',["user_disease_fetch.py",req.params.choice,req.params.input]);
  	console.log(req.params.choice,req.params.input);
  
  	process.on('close',function(){
	      	var obj = JSON.parse(fs.readFileSync('result.json'));
	  	var str = "";
	  	obj.forEach(function(item){
		  	str += item;
		  	str += '\n';	
  		});
  	
      	console.log(str);
  	res.send(str);
  	res.end();
  });
  
  //console.log(str);
  
});
app.listen(3000,function(err){
  if(err){
    console.log("port error");
  }
  else{
    console.log("connected sucessfully");
  }
});
