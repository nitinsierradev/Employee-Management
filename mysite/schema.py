import graphene
from graphene_django import DjangoObjectType
from graphene import relay, ObjectType
from student_management.models import Employee,Project
from graphene_django.rest_framework.mutation import SerializerMutation
from student_management.serializers.employeeSerializer import EmployeeSerializer
class EmployeeList(DjangoObjectType):
    class Meta:
        model = Employee
        fields = '__all__'
        # interfaces = (relay.Node, )

class Projectlist(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'
        # interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    # print("~~~~~~~~~~~~~~~~~~")
    all_employee = graphene.List(EmployeeList, id=graphene.Int(required=False))
    all_project = graphene.List(Projectlist)
    # category_by_name = graphene.Field(EmployeeList, firstName=graphene.String(required=True))
    # project=graphene.List(Projectlist)
    # category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_employee(root, info, id=None):
        id = id
        employee=Employee.objects.select_related('project').all()
        if id is not None:
            employee=employee.filter(id=id)
        return employee
    def resolve_all_project(root, info, id=None):
        return Project.objects.all()

class CreateEmployee(SerializerMutation):
    class Meta:
        serializer_class = EmployeeSerializer
        model_class=Employee
        model_operations = ['create', 'update','delete']
        # lookup_field = 'id'
    @classmethod
    def mutate(cls,root, info,**kwargs):
        serializer=EmployeeSerializer(data=kwargs['input'])
       
        print(kwargs['input'])
        # print(serializer.errors)
        if serializer.is_valid():
            print("~~~~~~~~~~~~~~~")
            print(serializer.errors)
            print("!!!!!!!!!!!!!!!!!!!!")
            # print(serializer)
            obj=serializer.save()
            return obj
        pass
    # class Arguments:
        # name=graphene.String(required=True)
        # description=graphene.String(required=True)
    


	# update_player = graphene.Field(EditPlayerMutation)
class Mutation(graphene.ObjectType):
    create_employee=CreateEmployee.Field()
    # debug = graphene.Field(DjangoDebug, name="_debug")

    # print(create_employee.__dict__)
   
        # return CreateActor(ok=ok, actor=actor_instance)
    # def mutation()

schema = graphene.Schema(query=Query,mutation=Mutation)