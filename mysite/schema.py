import graphene
from graphene_django import DjangoObjectType
from graphene import relay, ObjectType
from student_management.models import Employee,Project
from graphene_django.rest_framework.mutation import SerializerMutation
from student_management.serializers.employeeSerializer import EmployeeSerializer
from django.contrib.auth.models import User
from datetime import datetime

from student_management.constants import CLOSED_PHASE

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
    all_employee = graphene.List(EmployeeList)
    employee    = graphene.Field(EmployeeList,id=graphene.Int())
    all_project = graphene.List(Projectlist)
    # category_by_name = graphene.Field(EmployeeList, firstName=graphene.String(required=True))
    # project=graphene.List(Projectlist)
    # category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_employee(root, info):
        employee=Employee.objects.select_related('project').filter(is_deleted=0).all()
        return employee
    def resolve_employee(root,info,**kwargs):
        employee_id =kwargs.get('id')
        if employee_id is not None:
            return Employee.objects.get(pk=employee_id)
        return None

    def resolve_all_project(root, info, id=None):
        return Project.objects.all()

class CreateEmployee(graphene.Mutation):
    class Arguments:
        firstName           = graphene.String(required=True)
        lastName            = graphene.String(required=True)
        dob                 = graphene.String(required=True)
        email               = graphene.String(required=True)
        empId               = graphene.String(required=True)
        mobileNo            = graphene.String(required=True)
        password            = graphene.String(required=True)
        #photo               = models.ImageField(upload_to='emp-photo',null=True,blank=True)
        #reportingEmployee   = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='employee_reporting')
        project             = graphene.String(Project)
        #user                = graphene.String()

    employee = graphene.Field(EmployeeList)

        # lookup_field = 'id'
    def mutate(root, info,**kwargs):
        password=kwargs.pop('password')
        kwargs['dob']=datetime.strptime(kwargs['dob'], '%Y-%m-%d')  
        user=User.objects.create_user(username=kwargs['email'],first_name=kwargs['firstName'],last_name=kwargs['lastName'],email=kwargs['email'],password=password)
        project=kwargs.pop('project')
        kwargs['project']=Project.objects.get(id=project)
        kwargs['user']=user
        print(kwargs)
        employee=Employee.objects.create(**kwargs)
        return CreateEmployee(employee=employee)
    # class Arguments:
        # name=graphene.String(required=True)
        # description=graphene.String(required=True)
class UpdateEmployee(graphene.Mutation):
    class Arguments:
        id                  = graphene.ID(required=True)
        firstName           = graphene.String(required=True)
        lastName            = graphene.String(required=True)
        dob                 = graphene.String(required=True)
        email               = graphene.String(required=True)
        empId               = graphene.String(required=True)
        mobileNo            = graphene.String(required=True)
        #password            = graphene.String(required=True)
        #photo               = models.ImageField(upload_to='emp-photo',null=True,blank=True)
        #reportingEmployee   = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='employee_reporting')
        project             = graphene.String(Project)
        #user                = graphene.String()

    employee = graphene.Field(EmployeeList)

    def mutate(root, info,**kwargs):
        kwargs['dob']=datetime.strptime(kwargs['dob'], '%Y-%m-%d')  
        employee_data=Employee.objects.get(id=kwargs['id'])
        user=User.objects.filter(id=employee_data.user.id).update(username=kwargs['email'],first_name=kwargs['firstName'],last_name=kwargs['lastName'],email=kwargs['email'])
        #print(user)
        project=kwargs.pop('project')
        kwargs['project']=Project.objects.get(id=project)
        employee_data.firstName=kwargs['firstName']
        employee_data.lastName=kwargs['lastName']
        employee_data.email=kwargs['email']
        employee_data.dob=kwargs['dob']
        employee_data.empId=kwargs['empId']
        employee_data.mobileNo=kwargs['mobileNo']
        employee_data.project=kwargs['project']
        employee_data.save()
        return UpdateEmployee(employee=employee_data)

class DeleteEmployee(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
    employee = graphene.Field(EmployeeList)
    def mutate(root,info,**kwargs):
        delete_id=kwargs['id']
        employee=Employee.objects.get(id=delete_id)
        employee.is_deleted=1
        employee.save()
        return employee

class CreateProject(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        estimatedDate = graphene.String()
        phase = graphene.String(required=True)
        description = graphene.String()
    project = graphene.Field(Projectlist)
    def mutate(self, info, name, estimatedDate, phase, description):
        if estimatedDate:
            estimatedDate = datetime.strptime(estimatedDate, "%Y-%m-%d")
        project = Project.objects.create(name=name, estimated_date=estimatedDate, 
        phase=phase, description=description)
        return CreateProject(project=project)

class UpdateProject(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        estimatedDate = graphene.String()
        phase = graphene.String(required=True)
        description = graphene.String()
        id = graphene.ID(required=True)
    project = graphene.Field(Projectlist)
    def mutate(self, info, name, id, estimatedDate, phase, description):
        if estimatedDate:
            estimatedDate = datetime.strptime(estimatedDate, "%Y-%m-%d")
        project = Project.objects.get(id=id)
        project.name = name
        project.estimated_date = estimatedDate
        project.phase = phase
        project.description = description
        if phase == CLOSED_PHASE:
            project.closed_date = datetime.now()
        else:
            project.closed_date = None
        project.save()
        return UpdateProject(project=project)



	# update_player = graphene.Field(EditPlayerMutation)
class Mutation(graphene.ObjectType):
    create_employee=CreateEmployee.Field()
    update_employee=UpdateEmployee.Field()
    delete_employee=DeleteEmployee.Field()
    # debug = graphene.Field(DjangoDebug, name="_debug")`
    create_project = CreateProject.Field()
    update_project = UpdateProject.Field()

    # print(create_employee.__dict__)
   
        # return CreateActor(ok=ok, actor=actor_instance)
    # def mutation()


schema = graphene.Schema(query=Query,mutation=Mutation)