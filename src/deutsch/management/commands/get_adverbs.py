import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand, CommandError
from django.core.management.color import no_style
from django.db import connection

from ...models import ListCategory, Word


class Command(BaseCommand):
    help = 'Grab german adverbs from deutsch-sprechen.ru'
    url = 'https://deutsch-sprechen.ru' \
          + '/%D0%BD%D0%B5%D0%BC%D0%B5%D1%86%D0%BA%D0%B8%D0%B5-%D0%BD%D0%B0%D1%80%D0%B5%D1%87%D0%B8%D1%8F'
    word_list_id = 1

    def handle(self, *args, **options):
        self.clean_table()

        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')

        title = soup.title.string
        self.stdout.write(f'Title: {title}')

        list_category = None
        list_category_name = None
        list_category_order = 0

        div_entry = soup.find('div', class_='entry-content')

        for child in div_entry.children:
            if child.find('span'):
                child_string = str(child.find('span').string)
            else:
                child_string = str(child.string)

            if len(child_string) > 170:
                continue

            if 'Наречия с указанием на' in child_string or 'Наречия для' in child_string:
                list_category_name = child_string
                list_category = ListCategory.objects.create(title=list_category_name,
                                                            order=list_category_order,
                                                            word_list_id=self.word_list_id)
                list_category_order += 1
                self.stdout.write(f'Added list category {list_category_name}')
            elif child.name == 'table':
                for tr in child.find_all('tr'):
                    tds = tr.find_all('td')
                    for td in tds:
                        if td.string:
                            print(td.string)
                            word = td.string.replace('—', '@@@').replace('–', '@@@').replace('-', '@@@')
                            if '@@@' in word:
                                (original_word, translated_word) = word.split('@@@', 1)
                                Word.objects.create(word=original_word.strip(),
                                                    translated_word=translated_word.strip(),
                                                    list_category_id=list_category.id)

        self.stdout.write(self.style.SUCCESS('Done'))

    def clean_table(self):
        """Run django-admin sqlsequencereset app_label --database DATABASE to reset all tables"""
        Word.objects.all().delete()
        ListCategory.objects.all().delete()
        sequence_sql = connection.ops.sequence_reset_sql(no_style(), [ListCategory, Word])
        with connection.cursor() as cursor:
            for sql in sequence_sql:
                cursor.execute(sql)

        self.stdout.write(self.style.WARNING('ListCategory and Word have been cleaned'))
