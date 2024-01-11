import { useEffect, useState } from 'react';
import './App.css';
import resultJson from './result.json';

// 키 배열 먼저 추출, 오브젝트에 키 배열 돌려서, 빈 배열 빼고,
function App() {
  const [resultObj, setResultObj] = useState({});
  const [keyArr, setKeyArr] = useState([]);
  useEffect(() => {
    const parsedJson = JSON.parse(JSON.stringify(resultJson));
    const newJson = {};
    Object.keys(parsedJson).map((key) => {
      if (parsedJson[key].length > 0) {
        newJson[key] = [];
        parsedJson[key].map((commentObj) => {
          if (
            filterKeywords.some((keyword) =>
              commentObj?.글제목.includes(keyword)
            ) ||
            filterKeywords.some((keyword) =>
              commentObj?.글내용.includes(keyword)
            )
          ) {
            newJson[key].push(commentObj);
          }
        });
        if (newJson[key].length === 0) {
          delete newJson[key];
        }
      }
    });
    console.log(newJson);
    setResultObj(newJson);
    setKeyArr(Object.keys(newJson));
  }, []);
  return (
    <div className="container">
      {keyArr.map((key) => (
        <div className="container_stock">
          <div className="title">{key}</div>
          <div className="container_comments">
            {resultObj[key].map((comment) => (
              <div className="container_comment">
                <div className="top_comment">
                  <span className="text title_comment">
                    <b>{comment?.글제목}</b>
                  </span>
                  <span className="text like">{comment?.공감}</span>
                  <span className="text dislike">{comment?.비공감}</span>
                </div>
                <span className="text content">{comment?.글내용}</span>
              </div>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}

export default App;

const filterKeywords = [
  '헬로우',
  '구글',
  '애플',
  '테슬라',
  '유튜브',
  '마이크로소프트',
  '아마존',
  '인수',
  '호재',
  '예상',
  '단독',
  '페이스북',
  '유치',
  '전환',
  '버크셔',
  '월마트',
  '디즈니',
  '모건',
  '모간',
  '비자',
  '인텔',
  '엔비디아',
  '페이팔',
  '넷플릭스',
  '펩시',
  '코카콜라',
  '어도비',
  '실적',
  '개선',
  '매출',
  '상장',
  '판로',
  '개발',
  '성공',
  '협약',
  '신기록',
  '수출',
  '이익',
  '증가',
  '영업이익',
  '전년',
  '전월',
  '대비',
  '육박',
  '내부',
  '내부자',
  '영업익',
  '흑자',
  '무역수지',
  '활황',
  '인기',
  '대박',
  '턴어라운드',
  '기록',
  '성장',
  '달성',
  '독점',
  '발견',
  '발굴',
  '입수',
  '좋은',
  '소식',
  '상용화',
  '임박',
  '제휴',
  '최초',
  '모멘텀',
  '암드',
  '최고',
  '계약',
  '평가',
  '지표',
  '1등',
  '1위',
  '공개',
  '우수',
  '최우수',
  '대상',
  '상회',
  '예측',
  '인상',
  '기대',
  '증대',
  '창출',
  '효과',
  '컨센서스',
  '가이던스',
  '유상증자',
  '유증',
  '신작',
  '출시',
  '기대감',
  '공유',
  'msci',
  '순이익',
  '당기',
  '공급',
  '낙폭',
  '저점',
  '최저',
  '기회',
  '분석',
  '총선',
  '대선',
  '정부',
  '이슈',
  '전망',
  '반응',
  '핵심',
  '소재',
  '승인',
  '엠바고',
  '찌라시',
  '체결',
  '자사주',
  '소각',
  '가능',
  '결정',
];
