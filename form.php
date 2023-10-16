<?php
include 'top.php';
$favoriteGenres = array('Classic Rock', 'Alternative Rock', 'Indie', 'Folk', 'Acoustic');
$dataIsGood = false;
$errorMessage = '';
$message = '';

$favoriteGenre = '';
$bandName = '';
$name = '';
$email = '';
$instrument = '';
$audition = 1;

function getData($field) {
    if(!isset($_POST[$field])) {
        $data = "";
    } else{
        $data = trim($_POST[$field]);
        $data = htmlspecialchars($data);
    }
return $data;
    }
    function verifyAlphaNum($testString) {
        // Check for letters, numbers and dash, period, space and single quote only.
        // added & ; and # as a single quote sanitized with html entities will have 
        // this in it bob's will be come bob's
        return (preg_match ("/^([[:alnum:]]|-|\.| |\'|&|;|#)+$/", $testString));
    }
?>
<main>
        <section>
            <h2>Please take this survey</h2>
            <p>By taking this survey you will help us pick a band name</p>
        </section>
<?php
if($_SERVER["REQUEST_METHOD"] == 'POST'){
    print PHP_EOL . '<!-- Starting Sanitization -->' . PHP_EOL;
    $favoriteGenre = getData('lstFavoriteGenres');
    $bandName = getData('txtbandName');
    $name = getData('txtname');
    $email = getData('txtEmail');
    $email = filter_var($email, FILTER_SANITIZE_EMAIL);
    $instrument = getData('txtinstrument');
    $audition = getData('radaudition');

    print PHP_EOL . '<!-- Starting Validation -->' . PHP_EOL;

    $dataIsGood = true;

    if($favoriteGenre == ''){
        $errorMessage .= '<p class="mistake">Please choose a favorite genre</p>';
        $dataIsGood = false;
    } elseif(!in_array($favoriteGenre, $favoriteGenres)){
        $errorMessage .= '<p class="mistake">Please choose a favorite genre</p>';
        $dataIsGood = false;
    }
    if($bandName == ''){
        $errorMessage .= '<p class="mistake">Please enter an idea for a band name</p>';
        $dataIsGood = false;
    } elseif(!verifyAlphaNum($bandName)){
        $errorMessage .= '<p class="mistake">Name contains invalid characters please just use letters</p>';
        $dataIsGood = false;
    }
    if($name == ''){
        $errorMessage .= '<p class="mistake">Please enter your name</p>';
        $dataIsGood = false;
    } elseif(!verifyAlphaNum($name)){
        $errorMessage .= '<p class="mistake">Please only use letters</p>';
        $dataIsGood = false;
    }
    if($email == ''){
        $errorMessage .= '<p class="mistake">Please type in your email address</p>';
        $dataIsGood = false;
    } elseif(!filter_var($email, FILTER_VALIDATE_EMAIL)){
        $errorMessage .= '<p class="mistake">Your email address is invalid</p>';
        $dataIsGood = false;
    }

    if($instrument == ''){
        $errorMessage .= '<p class="mistake">Please enter an instrument</p>';
        $dataIsGood = false;
    } elseif(!verifyAlphaNum($instrument)){
        $errorMessage .= '<p class="mistake">Please just use letters</p>';
        $dataIsGood = false;
    }
    if ($audition != "Yes" AND $audition != "No"){
        $errorMessage .= '<p class="mistake">Please pick yes or no</p>';
        $dataIsGood = false;
    }

    print '<!-- Start Saving -->';
    if($dataIsGood) {
        $sql = 'INSERT INTO tblBandNameForm
        (fldFavoriteGenre, fldBandName, fldName, fldEmail, fldInstrument, fldAudition)
VALUES
        (?, ?, ?, ?, ?, ?)';
$data = array($favoriteGenre, $bandName, $name, $email, $instrument, $audition);
        

// $sqlText = $sql;
// foreach ($data as $value){
// // Look for ? and replace with the value
// // look for ? replace with value
// $pos = strpos($sqlText, '?');
// if ($pos !== false) {
// $sqlText = substr_replace($sqlText, '"' . $value . '"', $pos, strlen('?'));
// }
// }
// print '<p>' . $sqlText . '</p>';


        $statement = $pdo->prepare($sql);
            if($statement->execute($data)){
                $message .= '<h2>We value your input rockstar!</h2>';
                $to = $email;
                $from = 'Band Team <tjsnyder@uvm.edu>';
                $subject = 'Band Name Research';

                $mailMessage = '<p>Thank you for giving us band name ideas</p>';
                
                $headers = "MIME-Version: 1.0\r\n";
                $headers .= "Content-type: text/html; charset=utf-8\r\n";
                $headers .= "From:" . $from . "\r\n";

                $mailSent = mail($to, $subject, $mailMessage, $headers);

                if ($mailSent) {
                    print "<p>A copy of your form has been emailed to you.</p>";
                    print $mailMessage;
                }

            } else {
                $message .= '<p>Record was NOT successfully saved</p>';
                $dataIsGood = false;
            }
        }
    }
