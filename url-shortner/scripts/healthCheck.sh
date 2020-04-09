URL=$(sudo cat /home/ubuntu/airtxt/airtxt/ip)

echo "> curl -s ${URL}/api/skill/"

for RETRY_COUNT in {1..15}
do
  RESPONSE=$(curl -s ${URL}/api/skill/)
  UP_COUNT=$(echo $RESPONSE | grep '{' | wc -l)

  if [ $UP_COUNT -ge 1 ]
  then # $up_count >= 1 ("UP" 문자열이 있는지 검증)
      echo "> Health check 성공"
      break
  else
      echo "> Health check의 응답을 알 수 없거나 혹은 json이 아닙니다."
      echo "> Health check: ${RESPONSE}"
  fi

  if [ $RETRY_COUNT -eq 10 ]
  then
    echo "> Health check 실패. "
    exit 1
  fi

  echo "> Health check 연결 실패. 재시도..."
  sleep 10
done
exit 0