from django.core.management import BaseCommand

from books.models import (Author, BookDetail, BookFeature, BookFinance,
                          BookGeneral, BookGenre, BookVolume, Library, BookContent)
from users.models import User
from users.utils import create_user


class Command(BaseCommand):
    help = "Add test books to the database"

    def handle(self, *args, **kwargs):
        # Delete Data from database
        Library.objects.all().delete()
        User.objects.all().delete()
        Author.objects.all().delete()
        BookVolume.objects.all().delete()
        BookGeneral.objects.all().delete()
        BookDetail.objects.all().delete()
        BookGenre.objects.all().delete()
        BookFeature.objects.all().delete()
        BookVolume.objects.all().delete()
        BookFinance.objects.all().delete()
        BookContent.objects.all().delete()

        create_user()  # Creating users in database

        user_1 = User.objects.get(email="user1@user.com")
        user_2 = User.objects.get(email="user2@user.com")
        user_3 = User.objects.get(email="user3@user.com")
        user_4 = User.objects.get(email="user4@user.com")
        user_5 = User.objects.get(email="user5@user.com")
        user_6 = User.objects.get(email="user6@user.com")

        # Set user_1 and user_2 as librarians
        user_1.is_librarian = True
        user_1.save()
        user_2.is_librarian = True
        user_2.save()

        user_list = [user_1, user_2, user_3, user_4, user_5, user_6]
        user_card = 1
        for user in user_list:
            user.user_card = user_card
            user_card += 1
            user.save()

        library, _ = Library.objects.get_or_create(
            name="Library name",
            main_page="Library main page description",
            rules_page="Library rules page description",
        )

        authors = [
            {"name": "Агния", "surname": "Барто", "birth_date": "1901-02-04"},
            {"name": "Корней", "surname": "Чуковский", "birth_date": "1882-03-31"},
            {"name": "Лев", "surname": "Толстой", "birth_date": "1828-10-28"},
            {"name": "Даниель", "surname": "Дефо", "birth_date": "1660-04-26"},
            {"name": "Джоан", "surname": "Роулинг", "birth_date": "1965-07-31"},
            {"name": "Энтони", "surname": "Бёрджесс", "birth_date": "1917-02-25"},
            {"name": "Фёдор", "surname": "Достоевский", "birth_date": "1821-10-30"},
            {"name": "Борис", "surname": "Стругацкий", "birth_date": "1933-04-15"},
            {"name": "Джон", "surname": "Толкин", "birth_date": "1892-01-03"},
            {"name": "Антуан", "surname": "Де Сент-Экзюпери", "birth_date": "1900-06-29"},
        ]

        for author_data in authors:
            author, created = Author.objects.get_or_create(**author_data)
            if not created:
                self.stdout.write(
                    self.style.WARNING(
                        f"Author {author.name} {author.surname}  already exists\n"
                    )
                )

        self.stdout.write(
            self.style.SUCCESS(f"Successfully added {len(authors)} authors")
        )

        genres = [
            {"genre": "Adventure"},
            {"genre": "Kids"},
            {"genre": "Classic"},
            {"genre": "Foreign_language"},
            {"genre": "Fantasy"},
            {"genre": "Science"},
            {"genre": "Mix"},
        ]

        for genre_data in genres:
            genre, created = BookGenre.objects.get_or_create(**genre_data)
            if not created:
                self.stdout.write(
                    self.style.WARNING(f"Genre {genre.genre}  already exists\n")
                )

        self.stdout.write(
            self.style.SUCCESS(f"Successfully added {len(genres)} genres")
        )

        features = [
            {"feature": BookFeature.RARE},
            {"feature": BookFeature.EXPENSIVE},
            {"feature": BookFeature.NO_FEATURES},
        ]

        for feature_data in features:
            feature, created = BookFeature.objects.get_or_create(**feature_data)
            if not created:
                self.stdout.write(
                    self.style.WARNING(f"Genre {feature.feature}  already exists\n")
                )

        self.stdout.write(
            self.style.SUCCESS(f"Successfully added {len(features)} features")
        )

        books_general = [
            {
                "library": library,
                "title": "Игрушки (сборник)",
                "author": Author.objects.get(surname="Барто"),
                "description": "В книжке собраны все стихотворения А. Барто из цикла "
                "«Игрушки». «Гармошки» - это серия "
                "книжек-гармошек на плотном картоне, в которую вошли популярные сказки, песенки, "
                "потешки и колыбельные для малышей. Яркие, забавные иллюстрации. "
                "Качественный картон "
                "с глянцевой пленкой. Книжку удобно использовать в игре",
                "age_restriction": 0,
                "genre": BookGenre.objects.get(genre="Kids"),
            },
            {
                "library": library,
                "title": '"Сказки" (Сборник сказок)',
                "author": Author.objects.get(surname="Чуковский"),
                "description": 'Детская книга Корней Чуковский "Сказки" с '
                '9 аудиосказками - это интересные стихи для '
                "детей про животных, птиц, насекомых, путешествия, "
                "на которых выросло ни одно поколение "
                "детей.",
                "age_restriction": 0,
                "genre": BookGenre.objects.get(genre="Kids"),
            },
            {
                "library": library,
                "title": "Harry Potter and the Philosopher's Stone",
                "author": Author.objects.get(surname="Роулинг"),
                "description": "Harry Potter has never even heard of Hogwarts "
                "when the letters start dropping on the"
                " doormat at number four, Privet Drive. Addressed in green "
                "ink on yellowish parchment "
                "with a purple seal, they are swiftly confiscated by his "
                "grisly aunt and uncle. Then, "
                "on Harry’s eleventh birthday, a great beetle-eyed giant of "
                "a man called Rubeus Hagrid "
                "bursts in with some astonishing news: Harry Potter is a wizard, "
                "and he has a place at "
                "Hogwarts School of Witchcraft and Wizardry. "
                "An incredible adventure is about to begin!",
                "age_restriction": 5,
                "genre": BookGenre.objects.get(genre="Foreign_language"),
            },
            {
                "library": library,
                "title": "A clockwork orange",
                "author": Author.objects.get(surname="Бёрджесс"),
                "description": " is a dystopian satirical black comedy novel "
                "by English writer Anthony Burgess, "
                "published on March 17, 1962. It is set in a near-future society that has a youth "
                "subculture of extreme violence.",
                "age_restriction": 13,
                "genre": BookGenre.objects.get(genre="Foreign_language"),
            },
            {
                "library": library,
                "title": "Хищные вещи века",
                "author": Author.objects.get(surname="Стругацкий"),
                "description": 'В этот том вошел роман "Хищные вещи века" — '
                'одно из ранних произведений братьев '
                "Стругацких, увлекательный фантастический детектив, "
                "герой которого проводит "
                "расследование в маленькой, задыхающейся от провинциальной "
                "тупости и буржуазной "
                "сырости стране, откуда по миру распространяется новый, "
                "смертельно опасный наркотик…",
                "age_restriction": 12,
                "genre": BookGenre.objects.get(genre="Fantasy"),
            },
            {
                "library": library,
                "title": "Властелин колец",
                "author": Author.objects.get(surname="Толкин"),
                "description": '"Властелин Колец. Хранители Кольца" - '
                'это книга, которая подарит вам незабываемые '
                "впечатления от захватывающей истории о приключениях"
                " хоббита Фродо и его друзей в "
                "мире магии и волшебства.",
                "age_restriction": 6,
                "genre": BookGenre.objects.get(genre="Fantasy"),
            },
            {
                "library": library,
                "title": "Война и мир",
                "author": Author.objects.get(surname="Толстой"),
                "description": "роман-эпопея Льва Николаевича Толстого, "
                "описывающий русское общество в эпоху войн "
                "против Наполеона в 1805—1812 годах. "
                "Эпилог романа доводит повествование до 1820 года.",
                "age_restriction": 8,
                "genre": BookGenre.objects.get(genre="Classic"),
            },
            {
                "library": library,
                "title": "Преступление и наказание",
                "author": Author.objects.get(surname="Достоевский"),
                "description": "Самое известное произведение классика "
                "русской литературы Федора Михайловича "
                "Достоевского. Роман проходят во всех российских школах "
                "и вузах, а заграницей он "
                'считается одним из символов русской культуры. '
                '"Преступление и наказание" поднимает '
                "важнейшие нравственно-мировоззренческие вопросы "
                "- о вере, совести, грехе и об "
                "искуплении через страдание.",
                "age_restriction": 12,
                "genre": BookGenre.objects.get(genre="Classic"),
            },
            {
                "library": library,
                "title": "Робинзон Крузо",
                "author": Author.objects.get(surname="Дефо"),
                "description": "История человека, сумевшего выжить на необитаемом острове. "
                "История его борьбы с "
                "безжалостными силами природы и блистательной победы. "
                "История его дружбы с благородным "
                "дикарем и опасной схватки с пиратами... ",
                "age_restriction": 5,
                "genre": BookGenre.objects.get(genre="Adventure"),
            },
            {
                "library": library,
                "title": "Маленький принц",
                "author": Author.objects.get(surname="Де Сент-Экзюпери"),
                "description": "Есть произведения, которые можно читать и "
                "перечитывать много раз. "
                "Книга Антуана де Сент-Экзюпери «Маленький принц» "
                "одна из таких. "
                "С момента первого издания в 1943 году она входит в число "
                "самых читаемых в мире. "
                "Ее автор, французский летчик и писатель, взрослый, "
                "так и оставшийся в душе ребенком. "
                "Книга «Маленький принц» рассказывает о необыкновенной встрече пилота "
                "(из-за неполадок в моторе летчику пришлось посадить самолет в пустыне)"
                "с Маленьким принцем, гостем с другой планеты. "
                " Это произведение входит в программу "
                "литературы 6 класса",
                "age_restriction": 0,
                "genre": BookGenre.objects.get(genre="Adventure"),
            },
        ]

        for book_data in books_general:
            book, created = BookGeneral.objects.get_or_create(**book_data)
            if not created:
                self.stdout.write(
                    self.style.WARNING(f"Book {book.title}  already exists\n")
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully added {len(books_general)} genera books descriptions"
            )
        )

        books_detail = [
            {
                "book_general": BookGeneral.objects.get(title="Игрушки (сборник)"),
                "edition_year": "1950-01-10",
                "page_amount": 75,
                "feature": BookFeature.objects.get(feature="Rare"),
                "client": user_3,
            },
            {
                "book_general": BookGeneral.objects.get(
                    title='"Сказки" (Сборник сказок)'
                ),
                "edition_year": "1964-03-23",
                "page_amount": 50,
                "client": user_4,
                "feature": BookFeature.objects.get(feature="No_features"),
            },
            {
                "book_general": BookGeneral.objects.get(
                    title="Harry Potter and the Philosopher's Stone"
                ),
                "edition_year": "2010-06-10",
                "page_amount": 568,
                "client": user_5,
                "feature": BookFeature.objects.get(feature="No_features"),
            },
            {
                "book_general": BookGeneral.objects.get(title="A clockwork orange"),
                "edition_year": "1983-08-25",
                "page_amount": 375,
                "feature": BookFeature.objects.get(feature="Expensive"),
                "client": user_6,
            },
            {
                "book_general": BookGeneral.objects.get(title="Хищные вещи века"),
                "edition_year": "1995-11-15",
                "page_amount": 250,
                "client": user_3,
                "feature": BookFeature.objects.get(feature="No_features"),
            },
            {
                "book_general": BookGeneral.objects.get(title="Властелин колец"),
                "edition_year": "2000-01-25",
                "page_amount": 756,
                "feature": BookFeature.objects.get(feature="Expensive"),
                "client": user_4,
            },
            {
                "book_general": BookGeneral.objects.get(title="Война и мир"),
                "edition_year": "1928-12-08",
                "feature": BookFeature.objects.get(feature="Rare"),
                "page_amount": 586,
                "client": user_5,
            },
            {
                "book_general": BookGeneral.objects.get(
                    title="Преступление и наказание"
                ),
                "edition_year": "1953-09-17",
                "page_amount": 675,
                "feature": BookFeature.objects.get(feature="Rare"),
            },
            {
                "book_general": BookGeneral.objects.get(title="Робинзон Крузо"),
                "edition_year": "1850-03-30",
                "page_amount": 965,
                "feature": BookFeature.objects.get(feature="Rare"),
            },
            {
                "book_general": BookGeneral.objects.get(title="Маленький принц"),
                "edition_year": "1996-12-31",
                "page_amount": 110,
                "feature": BookFeature.objects.get(feature="Rare"),
            },
        ]

        for book_data in books_detail:
            books, created = BookDetail.objects.get_or_create(**book_data)
            if not created:
                self.stdout.write(
                    self.style.WARNING(f"Book {book.book_general}  already exists\n")
                )

        self.stdout.write(
            self.style.SUCCESS(f"Successfully added {len(books_detail)} books")
        )

        books_volume = [
            {
                "number": 1,
                "page_amount": 567,
                "book": BookDetail.objects.get(edition_year="1928-12-08"),
            },
        ]

        for volume_data in books_volume:
            volume, created = BookVolume.objects.get_or_create(**volume_data)
            if not created:
                self.stdout.write(
                    self.style.WARNING(f"Volume {volume.volume}  already exists\n")
                )

        self.stdout.write(
            self.style.SUCCESS(f"Successfully added {len(books_volume)} volumes\n")
        )

        contents = [
            {"volume": BookVolume.objects.get(number=1), "number": " ", "content": "Том первый"},
            {"volume": BookVolume.objects.get(number=1), "number": " ", "content": "Часть первая"},
            {"volume": BookVolume.objects.get(number=1), "number": "I", "content": "5"},
            {"volume": BookVolume.objects.get(number=1), "number": "II", "content": "15"},
            {"volume": BookVolume.objects.get(number=1), "number": "III", "content": "27"},
            {"volume": BookVolume.objects.get(number=1), "number": " ", "content": "Часть вторая"},
        ]

        for content_data in contents:
            content, created = BookContent.objects.get_or_create(**content_data)
            if not created:
                self.stdout.write(
                    self.style.WARNING(f"Content {content.content}  already exists\n")
                )

        books_finances = [
            {
                "book": BookDetail.objects.get(
                    book_general=BookGeneral.objects.get(title="Игрушки (сборник)"),
                    edition_year="1950-01-10",
                ),
                "price": 15000,
            },
            {
                "book": BookDetail.objects.get(
                    book_general=BookGeneral.objects.get(
                        title='"Сказки" (Сборник сказок)'
                    ),
                    edition_year="1964-03-23",
                ),
                "price": 20000,
            },
            {
                "book": BookDetail.objects.get(
                    book_general=BookGeneral.objects.get(
                        title="Harry Potter and the Philosopher's " "Stone"
                    ),
                    edition_year="2010-06-10",
                ),
                "price": 30000,
            },
            {
                "book": BookDetail.objects.get(
                    book_general=BookGeneral.objects.get(title="A clockwork orange"),
                    edition_year="1983-08-25",
                ),
                "price": 22000,
            },
            {
                "book": BookDetail.objects.get(
                    book_general=BookGeneral.objects.get(title="Хищные вещи века"),
                    edition_year="1995-11-15",
                ),
                "price": 15000,
            },
            {
                "book": BookDetail.objects.get(
                    book_general=BookGeneral.objects.get(title="Властелин колец"),
                    edition_year="2000-01-25",
                ),
                "price": 8000,
            },
            {
                "book": BookDetail.objects.get(
                    book_general=BookGeneral.objects.get(title="Война и мир"),
                    edition_year="1928-12-08",
                ),
                "price": 150000,
            },
            {
                "book": BookDetail.objects.get(
                    book_general=BookGeneral.objects.get(
                        title="Преступление и наказание"
                    ),
                    edition_year="1953-09-17",
                ),
                "price": 400000,
            },
            {
                "book": BookDetail.objects.get(
                    book_general=BookGeneral.objects.get(title="Робинзон Крузо"),
                    edition_year="1850-03-30",
                ),
                "price": 400000,
            },
            {
                "book": BookDetail.objects.get(
                    book_general=BookGeneral.objects.get(title="Маленький принц"),
                    edition_year="1996-12-31",
                ),
                "price": 23000,
            },
        ]

        for book_finance_data in books_finances:
            book_finance, created = BookFinance.objects.get_or_create(
                **book_finance_data
            )
            if not created:
                self.stdout.write(
                    self.style.WARNING(
                        f"Finance data {book_finance.price}  already exists\n"
                    )
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully added {len(books_finances)} finance data\n"
            )
        )

        self.stdout.write(
            self.style.SUCCESS("Successfully added 2 Librarians and 4 users\n")
        )
