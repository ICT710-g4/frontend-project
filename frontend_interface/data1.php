<?php

$requestPayload = file_get_contents("php://input");
var_dump($requestPayload);
$myfile = fopen("data1.txt","w")or die("Unable to open file!");
$txt = "Menghorng\n";
fwrite($myfile,$requestPayload);
fclose($myfile);
?>