<html>
<header>
<title>ACME MyApp1 2-Tier App PRD</title>
</header>
<body>
<font face="verdana"><center>
<img src="apic-dc_hero_banner.jpg">
<br>
<table width='100%' border=0><tr><td width='20%'></td><td width='60%'>
<h1>Control panel for Sirius App1 Firewall Rules</h1>

<p>
This page can be used to control firewall rules for the application "App1" (tenant "<a href="https://muc-apic.cisco.com/#bTenants:SiriusCyber|uni/tn-SiriusCyber">SiriusCyber</a>") in ACI. The options below will modify the ruleset in the frontend or backend firewalls. If you want to insert or remove the firewalls, you can do so in <a href="sirius-ctrl.php">http://muc-server-01.cisco.com/sirius-ctrl.php</a>
</p>

<p>
You can test the MyApp application here: <a href="http://sirius-app1.cisco.com/index.php">http://sirius-app1.cisco.com/index.php</a>
</p>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $deleterule = $_POST["rules"];
  $newprot    = $_POST["prot"];
  $newport    = $_POST["port"];
  $neworder   = $_POST["order"];
  $newaddr    = $_POST["addr"];


  if ((isset($deleterule)) && (strlen($deleterule) > 0)) {
      system ("/usr/bin/python /root/asa-demo/delete-rule.py http://192.168.0.50 admin C15co123 " . $deleterule);
  }
  if ((isset($newprot)) && (isset($newport)) && (isset($neworder)) && (strlen($newport)>0) && (strlen($newprot)>0)) {
      $newrulename = "permit-" . $newport;
      if ($newaddr == "any") {
          system ("/usr/bin/python /root/asa-demo/create-rule.py http://192.168.0.50 admin C15co123 " . $newrulename . " " . $newprot . " " . $newport . " " . $neworder);
      } elseif ($newaddr == "epg") {
          system ("/usr/bin/python /root/asa-demo/create-rule-epg.py http://192.168.0.50 admin C15co123 " . $newrulename . " " . $newprot . " " . $newport . " " . $neworder);
      }
  }
}
?>

<h2>Existing rules</h2>
<p>Note that only one ACE can be deleted at a time</p>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">

<?php
  system ("/usr/bin/python /root/asa-demo/get-rules.py http://192.168.0.50 admin C15co123");
?>
  <br>
  Fill this data if you want to add a new ACE, otherwise leave blank:
  <br>
  ACE order:<br>
  <input type="text" name="order"><br>
  Destination Protocol (TCP or UDP):<br>
  <input type="text" name="prot"><br>
  Destination Port number:<br>
  <input type="text" name="port"><br>
  Destination IP address:<br>
  <input type="radio" name="addr" value="any" checked>Any<br>
  <input type="radio" name="addr" value="epg">EPG<br>
  <br>
  <input type="submit" value="Submit">
</form>

<p>
</p>


</td><td width='20%'></td></tr></table>
</center></font>
</body>
</html>


