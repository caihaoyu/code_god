from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    class Meta():
        index_together = [['title']]
        ordering = ('-edit_date',)

    title = models.CharField('标题', max_length=100, db_index=True, )
    author = models.ForeignKey(User)
    content = models.TextField('内容')
    trackback_url = models.CharField('引用地址', max_length=300)
    original_author = models.CharField('原作者', max_length=100, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    def get_answer_rest(self):
        answers = []
        for answer in self.answer_set.all():
            answers.append({"id": answer.id, "content": answer.content, "is_accept": answer.is_accept,
                            "original_author": answer.original_author})
        return answers

    def get_answer_count(self):
        return self.answer_set.count()

    def get_tag_rest(self):
        tags = [];
        for tag in self.tag_set.all():
            tags.append({"id": tag.id, "title": tag.title})
        return tags

    def get_tags_id_rest(self):
        tags = [];
        for tag in self.tag_set.all():
            tags.append(tag.id)
        return tags

    def __str__(self):
        return self.title


class Tag(models.Model):
    class Meta():
        index_together = [['title']]

    title = models.CharField(max_length=30, db_index=True, )
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.title


class Answer(models.Model):
    content = models.TextField('内容')
    is_accept = models.BooleanField('是否被采纳', default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    original_author = models.CharField('原作者', max_length=100, null=True, blank=True)
    author = models.ForeignKey(User)
    questions = models.ForeignKey(Question, verbose_name="问题")

    def __str__(self):
        return self.content


class KeyWord(models.Model):
    word = models.CharField('关键词', max_length=100)
    question = models.ForeignKey(Question, verbose_name="问题")

    def __str__(self):
        return self.word


class Evaluate(models.Model):
    ip = models.CharField(max_length=100, )
    approval = models.BooleanField('是否赞同', default=False)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.approval



