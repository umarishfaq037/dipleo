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
    model = Education
    fields = '__all__'


class ScholarshipSerializer(serializers.ModelSerializer):
    model = Scholarship
    fields = '__all__'


class ReferenceSerializer(serializers.ModelSerializer):
    model = Reference
    fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    model = Skill
    fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    model = Language
    fields = '__all__'

class ProgrammingSerializer(serializers.ModelSerializer):
    model = Programming
    fields = '__all__'


class DesignSerializer(serializers.ModelSerializer):
    model = Design
    fields = '__all__'


class DataSerializer(serializers.ModelSerializer):
    model = Data
    fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    education = EducationSerializer(read_only=True)
    scholarship = ScholarshipSerializer(read_only=True)
    reference = ReferenceSerializer(read_only=True)
    skill = SkillSerializer(read_only=True)
    language = LanguageSerializer(read_only=True)
    programming = ProgrammingSerializer(read_only=True)
    design = DesignSerializer(read_only=True)
    data = DataSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


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