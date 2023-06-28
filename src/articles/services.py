from .models import Category, Article


def get_main_categories():
    return Category.objects.get_main_categories()


def get_category_by_id(id: int):
    return Category.objects.get(pk=id)


def get_category_breadcrumbs(category: Category):
    categories = []
    parent = category.parent_category
    while parent:
        categories.append(parent)
        parent = parent.parent_category
    return categories[::-1]


def get_first_article_in_category(category_id: int):
    return Article.objects.filter(category_id=category_id).first()


def get_first_sub_category(category_id: int):
    return Category.objects.filter(parent_category_id=category_id).first()


def get_article_by_slug(slug: str):
    return Article.objects.get(slug=slug)


def get_article_breadcrumbs(article: Article):
    categories = []
    parent = article.category
    while parent:
        categories.append(parent)
        parent = parent.parent_category
    return categories[::-1]
