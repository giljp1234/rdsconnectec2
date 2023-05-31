<?php
$conn = mysqli_connect(
    'mysql-cluster-test.cluster-ceu1cbdwfs8l.ap-northeast-2.rds.amazonaws.com', // 주소
    'admin',
    'wnsvy486',
    'test'); // 데이터베이스 이름
  # title, description 이라는 사용자가 입력한 정보를 그대로 php에 입력하는 행위는 보안에 취약, 따라서 관리 필요

  $filtered = array(
    'NUM'=>mysqli_real_escape_string($conn, $_POST['NUM'])
  );

$sql = "
  INSERT INTO test
    (NUM, created)
    VALUES(
      '{$filtered['NUM']}'
        NOW()
    )
";
$result = mysqli_query($conn, $sql);
if($result === false){
  echo '저장하는 과정에서 문제가 생겼습니다. 관리자에게 문의해주세요';
  error_log(mysqli_error($conn));
} else {
  echo '성공했습니다. <a href="create.php">돌아가기</a>';
}
?>