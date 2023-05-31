<?php
$conn = mysqli_connect(
  'mysql-cluster-test.cluster-ceu1cbdwfs8l.ap-northeast-2.rds.amazonaws.com', // 주소
  'admin',
  'wnsvy486',
  'test'); // 데이터베이스 이름

$sql = "SELECT * FROM number";
$result = mysqli_query($conn, $sql);

?>
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>WEB</title>
  </head>
  <body>
    <h1>Hoseo University</h1>
    <h3> 당신의 번호를 입력하세요. </h3>
    <form action="process_create.php" method="POST">
      <p><input type="text" name="NUM" placeholder="번호 (ex)12"></p>
      <p><input type="submit"></p>
    </form>
  </body>
</html>