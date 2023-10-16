<?php
$databaseName = 'TJSNYDER_labs';
$dsn = 'mysql:host=webdb.uvm.edu;dbname=' . $databaseName;
$username = 'tjsnyder_writer';
$password = 'vt4ZjypvRv5u';
$pdo = new PDO($dsn, $username, $password);
?>