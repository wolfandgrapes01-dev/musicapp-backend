from fastapi import Depends, HTTPException
from models.user import User
from schemas.auth.requests.login_req import LoginReq
from schemas.auth.requests.signup_req import SignUpReq
from schemas.auth.responses.auth_res import AuthRes
from middleware.auth_middleware import auth_middleware
from fastapi import APIRouter
from database import get_db
from sqlalchemy.orm import Session

from services.auth_service import login_user_service, signup_user_service

router = APIRouter()

@router.post('/signup', status_code=201, response_model=AuthRes)
def signup_user(request: SignUpReq, db: Session = Depends(get_db)):
    """
    Register a new user using the provided signup information. This includes:
    - Validating if the phone number is already registered.
    - Hashing the user's password.
    - Storing user data in the database.
    - Returning a JWT access token along with public user information.
    
    Args:
        signup_info (SignupReq): Data object containing new user's registration details.
        db (Session): SQLAlchemy session object for interacting with the database.

    Raises:
        HTTPException:
            - 409 if a user with the same phone number already exists (ERR_001).

    Returns:
        AuthRes: Object containing the JWT access token and registered user info.
    """

    return signup_user_service(request, db)

    
@router.post('/login', status_code=200, response_model=AuthRes)
def login_user(request: LoginReq, db: Session = Depends(get_db)):    
    """
    Authenticate a user based on phone number and password, update last login time,
    and return an access token along with user information.

    Args:
        login_info (LoginReq): Object containing user's login credentials (phone number and password).
        db (Session): SQLAlchemy database session used for querying and updating the user record.

    Raises:
        HTTPException: 
            - 404 if user with the given phone number is not found (ERR_002).
            - 401 if the provided password does not match the stored password (ERR_003).

    Returns:
        AuthRes: Object containing the JWT access token and authenticated user info.
    """

    return login_user_service(request, db)

@router.get('/')
def current_user_data(db: Session=Depends(get_db), user_dict = Depends(auth_middleware)):
    rst_user_info = db.query(User).filter(User.id == user_dict['uid']).first()

    if not rst_user_info:
        # ERR_004
        raise HTTPException(status_code=404, detail='User not found!')
    
    return rst_user_info