<?php

header("Access-Control-Allow-Origin","*");
$data = $_GET['a'];
	if ($data =="ok"){
		$url= "https://read-sensor-location.herokuapp.com//summary";
	}else{
		$url== "https://read-sensor-location.herokuapp.com//summary";
	}
$handle = fopen($url,"r");
if ($handle){
	while(!feof($handle)){
		$buffer = fgets($handle);
		echo $buffer;
	}
	fclose($handle);
}
?>