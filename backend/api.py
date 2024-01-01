from ninja import NinjaAPI

api = NinjaAPI()

api.add_router('', 'backend.expense.api.router')
