from rest_framework import serializers
from .models import *
from company.models import *
from company.serializers import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'

class CandidateIntroSerializer(serializers.ModelSerializer):

    class Meta:
        model = CandidateIntro
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Education
        fields = '__all__'


class ScholarshipSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Scholarship
        fields = '__all__'


class ReferenceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reference
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Skill
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Language
        fields = '__all__'

class ProgrammingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Programming
        fields = '__all__'


class DesignSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Design
        fields = '__all__'

class EmploymentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employement
        fields = '__all__'


class DataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Data
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    #education_set = EducationSerializer(many=True, read_only=True)
    #scholarship = ScholarshipSerializer(read_only=True)
    #reference = ReferenceSerializer(read_only=True)
    #skill_a = SkillSerializer(many=True, read_only=True)
    #language = LanguageSerializer(read_only=True)
    #programming = ProgrammingSerializer(read_only=True)
    #design = DesignSerializer(read_only=True)
    #data = DataSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'
        #read_only_fields = ('user', 'name', 'education' )
        #fields = '__all__'


class SaveJobsSerializer(serializers.ModelSerializer):
    job = JobSerializer(read_only=True)
    class Meta:
        model = SavedJob
        fields = '__all__'


class ApplyJobsSerializer(serializers.ModelSerializer):
    job = JobSerializer(read_only=True)
    company = CompanySerializer()
    user = UserProfileSerializer()
    class Meta:
        model = ApplyJob
        fields = '__all__'


class SavedApplyJobSerializer(serializers.ModelSerializer):
    job = JobSerializer(read_only=True)
    # user = UserSerializer(read_only=True)
    class Meta:
        model = SavedApplyJob
        fields = '__all__'


class CandidateApplyJobsSerializer(serializers.ModelSerializer):
    candiate = UserProfileSerializer(read_only=True)
    class Meta:
        model = ApplyJob
        fields = '__all__'

class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = '__all__'

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = '__all__'