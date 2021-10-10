import graphene
from graphene_django import DjangoObjectType
from operations.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email'
        )


class UserInput(graphene.InputObjectType):
    username = graphene.String()
    email = graphene.String()


class CreateUser(graphene.Mutation):
    class Arguments:
        input = UserInput(required=True)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, input):
        user = User()
        user.username = input.username
        user.email = input.email
        user.save()
        return CreateUser(user=user)


class UpdateUser(graphene.Mutation):
    class Arguments:
        input = UserInput(required=True)
        id = graphene.ID()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, input, id):
        user = User.objects.get(pk=id)
        user.username = input.username
        user.email = input.email
        user.save()
        return UpdateUser(user=user)
