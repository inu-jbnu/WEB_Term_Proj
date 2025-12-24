# app/db/seed.py
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.models.test import Test
from app.db.models.question import Question
from app.db.models.question_choice import QuestionChoice
from app.db.models.result_type import ResultType

def seed_data():
    db: Session = SessionLocal()

    # 1️⃣ 결과 유형
    result_types = [
        ResultType(result_type="A", name="조용한 관찰자",
                   description="혼자 있는 시간을 통해 에너지를 얻음\n신중하고 깊이 생각하는 성향\n감정 표현은 적지만 공감 능력 높음",
                   summary="말보다 행동과 생각이 앞서는 사람"),
        ResultType(result_type="B", name="에너지 메이커",
                   description="사람들과 함께할 때 진가를 발휘\n긍정적이고 표현력이 풍부\n주변을 밝게 만드는 힘이 있음",
                   summary="당신이 있는 곳엔 웃음이 있습니다"),
        ResultType(result_type="C", name="논리적 분석가",
                   description="이성적 판단을 중시\n문제 해결과 전략에 강함\n객관적인 시선으로 신뢰받음",
                   summary="감정보다 구조를 먼저 보는 사람"),
        ResultType(result_type="D", name="균형 잡힌 조율자",
                   description="상황 파악과 중재 능력이 뛰어남\n책임감 있고 현실적\n조직에서 꼭 필요한 존재",
                   summary="모두가 의지하게 되는 중심축"),
    ]
    db.add_all(result_types)
    db.commit()

    # 2️⃣ 테스트 생성
    test = Test(title="성격 유형 테스트", description="12문항으로 보는 성격 테스트")
    db.add(test)
    db.commit()
    db.refresh(test)

    # 3️⃣ 질문과 선택지
    questions = [
        ("약속이 갑자기 취소됐다. 이때 당신의 반응은?",
         [("A", "오히려 좋다. 집에서 혼자 쉬어야지", "A"),
          ("B", "아쉽지만 다른 약속을 찾아본다", "B"),
          ("C", "이유부터 꼼꼼히 따져본다", "C"),
          ("D", "괜히 내가 뭔가 잘못했나 고민한다", "D")]),

        ("새로운 일을 시작할 때 나는?",
         [("A", "일단 해보고 생각한다", "A"),
          ("B", "계획을 세운 뒤 움직인다", "B"),
          ("C", "정보부터 최대한 모은다", "C"),
          ("D", "주변 사람 의견을 많이 참고한다", "D")]),

        ("스트레스를 받을 때 주로 하는 행동은?",
         [("A", "혼자만의 시간이 필요하다", "A"),
          ("B", "친구에게 바로 연락한다", "B"),
          ("C", "운동이나 산책을 한다", "C"),
          ("D", "아무것도 안 하고 멍 때린다", "D")]),

        ("단체 활동에서 나는 보통?",
         [("A", "리더 역할을 맡는 편이다", "A"),
          ("B", "분위기 메이커다", "B"),
          ("C", "묵묵히 맡은 일을 한다", "C"),
          ("D", "상황에 따라 유연하게 움직인다", "D")]),

        ("문제가 생겼을 때 더 중요한 것은?",
         [("A", "빠른 해결", "A"),
          ("B", "모두의 감정", "B"),
          ("C", "논리적 타당성", "C"),
          ("D", "책임 소재", "D")]),

        ("쉬는 날 가장 끌리는 것은?",
         [("A", "집에서 넷플릭스 정주행", "A"),
          ("B", "사람 만나는 약속", "B"),
          ("C", "새로운 곳 탐험", "C"),
          ("D", "밀린 할 일 정리", "D")]),

        ("누군가 고민을 털어놓을 때 나는?",
         [("A", "조용히 들어주는 편이다", "A"),
          ("B", "공감하며 함께 화내준다", "B"),
          ("C", "해결책을 제시해준다", "C"),
          ("D", "상황을 객관적으로 정리해준다", "D")]),

        ("갑작스러운 변화가 생기면?",
         [("A", "생각보다 잘 적응한다", "A"),
          ("B", "흥미롭고 재미있다", "B"),
          ("C", "불안해서 계획을 다시 세운다", "C"),
          ("D", "필요하면 주변 도움을 구한다", "D")]),

        ("팀 프로젝트에서 가장 싫은 상황은?",
         [("A", "방향 없이 질질 끄는 것", "A"),
          ("B", "분위기가 냉랭한 것", "B"),
          ("C", "비효율적인 진행", "C"),
          ("D", "책임 떠넘기기", "D")]),

        ("누군가 나를 평가한다면 가장 많이 들을 말은?",
         [("A", "차분하다", "A"),
          ("B", "활발하다", "B"),
          ("C", "똑똑하다", "C"),
          ("D", "믿음직하다", "D")]),

        ("중요한 결정을 할 때 나는?",
         [("A", "내 직감을 믿는다", "A"),
          ("B", "주변 반응을 본다", "B"),
          ("C", "장단점을 정리한다", "C"),
          ("D", "현실적인 조건을 따진다", "D")]),

        ("인간관계에서 내가 가장 중요하게 생각하는 것은?",
         [("A", "편안함", "A"),
          ("B", "즐거움", "B"),
          ("C", "신뢰", "C"),
          ("D", "책임감", "D")]),
    ]

    for idx, (q_text, choices) in enumerate(questions, start=1):
        q = Question(test_id=test.test_id, content=q_text, order_no=idx)
        db.add(q)
        db.commit()
        db.refresh(q)

        db_choices = [QuestionChoice(question_id=q.question_id, label=label, content=content, result_type=result)
                      for label, content, result in choices]
        db.add_all(db_choices)
        db.commit()

    db.close()
    print("✅ Seed data inserted successfully!")

if __name__ == "__main__":
    seed_data()
