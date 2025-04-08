from djongo import models

class User(models.Model):
    _id = models.ObjectIdField()
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "users"

class Team(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User)

    class Meta:
        db_table = "teams"

class Activity(models.Model):
    _id = models.ObjectIdField()
    activity_id = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    duration = models.IntegerField()  # in minutes
    date = models.DateField()

    class Meta:
        db_table = "activity"

class Leaderboard(models.Model):
    _id = models.ObjectIdField()
    leaderboard_id = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

    class Meta:
        db_table = "leaderboard"

class Workout(models.Model):
    _id = models.ObjectIdField()
    workout_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()  # in minutes

    class Meta:
        db_table = "workouts"