import random
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# 본인의 모델 파일에서 Base와 Table 클래스들을 import 하세요
# 예: from app.database import Base, engine
#    from app.models import User, Post, Comment, Category

# 1. DB 연결 설정 (본인의 .env 또는 config 활용)
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://user:password@localhost/dbname"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

def run_seed():
    print("데이터 생성을 시작합니다...")

    # 2. 사용자(User) 데이터 10명 생성
    users = []
    for i in range(1, 11):
        user = User(
            email=f"user{i}@example.com",
            password="hashed_password", # 실제로는 bcrypt 등으로 해싱 필요
            nickname=f"유저{i}",
            role="ROLE_USER" if i > 1 else "ROLE_ADMIN" # 1번만 관리자
        )
        db.add(user)
        users.append(user)
    db.commit()

    # 3. 카테고리(Category) 데이터 5개 생성
    categories = []
    category_names = ["공지사항", "자유게시판", "Q&A", "정보공유", "맛집"]
    for name in category_names:
        cat = Category(name=name)
        db.add(cat)
        categories.append(cat)
    db.commit()

    # 4. 게시글(Post) 데이터 200개 생성 (필수 요건 충족)
    for i in range(1, 201):
        post = Post(
            title=f"테스트 게시글 제목 {i}",
            content=f"이것은 {i}번째 테스트 게시글 내용입니다.",
            user_id=random.choice(users).id,
            category_id=random.choice(categories).id,
            created_at=datetime.now()
        )
        db.add(post)
    
    db.commit()
    print(f"성공적으로 200개의 게시글과 데이터를 생성했습니다.")

if __name__ == "__main__":
    run_seed()