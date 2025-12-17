from fastapi import FastAPI
from database import Base, engine

# Routers
from router.food_router import router as food_router
from router.user_router import router as user_router
from router.order_router import router as order_router
from router.vendor_router import router as vendor_router
from router.order_items_router import router as order_items_router
from router.payment_router import router as payment_router
from router.cart_router import router as cart_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="LocalEats Food API")

# Register Routers with Tags
app.include_router(food_router, tags=["Foods"])
app.include_router(user_router, tags=["Users"])
app.include_router(order_router, tags=["Orders"])
app.include_router(vendor_router, tags=["Vendors"])
app.include_router(order_items_router, tags=["Order Items"])
app.include_router(payment_router,tags=["Payments"])
app.include_router(cart_router,tags=["Cart"])

