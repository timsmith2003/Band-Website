<?php
    $phpSelf = htmlspecialchars($_SERVER['PHP_SELF']);
    $pathParts = pathinfo($phpSelf);
?>
<!DOCTYPE HTML>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>We Don't Have A Name Yet</title>
        <meta name="author" content="Trent & Tim">
        <meta name="description" content="Website advertising a band that needs a name">
        <link rel="stylesheet" href="css/custom.css?version=<?php print time(); ?>" type="text/css">
        <link rel="stylesheet" media="(max-width:800px)" href="css/custom-tablet.css?version=<?php print time(); ?>" type="text/css">
        <link rel="stylesheet" media="(max-width:600px)" href="css/custom-phone.css?version=<?php print time(); ?>" type="text/css">
        <meta name="viewport" content="width=device-width, initial scale=1.0">
        
    </head>
<?php
    print '<body class ="' . $pathParts['filename'] . '">';
    print '<!-- #################    Body element  ############## -->';
    include 'connect-DB.php';
    include 'header.php';
    include 'nav.php';
?>

