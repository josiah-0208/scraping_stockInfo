목적 : 제테크에 관심이 많던 중 좋은 보조지표에 대한 아이디어가 떠올랐고, 이를 GPT-4의 도움을 얻어 싶었다.
즉 필요에 의한 개발이었지만, 지금은 사용하지 않는다,,,ㅎ

사용 기술 : GPT-4, 파이썬, beautifulsoup, CRA(-이제는 죽은-)

도전과 응전 :

- Selenium 인가, BeautifulSoup인가
  beautifulsoup이다. selenium은 실제로 동작을 하는 더 정교한 작업에 적합한 대신 처리 시간이 길다.
  셀레니움은 처리 과정에 실제 동작이 들어가기 때문이다.

- 헤더
  스크래핑이란게 요청이 많고, 처리해주는 입장에서 막아놨다.
  헤더에 특정 깔끔하게 처리된다. 교육목적이 아니라면, 지양하는게,,
  속도와도 관련이 있다는데, 지금은 기억나지 않는다.

- 파이썬 처리와 리액트
  api를 뚫을 것인가 excel을 저장하는 것이 아니라 json파일을 만들어 프로젝트 폴더 내부에 저장시켜
  localhost에서 참조하게 만들었다.
  어디서 많은 데이터를 가공할 것인가. 답은 브라우저와 나눴다.

- 최종병기 병렬처리

언어라는게 결국, 비슷하기 때문에 파이썬을 익히지 않고서도 파이썬을 이용하여

- 댓글은 포기
  댓글은 페이지 파싱 후에 모듈을 불러오기 때문에 selenium을 써야했다.
  분명 결국에는 가능했겠지만, 필요도에 따라 조절하였다.

결론은 - GPT-4 짱
이제는 gpt가 능률인 것 같다. 이게 더 다듬어진다면 훌륭한 감독자가 되어야할 것 같은데,

1. 참조사이트
   https://tglv.tistory.com/50 network url 보는 방법
   https://tglv.tistory.com/53 정규식
   https://moons-rainbow.tistory.com/30 모듈화
   https://tibetsandfox.tistory.com/20 파이썬 '\_'의 의미
   https://tglv.tistory.com/50

가공하고 쏠까, 쏘면서 필터로 가공할까 연산량은 후자가 더 많지만, 로직이 화면으로 간다.
가공 요소
제목과 && 본문이 3글자 미만이면 없애고, 루프 빠져나오고
댓글도 3글자 미만이면 루프 빠져나오고
or
해당 문자열이 제목, 본문, 댓글에 포함되어 있으면 전체 가져오기?

https://ecofriendlyapplesu.tistory.com/10
https://twoicefish-secu.tistory.com/375
https://bjwan-career.tistory.com/129
병렬처리


