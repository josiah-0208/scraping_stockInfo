번뜩이는 아이디어를 기반으로, 실사용을 위한 스크래핑 프로그램을 짰습니다.
GPT는 짱
https://tglv.tistory.com/50

0. 서론 - 어떤 기술인지, 이유, 사용 기술, 

2. selenium vs beautifulsoup

3. 헤더에 user agent - 속도와도 관련이 있다.

4. api를 뚫을 것인가, cra를 사용한 이유 결국 excel이 아닌 localhost로 접근하기로 했다.

5. 결국 selenium을 써야한다. 네트워크

6. 시간이 너무 많이 걸린다. - 코스피, 코스닥으로 나눠서 데스크탑 2개로 돌릴지, 병렬처리를 할지

7. 참조사이트

요청 헤더에 user agent 속성이 들어가야 한다.
셀레니움보다 requests가 속도적으로 빠르다.
셀레니움은 동작이 들어가기 때문이다.
https://tglv.tistory.com/50 network url 보는 방법
https://tglv.tistory.com/53 정규식
https://moons-rainbow.tistory.com/30 모듈화 
https://tibetsandfox.tistory.com/20 파이썬 '\_'의 의미

파이썬 요청 시간 보고,
댓글 안나오는 이유 보고,
리액트 앱에서 json 목업 데이터 참조해서

가공하고 쏠까, 쏘면서 필터로 가공할까 연산량은 후자가 더 많지만, 로직이 화면으로 간다.
가공 요소
제목과 && 본문이 3글자 미만이면 없애고, 루프 빠져나오고
댓글도 3글자 미만이면 루프 빠져나오고
or
해당 문자열이 제목, 본문, 댓글에 포함되어 있으면 전체 가져오기?

useEffect 안에서 화면 룰에 맞게 쏴주는데 필터링 배열에 포함되는지 확인
let originalArray = ["apple", "banana", "cherry", "date", "elderberry"];
let filterArray = ["banana", "date"];

let filteredArray = originalArray.filter(item => filterArray.includes(item));

console.log(filteredArray); // Output: ["banana", "date"]

그다음에 얻어진 객체를 jsx 안에서 for in과 map 반복문을 돌리자
서버를 킨 상태에서 localhost로 접근

전역 스타일 적용하고,
BG#262626, P#AA540, T#F7F7F7
P#F19 E54
글꼴은 종목명 25 제목 본문 21 댓글 18 좋아요 싫어요 16
70퍼센트 중앙정렬
라인헤이트 140 ~ 160
바디 100 100 플렉스 중앙정렬
컨테이너 너비 75퍼

종목명
제목 본문 좋아요 싫어요
댓글
댓글

최종적으로 파이썬 모듈화 코드정리 진행

댓글은 모듈을 불러오기 때문에 selenium을 써야한다.
https://ecofriendlyapplesu.tistory.com/10
https://twoicefish-secu.tistory.com/375
https://bjwan-career.tistory.com/129
병렬처리 
