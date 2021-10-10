import graphene
from graphene_django import DjangoObjectType
from operations.models import Operation


class OperationType(DjangoObjectType):
    class Meta:
        model = Operation
        fields = (
            'id',
            'user',
            'total'
        )


class OperationInput(graphene.InputObjectType):
    user_id = graphene.Int()
    amount = graphene.Decimal()
    type_operation = graphene.String()


class CreateOperation(graphene.Mutation):
    class Arguments:
        input = OperationInput(required=True)

    operation = graphene.Field(OperationType)

    @classmethod
    def mutate(cls, root, info, input):
        operation = Operation()
        operation.user_id = input.user_id
        operation.amount = input.email
        operation.type_operation = input.type_operation
        operation.save()
        return CreateOperation(operation=operation)
