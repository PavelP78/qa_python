import pytest
from main import BooksCollector


class TestBooksCollector:
    @pytest.fixture
    def books_collector(self):
        return BooksCollector()

    def test_constructor(self, books_collector):
        assert isinstance(books_collector, BooksCollector)
        assert books_collector.books_genre == {}
        assert books_collector.favorites == []
        assert books_collector.genre == [
            "Фантастика",
            "Ужасы",
            "Детективы",
            "Мультфильмы",
            "Комедии",
        ]
        assert books_collector.genre_age_rating == ["Ужасы", "Детективы"]

    @pytest.mark.parametrize("book_name", ["Книга 1", "Книга 2", "Книга 3"])
    def test_add_new_book_different_book_name_successfully_adds(self, books_collector, book_name):
        books_collector.add_new_book(book_name)
        assert books_collector.get_books_genre()[book_name] == ""

    def test_add_book_in_favorites_with_hamlet_title_successfully_adds_in_favorite(self, books_collector):
        book_name = "hamlet"
        books_collector.add_new_book(book_name)
        books_collector.add_book_in_favorites(book_name)
        assert book_name in books_collector.get_list_of_favorites_books()

    def test_set_book_genre_with_hamlet_title_successfully_set_book_genre(self, books_collector):
        book_name = "hamlet"
        expected_genre = "Фантастика"
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, expected_genre)
        actual_genre = books_collector.get_book_genre(book_name)
        assert actual_genre == expected_genre

    def test_get_book_genre_with_hamlet_title_successfully_get_book_genre(self, books_collector):
        book_name = "hamlet"
        expected_genre = "Фантастика"
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, expected_genre)
        actual_genre = books_collector.get_book_genre(book_name)
        assert actual_genre == expected_genre

    def test_delete_book_from_favorites_with_hamlet_title_successfully_delete_from_favorite(self, books_collector):
        book_name = "hamlet"
        books_collector.add_new_book(book_name)
        books_collector.add_book_in_favorites(book_name)
        books_collector.delete_book_from_favorites(book_name)
        assert book_name not in books_collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_with_hamlet_title_successfully_in_favorite_books(self, books_collector):
        book_name = "hamlet"
        books_collector.add_new_book(book_name)
        books_collector.add_book_in_favorites(book_name)
        favorite_books = books_collector.get_list_of_favorites_books()
        assert book_name in favorite_books

    def test_get_books_with_specific_genre_with_hamlet_title_successfully_in_books_fantasty(self, books_collector):
        book_name = "hamlet"
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, "Фантастика")
        books_in_fantasy = books_collector.get_books_with_specific_genre("Фантастика")
        assert book_name in books_in_fantasy

    def test_get_books_for_children_with_harry_title_successfully_in_children_books(self, books_collector):
        book_name = "harry"
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, "Фантастика")
        children_books = books_collector.get_books_for_children()
        assert book_name in children_books

    def test_get_books_for_children_with_adult_title_not_successfully_in_children_bookse(self, books_collector):
        book_name = "adult"
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, "Ужасы")
        children_books = books_collector.get_books_for_children()
        assert book_name not in children_books
