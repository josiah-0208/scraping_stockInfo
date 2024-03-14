목적 : 제테크에 관심이 많아 원하는 자료를 스크래핑하고 싶었고, 전적으로 GPT-4의 도움으로 개발하였다
필요에 의한 개발이었지만, 지금은 사용하지 않는다,,,ㅎ

사용 기술 : GPT-4, 파이썬, beautifulsoup, CRA(-이제는 죽은-)

도전과 응전 :

- Selenium 인가, BeautifulSoup인가
  내게 적절한 기술은 beautifulsoup이었다. selenium은 절차적으로 실제로 동작 하기 때문에 더 정교한 작업에 적합하다. 대신 처리 시간이 길다. 처리 과정에 동작이 들어가기 때문이다.

- 헤더
  스크래핑이란게 요청이 많기 때문에, 요청 받는 곳에서 기본 요청은 막아놨다.
  헤더에 특정 값을 넣으면 깔끔하게 해결된다. 속도와도 관련이 있다는데, 지금은 기억나지 않는다.

- 파이썬 처리와 리액트
  api를 뚫을 것인가 excel을 저장하는 것이 아니라 json파일을 만들어 프로젝트 폴더 내부에 저장시켜
  localhost에서 참조하게 만들었다.
  어디서 많은 데이터를 가공할 것인가. 답은 브라우저와 나눴다.

- 최종병기 병렬처리
  사이트의 도움과 GPT의 도움으로 해결하였다.

- 댓글은 포기
  댓글은 페이지 파싱 후에 모듈을 불러오기 때문에 selenium을 써야했다.
  결국에는 가능하겠지만, 필요도가 낮아 패스!

종합적인 결론은 - GPT-4 짱이다. 언어야 비슷하겠지만, 파이썬에 대해 전혀 몰라도 단기간에 프로그램 작성이 가능했다. 이제는 gpt가 능률인 것 같다. 이게 더 다듬어진다면 훌륭한 감독자가 되어야할 것 같은데,,,

1. 참조사이트
   https://tglv.tistory.com/50 network url 보는 방법
   https://tglv.tistory.com/53 정규식
   https://moons-rainbow.tistory.com/30 모듈화
   https://tibetsandfox.tistory.com/20 파이썬 '\_'의 의미
   https://tglv.tistory.com/50
   병렬처리
   https://ecofriendlyapplesu.tistory.com/10
   https://twoicefish-secu.tistory.com/375
   https://bjwan-career.tistory.com/129
