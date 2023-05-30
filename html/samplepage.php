<?php include "../inc/dbinfo.inc"; ?>

<html>

<body>

<h1>Sample page</h1>

<?php

 /* Connect to MySQL and select the database. */

  $connection = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD);

  if(mysqli_connect_errno()) echo "Failed to connect to MySQL: " . mysqli_connect_error();

   $database = mysqli_select_db($connection, DB_DATABASE);

  /* Ensure that the Employees table exists. */

  VerifyEmployeesTable($connection, DB_DATABASE);

  /* If input fields are populated, add a row to the Employees table. */

  $employee_name = htmlentities($_POST['Name']);

  $employee_address = htmlentities($_POST['Address']);

   if(strlen($employee_name) || strlen($employee_address)) {

    AddEmployee($connection, $employee_name, $employee_address);

  }

?>

<!-- Input form -->

<form action="<?PHP echo $_SERVER['SCRIPT_NAME'] ?>" method="POST">

  <table border="0">

    <tr>

      <td>Name</td>

      <td>Address</td>

    </tr>

    <tr>

      <td>

        <input type="text" name="Name" maxlength="45" size="30" />

      </td>

      <td>

        <input type="text" name="Address" maxlength="90" size="60" />

      </td>

      <td>

        <input type="submit" value="Add Data" />

      </td>

    </tr>

  </table>

</form>

<!-- Display table data. -->

<table border="1" cellpadding="2" cellspacing="2">

  <tr>

    <td>ID</td>

    <td>Name</td>

    <td>Address</td>

  </tr>


</table>


</body>

</html>