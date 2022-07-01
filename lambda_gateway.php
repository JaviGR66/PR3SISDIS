

<?php

	$aws_access_key_id='ASIASHFGZT5CFWFEI7EP';
	$aws_secret_access_key='WtUZewXxQSMQAqwFC1/3PLgcS+dGdqk8uZcfoQ5N';
	$aws_session_token='FwoGZXIvYXdzELH//////////wEaDANStO6nfZZrmHuoRSK8AVBWuOp7MlSDQcVlWmuocY9WgDzt1FL48LA7IdO4s41jQ8P4eyJadVq6Ng8JDIzccTBfgncPVOJkoyXw/+cxv4lfILJeTfFdIEdXDgVvogfbIWi4NWEXP/EotsDLNEhMOHZk8fz2re8PvqGjv3E4N2OklH0/l7UnJZqzLkdMFw6+90iOEkUAERlHFvVO3gGxQLP4Zy5zHaoR1+lgiJk2iJVGxGbMkcQt/BywxsXqhLHZMjUrzonfamppB87YKM/8p5UGMi2P84mFMcDpkFEcnUXoz7R3GzelJPbzrEH3dx4cuwkM2WbtZDt5v9lmwUTLb0k=';
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



