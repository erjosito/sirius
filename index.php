<html>
<header>
<title>ACME MyApp1 2-Tier App PRD</title>
</header>
<body>
<font face="verdana"><center>
<img src="apic-dc_hero_banner.jpg">
<br>
<table width='100%' border=0><tr><td width='20%'></td><td width='60%'>
<h1>Testing an example 2-tier app</h1>
<p>In the following text you should see two sections, one per tier (Web and DB). If one of the tiers is down, the page will take longer to load (the request to that 
tier needs to time out, and eventually will show without that tier. If tier 2 is down, it doesnt matter whether tier 3 is up/down, that will not be shown.</p>

<h2>Tier 1 - Web</h2>
<p>You are seeing this page, so the tier 1 is working. The following WEB server is up and running: 172.18.1.11</p>


<h2>Tier 2 - DB</h2>
<p>Enter a name to find out its number, for example the names "jose" and "stefan" have been defined in the database. If you want to enter a SQL code injection attack, you can enter for example the following string: anything' OR 'x'='x</p>

<?php

function resultToArray($result) {
    $rows = array();
    while($row = $result->fetch_assoc()) {
        $rows[] = $row;
    }
    return $rows;
}

$name="";
$nameErr="";

if ($_SERVER["REQUEST_METHOD"] == "POST") {

  if (empty($_POST["name"])) {
    $nameErr = "Name is required";
  } else {
    $mysqli = new mysqli("172.18.2.11", "root", "cisco123", "numbers");
  
    /* check connection */
    if ($mysqli->connect_errno){
      printf("Connect failed: %s\n", $mysqli->connect_error);
      exit();
    }

    /* Select queries return a resultset */
    $name = $_POST["name"];
    if ($result = $mysqli->query("SELECT number FROM numbers WHERE name = '" . $name . "'")) {
      $rowcnt = $result->num_rows;
      //$row = $result->fetch_array (MYSQLI_NUM);
      $row = resultToArray($result);
      /* free result set */
      $result->close();
    }
  }
}
?>

<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
  Name:<br><input type='text' name='name' value='<?php echo $name;?>'>
  <br><br>
  <input type="submit" value="Submit">
</form>

<?php
  if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (strlen($row[0]['number'])>0) {
      echo "<p>" . $name . " has the telephone number:";
      foreach ($row as $number) {
        echo " " . $number['number'] . " ";
      }
    } else {
      if ($name) {
        echo "<p>";
        echo "No number found for " . $name;
      }
    }
  }
?>

<?php
  if (strlen($nameErr)>0) {
    echo "<p>";
    echo "Error accessing the database, no name specified";
  }
?>
</td><td width='20%'></td></tr></table>
</center></font>
</body>
</html>



