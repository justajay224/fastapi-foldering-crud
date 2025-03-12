from .product_route import router as router_orm
from .product_non_orm_route import router as router_non_orm

__all__ = ["all_routers"]


all_routers = [
    router_orm,
    router_non_orm
]

def include_routers(app):
    for router in all_routers:
        app.include_router(router)