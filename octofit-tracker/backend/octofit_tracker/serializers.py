from rest_framework import serializers
from bson import ObjectId
from .models import User, Team, Activity, Leaderboard, Workout

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value) if isinstance(value, ObjectId) else value

    def to_internal_value(self, data):
        return ObjectId(data) if ObjectId.is_valid(data) else data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['_id', 'email', 'name', 'age', 'created_at']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['_id', 'name', 'members']

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['_id', 'user', 'type', 'duration', 'date']

class LeaderboardSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Use the UserSerializer to serialize the user field

    class Meta:
        model = Leaderboard
        fields = ['_id', 'user', 'score']

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['_id', 'name', 'description', 'duration']