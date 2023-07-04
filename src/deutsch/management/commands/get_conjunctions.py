import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand, CommandError
from django.core.management.color import no_style
from django.db import connection

from ...models import ListCategory, Word, WordList


class Command(BaseCommand):
    help = 'Grab german adverbs from deutsch-sprechen.ru'
    urls = {
        # 2: 'https://online-teacher.ru/blog/%D1%81%D0%BE%D1%87%D0%B8%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D0%BD%D0%B5%D0%BC%D0%B5%D1%86%D0%BA%D0%B8%D0%B5-%D1%81%D0%BE%D1%8E%D0%B7%D1%8B',
        # 3: 'https://online-teacher.ru/blog/%D0%BF%D0%BE%D0%B4%D1%87%D0%B8%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D1%81%D0%BE%D1%8E%D0%B7%D1%8B-%D0%B2-%D0%BD%D0%B5%D0%BC%D0%B5%D1%86%D0%BA%D0%BE%D0%BC-%D1%8F%D0%B7%D1%8B%D0%BA',
        # 4: 'https://online-teacher.ru/blog/%D0%BF%D0%B0%D1%80%D0%BD%D1%8B%D0%B5-%D1%81%D0%BE%D1%8E%D0%B7%D1%8B-%D0%B4%D0%B2%D0%BE%D0%B9%D0%BD%D1%8B%D0%B5-%D1%81%D0%BE%D1%8E%D0%B7%D1%8B-%D0%B2-%D0%BD%D0%B5%D0%BC%D0%B5%D1%86%D0%BA%D0%BE%D0%BC',
    }

    def handle(self, *args, **options):
        for word_list_id in self.urls:
            self.clean_table(word_list_id)

            page = requests.get(self.urls[word_list_id])
            soup = BeautifulSoup(page.content, 'html.parser')

            title = soup.title.string
            self.stdout.write(self.style.WARNING(f'Title: {title}'))

            list_category = None
            list_category_name = None
            list_category_order = 0

            div_entry = soup.find('div', class_='entry')
            table = div_entry.find('table')

            for tr in table.find_all('tr'):
                first_td = tr.find('td')
                if 'colspan' in first_td.attrs:
                    colspan = int(first_td.attrs['colspan'])
                    if colspan == 3:
                        list_category_name = first_td.text.strip()
                        list_category = ListCategory.objects.create(
                            title=list_category_name,
                            order=list_category_order,
                            word_list_id=word_list_id
                        )
                        list_category_order += 1
                        self.stdout.write(list_category_name)
                elif list_category:
                    tds = tr.find_all('td')
                    translated_word = tds[0].text.strip().replace('«', '').replace('»', '')
                    original_word = tds[1].text.strip().replace('«', '').replace('»', '')
                    word = Word.objects.create(
                        word=original_word,
                        translated_word=translated_word,
                        list_category_id=list_category.id)
                    self.stdout.write('{} {}'.format(original_word, translated_word))
                else:
                    tds = tr.find_all('td')
                    translated_word = tds[0].text.strip().replace('«', '').replace('»', '')
                    original_word = tds[1].text.strip().replace('«', '').replace('»', '')
                    word = Word.objects.create(
                        word=original_word,
                        translated_word=translated_word,
                        word_list_id=word_list_id)
                    self.stdout.write('{} {}'.format(original_word, translated_word))

        self.stdout.write(self.style.SUCCESS('Done'))

    def clean_table(self, word_list_id: int):
        """Run django-admin sqlsequencereset app_label --database DATABASE to reset all tables"""
        Word.objects.filter(list_category__word_list_id=word_list_id).delete()
        ListCategory.objects.filter(word_list_id=word_list_id).delete()
        sequence_sql = connection.ops.sequence_reset_sql(no_style(), [WordList, ListCategory, Word])
        with connection.cursor() as cursor:
            for sql in sequence_sql:
                cursor.execute(sql)

        self.stdout.write(self.style.WARNING('ListCategory and Word have been cleaned'))