?>
        
        <section class = "grid7">
            <?php
            print $message;
            print $errorMessage;
            ?>
        </section>
        <section>
            <h2>Anything can be a band name</h2>
           <form action="#" id="frmFavGenre" method="post">

                <fieldset class="grid1">
                    <legend>Favorite Genre of Music</legend>
                    <p>
                        <select id="lstFavoriteGenre" name="lstFavoriteGenres" tabindex="120">
                            <option 
                            <?php if($favoriteGenre == "Classic Rock") print 'selected'; ?>
                            value="Classic Rock">Classic Rock</option>
                            <option
                            <?php if($favoriteGenre == "Alternative Rock") print 'selected'; ?>
                            value="Alternative Rock">Alternative Rock</option>
                            <option 
                            <?php if($favoriteGenre == "Indie") print 'selected'; ?>
                            value="Indie">Indie</option>
                            <option 
                            <?php if($favoriteGenre == "Folk") print 'selected'; ?>
                            value="Folk">Folk</option>
                            <option 
                            <?php if($favoriteGenre == "Acoustic") print 'selected'; ?>
                            value="Acoustic">Acoustic</option>
                        </select>
                    </p>
                </fieldset>

                <fieldset class="grid2">
                    <p>
                        <label class="required" for="txtbandName">What would be a good band name?</label>
                        <input type="text" id="txtbandName" name="txtbandName" tabindex="200" value = "<?php print $bandName; ?>">
                    </p>
                </fieldset>

                <fieldset class="grid3">
                    <p>
                        <label class="required" for="txtname">What is your name?</label>
                        <input type="text" id="txtname" name="txtname" tabindex="200" value = "<?php print $name; ?>">
                    </p>
                </fieldset>

                <fieldset class="grid4">
                    <legend>Contact information</legend>
                    <p>
                        <label class="required" for="txtEmail">Email</label>
                        <input id="txtEmail" maxlength="30" name="txtEmail" onfocus="this.select()" tabindex="305" type="email" value="<?php print $email; ?>" required>
                    </p>
                </fieldset>

                <fieldset class="grid5">
                    <p>
                        <label class="required" for="txtinstrument">What instrument do you play? If none type none</label>
                        <input type="text" id="txtinstrument" name="txtinstrument" tabindex="200" value = "<?php print $instrument; ?>">
                    </p>
                </fieldset>

                <fieldset class="grid6">
                    <legend>Would you like to audition to join our band?</legend>
                    <p>
                        <input type="radio" id="radYes" name="radaudition" value="Yes" tabindex="410" 
                        <?php if($audition == "Yes") print 'checked'; ?>
                        required>
                        <label class="radio-field" for="radYes">Yes</label>
                    </p>
                    <p>
                        <input type="radio" id="radNo" name="radaudition" value="No" tabindex="410" 
                        <?php if($bookNumber == "No") print 'checked'; ?>
                        required>
                        <label class="radio-field" for="radNo">No</label>
                    </p>
                </fieldset>

                <fieldset class="buttons">
                    <input id="btnSubmit" name="btnSubmit" tabindex="900" type="submit" value="Submit" class="sub">
                </fieldset>
            </form>
        </section>
    </main> 
<?php
include 'footer.php';
?>