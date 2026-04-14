from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.core.dependencies.dependencies import get_db
from app.modules.Users.schema import schema
from app.modules.Users.services.user_service import UserService
from app.core.middleware.security_layer import limiter
from fastapi import Request

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register", response_model=schema.RegisterResponse)
@limiter.limit("5/minute")  # Prevent spam registration
async def register(
    request: Request,
    user_data: schema.UserCreate,
    db: Session = Depends(get_db)
):
    
    if user_data.password is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Password is required")
    
    result = UserService.register_user(
        db=db,
        email=user_data.email,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        password=user_data.password # type: ignore
    )
    
    return schema.RegisterResponse(
        access_token=result["access_token"],
        token_type="bearer",
        user_id=result["user"].id,
        email=result["user"].email,
        first_name=result["user"].first_name,
        last_name=result["user"].last_name,
        message="User registered successfully"
    )