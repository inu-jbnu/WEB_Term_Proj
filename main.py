from fastapi import FastAPI
from app.routers import auth, user, questions, test, question_choice, answer, result_type, test_result  # test 포함
from fastapi.responses import JSONResponse
from app.core.exception import AppException
from fastapi import Request


app = FastAPI(title="My Web API")

from app.db.base import Base
from app.db.session import engine
Base.metadata.create_all(bind=engine)

# 라우터 등록
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(test.router)
app.include_router(questions.router)
app.include_router(question_choice.router)
app.include_router(answer.router)
app.include_router(result_type.router)
app.include_router(test_result.router)

# 헬스체크 예시
@app.get("/health")
def health_check():
    return {
        "status": "ok",
    }

def register_exception_handlers(app: FastAPI):
    @app.exception_handler(AppException)
    async def app_exception_handler(request: Request, exc: AppException):
        return JSONResponse(
            status_code=exc.status,
            content={
                "timestamp": exc.timestamp,
                "path": request.url.path,
                "status": exc.status,
                "code": exc.code,
                "message": exc.message,
                "details": exc.details,
            },
        )

