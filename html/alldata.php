<?php
$conn = mysqli_connect(
  'mysql-cluster-test.cluster-ceu1cbdwfs8l.ap-northeast-2.rds.amazonaws.com', // 주소
  'admin',
  'wnsvy486',
  'test');

 echo '<h1>Database</h1>';

$sql = "SELECT * FROM number";
$result = mysqli_query($conn, $sql);
  while($row = mysqli_fetch_array($result)) {
    echo $row['NUM'].'<br>';
    echo $row['created'].'<br>'.'<br>';
}
?>