<?
// Используем cURL для формирования HTTP POST-запроса к Google API
// Пакет php5-curl
$file_to_upload = array('myfile'=>'@current.flac');
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL,"https://www.google.com/speech-api/v1/recognize?xjerr=1&client=chromium&lang=ru-RU");
curl_setopt($ch, CURLOPT_POST,1);
curl_setopt($ch, CURLOPT_HTTPHEADER, array("Content-Type: audio/x-flac; rate=16000"));
curl_setopt($ch, CURLOPT_POSTFIELDS, $file_to_upload);
curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
$result=curl_exec ($ch);
curl_close ($ch);

// Google возвращает JSON, поэтому парсим стандартной функцией. Доступна в PHP 5.2
$json_array = json_decode($result, true);
$voice_cmd = $json_array["hypotheses"][0]["utterance"];

// Ищем в ответе Google наши команды.
// Если находим, выполняем заранее запрограммированное действие. В данном случае, вывод на экран
if(isset($json_array["hypotheses"][0]))
  echo $voice_cmd;

?>
