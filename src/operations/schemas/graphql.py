import graphene
from django.db.models import Sum, Q
from django.db.models.functions import Coalesce
from operations.models import User, Operation

from .operation import CreateOperation, OperationType
from .user import CreateUser, UpdateUser, UserType


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    create_operation = CreateOperation.Field()


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user_by_id = graphene.Field(UserType, user_id=graphene.Int())
    user_by_email = graphene.Field(UserType, user_email=graphene.String())
    balance_by_user_id = graphene.Int(user_id=graphene.Int())
    operations = graphene.List(OperationType)

    def resolve_users(root, info, **kwargs):
        return User.objects.all()

    def resolve_user_by_id(root, info, user_id):
        return User.objects.get(id=user_id)

    def resolve_user_by_email(root, info, user_email):
        return User.objects.get(email=user_email)

    def resolve_balance_by_user_id(root, info, user_id):
        total_sum = Operation.objects.filter(
            user_id=user_id,
        ).aggregate(
            sum=Coalesce(
                Sum(
                    'amount',
                    filter=Q(type_operation=Operation.DEPOSIT)
                ), 0,
            ) - Coalesce(
                Sum(
                    'amount', filter=Q(type_operation=Operation.WITHDRAW)
                ), 0,
            ))
        return total_sum['sum']

    def resolve_operations(root, info, **kwargs):
        return Operation.objects.all()


schema = graphene.Schema(query=Query, mutation=Mutation)
