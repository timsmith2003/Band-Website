<?php
include 'top.php';
?>
<main>
<section class="grid3">
    <h2>Schedule</h2>
<table>
                    <tr>
                        <th>DATE</th>
                        <th>LOCATION</th>
                        <th>PERFORMANCE</th>
                </tr>
<?php
$sql = 'SELECT fldDate, fldLocation, fldPerformance FROM tblSchedule';
$statement = $pdo->prepare($sql);
$statement->execute();

$records = $statement->fetchAll();

foreach($records as $record){
    print '<tr>';
    print '<td>' . $record['fldDate'] . '</td>';
    print '<td>' . $record['fldLocation'] . '</td>';
    print '<td>' . $record['fldPerformance'] . '</td>';
    print '</tr>' . PHP_EOL;
}

?>
        </table>
</section>
        <section class="grid2">
            <h2>Planned Shows</h2>
            <p>Next year we will once again be living on the Redstone campus, and plan to do more dorm and common room shows in the Wing Davis Wilks building. We are also hoping to perform at some basement concerts and outside if the weather permits. We also plan to participate in the battle of the bands contest next year. The winner opens for the spring fest that year. Congratulations to Earthworm for winning this year. We are looking forward to competing next year.</p>
            <figure>
                <img alt="Spring Fest Poster" 
                 src="images/spring.jpg">
                <figcaption>Spring Fest 2023 <cite>UVM</cite></figcaption>
    </figure>
</section>
        <section class="grid1">
            <h2>Performance Etiquette</h2>
            <p>Not all concert venues can be as big as a stadium or Higher Ground. Some of the best concerts happen in people’s basements, in the houses where they live and it is important to be respectful. There has been a history of property destruction and assault at basement shows. Basement shows do get very crowded, but it is still very important to not break anything and to be respectful. Do not go into areas of the house that have been blocked off, don’t purposefully break things in people’s basements or hang onto water/gas pipes. Make sure to give everyone their personal space while dancing. Basement concerts are fun, and it is important that they remain fun for everyone else there and for the owners of the house and their neighbors. 
</p>
</section>
</main>
<?php
include 'footer.php';
?>