

<?php

	$aws_access_key_id="ASIASHFGZT5CCZH5DMRD"
	$aws_secret_access_key="IDC22SWJd7UR8rwacEvyHK8RFYzcew3ZfbxModS8"
	$aws_session_token="FwoGZXIvYXdzEC8aDL1PMDrWQf9XBR8sKiK8ATG3i6K9IPIgCh8v+S6XsFkfo5ozu1JXZZ/GVGC327M4jB5XxSE60ZCfNXLbTh/3uv4hWbhkr8IgSUkpSHv/yyDRqAl7MR7raYMz/MKGE2DVxC/Tbbku2KYWL3NgnNFeCTqPvcZUT6BbdhjezwYB0UhvrbN5lIt9qrrp/zx9L9YstVDoUC/KCn0Cduxud65S0PmY+MFPfi8BlA70gv+NUCal+9P38+HwqFm9Nojc4kVx/D5uV5JodeO6M5AmKNLu+5UGMi1wkTHRuwsRmVU8NfhXiL0ihpB8tspcQtVtLjbAAKBsFmEalqN/1JFc0j5zfRk="

	$lambda_func='login';
	$payload='{"queryStringParameters": {';

	foreach ($_GET as $key => $value) {

		$payload .= '"' . $key . '":"' . $value .'",';

	}

	$payload=substr($payload, 0, -1);

	$payload.='}}';

	$cmd=' AWS_ACCESS_KEY_ID='. $aws_access_key_id .

	     ' AWS_SECRET_ACCESS_KEY='. $aws_secret_access_key .

             ' AWS_SESSION_TOKEN='. $aws_session_token . ' aws lambda invoke --function-name --region us-east-1 '. $lambda_func . ' --payload \'' . $payload . '\' /tmp/resp.json 2>&1';

	exec( $cmd,$result,$result2);

	header('Access-Control-Allow-Origin: *');

	$result=file_get_contents("/tmp/resp.json");

	$json=json_decode($result,true);

        echo json_encode($json['body']);
?>



