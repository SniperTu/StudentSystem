from django.db import models

# Create your models here.
#课程表
class CourseModel(models.Model):
    cour_id = models.CharField(max_length=15, verbose_name="学生id")
    course = models.CharField(max_length=30, verbose_name="课程")
    grade = models.IntegerField(default=60, verbose_name="分数")
    class Meta():
        db_table = 'course'
    def __str__(self):
        return "学生id: 课程： 分数： ".format(self.cour_id, self.course, self.grade)
#学生信息表
class StudentInformationModel(models.Model):
    stu_id = models.CharField(max_length=15, verbose_name="学生id")
    stu_name = models.CharField(max_length=30, verbose_name="学生姓名")
    stu_phone = models.CharField(max_length=20, verbose_name="学生电话")
    stu_addr = models.TextField(verbose_name="学生住址")
    stu_faculty = models.CharField(max_length=20, verbose_name="院系")
    stu_major = models.CharField(max_length=30, verbose_name="专业")
    class Meta():
        db_table = 'studentinformation'

#学生用户名密码表
class StudentModel(models.Model):
    stu_id = models.CharField(max_length=15, verbose_name="学生id")
    username = models.CharField(max_length=10, verbose_name="用户名")
    password = models.CharField(max_length=10, verbose_name="密码")
    class Meta():
        db_table = 'student'

