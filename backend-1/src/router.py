from fastapi import APIRouter
from .main import get_products, get_featured, search_products, purchase, get_user, send_message, get_messages

router = APIRouter()

router.add_api_route("/products", get_products, methods=["GET"])
router.add_api_route("/featured", get_featured, methods=["GET"])
router.add_api_route("/search", search_products, methods=["POST"])
router.add_api_route("/purchase", purchase, methods=["POST"])
router.add_api_route("/user", get_user, methods=["GET"])
router.add_api_route("/chat/send", send_message, methods=["POST"])
router.add_api_route("/chat/{user_id}", get_messages, methods=["GET"])