"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Process
from app.models import User
from seed.schema.types import Process as ProcessType

class SaveProcessMutation(graphene.Mutation):
    
    process = graphene.Field(ProcessType)
    
    class Arguments:
        input = graphene.Int(required=True)
        result = graphene.String(required=True)
        user = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        user = info.context.user
        process = {}
        if "input" in kwargs: process["input"] = kwargs["input"]
        if "result" in kwargs: process["result"] = kwargs["result"]
        if "user" in kwargs:
            user = User.filter_permissions(
                User.objects, User.permission_filters(user))\
                .get(pk=kwargs["user"])
            process["user"] = user
        process = Process.objects.create(**process)
        process.save()
    
        return SaveProcessMutation(process=process)

class SetProcessMutation(graphene.Mutation):
    
    process = graphene.Field(ProcessType)
    
    class Arguments:
        id = graphene.Int(required=True)
        input = graphene.Int(required=False)
        result = graphene.String(required=False)
        user = graphene.Int(required=False)

    def mutate(self, info, **kwargs):
        user = info.context.user
        process = Process.filter_permissions(
            Process.objects, Process.permission_filters(user))\
            .get(pk=kwargs["id"])
        if "input" in kwargs: process.input = kwargs["input"]
        if "result" in kwargs: process.result = kwargs["result"]
        if "user" in kwargs:
            user = User.objects.get(pk=kwargs["user"])
            process.user = user
        process.save()
    
        return SetProcessMutation(process=process)

class DeleteProcessMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        process_id = kwargs["id"]
        process = Process.objects.get(pk=kwargs["id"])
        process.delete()
        return DeleteProcessMutation(id=process_id)