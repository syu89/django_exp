from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """
    django 要求模型必须继承 models.Model 类。
    Category 只需要一个简单的分类名 name 就可以了。
    CharField 指定了分类名 name 的数据类型，CharField 是字符型，
    CharField 的 max_length 参数指定了其最大长度，超过这个长度的分类名就不能被存入数据库。
    当然，django 还为我们提供了多种其他的数据类型，如日期类型 DateTimeField、整数类型 IntegerField 等等。
    django 内置的全部类型可查看文档：
    https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types
    """

    name = models.CharField(max_length=100)



class Tag(models.Model):
    """
    标签 Tag 也比较简单，和 Category 一样。
    再次强调一定要继承models.Model 类！
    """

    name = models.CharField(max_length=100)


class Post(models.Model):
    """
    文章数据库表稍微复杂一点，主要是涉及的字段更多。
    """

    # 文章标题
    title = models.CharField(max_length=70)

    # 文章正文，我们使用了TextFiled。
    # 存储比较短的字符串可以使用 CharField，但对于文章的正文来说可能会是一大段文本，因此使用 TextField 来存储打断文本
    body = models.TextField()

    # 这两个列表分别表示文章的时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 文章摘要，可以没有文章摘要，但默认情况下 Chardield 要求我们必须存储数据，否则就会报错。
    # 指定 Charfield 的blank=True 参数值后就可以允许为空了。
    excerpt = models.Charfield(max_length=200, blank=True)


    # 这是分类与标签，分类与标签的模型我们已经定义在上面。
    # 我们在这里把文章对应的数据库表和分类、标签对应的数据表关联了起来，但是关联形式稍微有点不同。
    # 我们规定一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，所以我们使用的是ForeignKey，即一
    # 对多的关联关系，且自 django 2.0 以后，ForeignKey 必须传入一个 on_delete 参数用来指定当关联的
    # 数据被删除时，被关联的数据的行为，我们这里嘉定当某个分类被删除时，该分类下全部文章也同事被删除，因此使用 models.CASCADE 参数，意为级联删除。
    # 使用 model 而对于标签来说，一片文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 ManyToManyField，表明这个时多对多的关联关系。
    # 同时我们规定文章可以没有标签，因此标签 tags 指定了 blank=True。
    # 如果你对 foreignKey、ManyToManyField 不了解，请看教程中的解释，亦可以参考官方文档: https://docs.djangoproject.com/en/2.2/topics/db/models/#relationships
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 django 内置的应用，专门用于处理网站用户的注册、登陆等流程，User 是
    # django 为我们已经写好的用户模型。
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # 因为我们规定一篇文章只能有一个作者， 而一个作者可能会写多篇文章，因此这是一对多的关联关系， 和Category 类似
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    






