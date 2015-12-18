<html>
<header>
<title>ACME MyApp1 2-Tier App PRD</title>
</header>
<body>
<font face="verdana"><center>
<img src="apic-dc_hero_banner.jpg">
<br>
<table width='100%' border=0><tr><td width='20%'></td><td width='60%'>
<h1>Control panel for Sirius App1</h1>

<p>
This page can be used to control firewalling options for the application "App1" (tenant "<a href="https://muc-apic.cisco.com/#bTenants:SiriusCyber|uni/tn-SiriusCyber">SiriusCyber</a>") in ACI. The options below will insert or remove a frontend firewall (in front of the Web servers), or a backend firewall (between the Web and the DB servers).
</p>

<p>
You can test the MyApp application here: <a href="http://sirius-app1.cisco.com/index.php">http://sirius-app1.cisco.com/index.php</a>
</p>

<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {

  // Set some variables so that the form reflects the correct data
  $fefw = $_POST["FE"];
  $befw = $_POST["BE"];

  // Talk to the APIC
  if (isset($fefw) && $fefw == "Yes") {
    exec ("/usr/bin/python /root/asa-demo/insert-fe.py");
  } elseif (isset($fefw) && $fefw == "No") {
    exec ("/usr/bin/python /root/asa-demo/remove-fe.py");
  }
  if (isset($befw) && $befw == "Yes") {
    exec ("/usr/bin/python /root/asa-demo/insert-be.py");
  } elseif (isset($befw) && $befw == "No") {
    exec ("/usr/bin/python /root/asa-demo/remove-be.py");
  }
  
  // Update the picture
  if (($_POST["FE"]=="No") && ($_POST["BE"]=="No")) {
    $img = "Slide1.jpg";
  } elseif (($_POST["FE"]=="Yes") && ($_POST["BE"]=="No")) {
    $img = "Slide2.jpg";
  } elseif (($_POST["FE"]=="No") && ($_POST["BE"]=="Yes")) {
    $img = "Slide3.jpg";
  } elseif (($_POST["FE"]=="Yes") && ($_POST["BE"]=="Yes")) {
    $img = "Slide4.jpg";
  } 
  print "<p>Deployment at this time:</p>";
  print "<img src='" . $img . "'><br>";
} else {
  // Dont initialize on any value, dont show any default value in the option buttons, otherwise
  //    the user might think that is the current state of the fabric
  //$fefw = "No";
  //$befw = "No";
  $fesg = shell_exec ("/usr/bin/python /root/asa-demo/get-sg.py http://192.168.0.50 admin C15co123 out-to-app1 Subject");
  $besg = shell_exec ("/usr/bin/python /root/asa-demo/get-sg.py http://192.168.0.50 admin C15co123 App1-T2-Services App1-T2-Svc");
  if (strlen($fesg) > 1) {
    $fefw = "Yes";
  } else {
    $fefw = "No";
  }
  if (strlen($besg) > 1) {
    $befw = "Yes";
  } else {
    $befw = "No";
  }
  if (($fefw=="No") && ($befw=="No")) {
    $img = "Slide1.jpg";
  } elseif (($fefw=="Yes") && ($befw=="No")) {
    $img = "Slide2.jpg";
  } elseif (($fefw=="No") && ($befw=="Yes")) {
    $img = "Slide3.jpg";
  } elseif (($fefw=="Yes") && ($befw=="Yes")) {
    $img = "Slide4.jpg";
  }
  print "<p>Deployment at this time:</p>";
  print "<img src='" . $img . "'><br>";

  //print "<p>Deployment unknown at this time, please submit a design</p>";
}
?>

<p>If you want to change the deployment, choose one of the following options and click on "Submit". Please note that by doing so you will be modifying the network for tenant Sirius</p>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
  Please select whether you want frontend firewalling:<br>
  <input type="radio" name="FE" value="No" <?php if (isset($fefw) && $fefw=="No") echo "checked";?>>No Frontend Firewall<br>
  <input type="radio" name="FE" value="Yes" <?php if (isset($fefw) && $fefw=="Yes") echo "checked";?>>Frontend Firewall Inserted<br>
  <br>
  Please select whether you want backend firewalling:<br>
  <input type="radio" name="BE" value="No" <?php if (isset($befw) && $befw=="No") echo "checked";?>>No Backend Firewall<br>
  <input type="radio" name="BE" value="Yes" <?php if (isset($befw) && $befw=="Yes") echo "checked";?>>Backend Firewall Inserted<br>
  <br>
  <input type="submit" value="Submit">
</form>

</td><td width='20%'></td></tr></table>
</center></font>
</body>
</html>


