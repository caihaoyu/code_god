from django.db import models

# Create your models here.

class Weekly(models.Model):
    issues = models.CharField("刊号", max_length=500)
    create_date = models.DateTimeField(auto_now_add=True)
    send_date = models.DateField()
    is_send = models.BooleanField(default=False)
    articles = models.ManyToManyField('Article', through='OrderShip')

    def get_articles_rest(self):
        articles = []
        for order_ship in OrderShip.objects.filter(weekly=self):
            article = order_ship.article
            articles.append({'id': article.id, 'title': article.title})
        return articles

    def __str__(self):
        return self.issues

    class Meta:
        ordering = ('-create_date',)


class Article(models.Model):
    title = models.CharField("标题", max_length=50)
    article_content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    weeklys = models.ManyToManyField(Weekly, through='OrderShip')
    order = models.IntegerField()

    def __str__(self):
        return str(self.id)


class OrderShip(models.Model):
    number = models.IntegerField("排序号")
    weekly = models.ForeignKey(Weekly,related_name="weekly")
    article = models.ForeignKey(Article,related_name="article")

    class Meta:
        ordering = ('number',)

