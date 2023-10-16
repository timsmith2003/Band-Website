<nav>
    <a class="<?php
    if ($pathParts['filename'] == "index") {
        print 'activePage';
    }
    ?>" href="index.php">Members</a>

<a class="<?php
    if ($pathParts['filename'] == "array") {
        print 'activePage';
    }
    ?>" href="array.php">Schedule</a>
    
    <a class="<?php
    if ($pathParts['filename'] == "detail") {
        print 'activePage';
    }
    ?>" href="detail.php">Music</a>
    
    <a class="<?php
    if ($pathParts['filename'] == "form") {
        print 'activePage';
    } 
    ?>" href="form.php">Survey</a>
</nav>