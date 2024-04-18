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
    def test_add_new_book(self, books_collector, book_name):
        books_collector.add_new_book(book_name)
        assert books_collector.books_genre[book_name] == ""
        assert books_collector.books_genre.get(book_name) is not None

    def test_add_book_in_favorites(self, books_collector):
        book_name = "Тестовая книга"
        books_collector.add_new_book(book_name)
        books_collector.add_book_in_favorites(book_name)
        assert book_name in books_collector.favorites

    def test_set_book_genre(self, books_collector):
        book_name = "Гарри Поттер и философский камень"
        expected_genre = "Фантастика"
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, expected_genre)
        actual_genre = books_collector.get_book_genre(book_name)
        assert actual_genre == expected_genre

    def test_get_book_genre(self, books_collector):
        book_name = "Гарри Поттер и философский камень"
        expected_genre = "Фантастика"
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, expected_genre)
        actual_genre = books_collector.get_book_genre(book_name)
        assert actual_genre == expected_genre

    def test_delete_book_from_favorites(self, books_collector):
        books_collector.add_new_book("Harry Potter")
        books_collector.add_book_in_favorites("Harry Potter")
        books_collector.delete_book_from_favorites("Harry Potter")
        assert "Harry Potter" not in books_collector.favorites

    def test_get_list_of_favorites_books(self, books_collector):
        books_collector.add_new_book("Harry Potter")
        books_collector.add_book_in_favorites("Harry Potter")
        favorite_books = books_collector.get_list_of_favorites_books()
        assert "Harry Potter" in favorite_books

    def test_get_books_with_specific_genre(self, books_collector):
        books_collector.add_new_book("Harry Potter")
        books_collector.set_book_genre("Harry Potter", "Фантастика")
        books_in_fantasy = books_collector.get_books_with_specific_genre("Фантастика")
        assert "Harry Potter" in books_in_fantasy

    def test_get_books_for_children(self, books_collector):
        books_collector.add_new_book("Harry Potter")
        books_collector.set_book_genre("Harry Potter", "Фантастика")
        children_books = books_collector.get_books_for_children()
        assert "Harry Potter" in children_books

    def test_get_books_for_children_2(self, books_collector):
        books_collector.add_new_book("Book not for the children")
        books_collector.set_book_genre("Book not for the children", "Ужасы")
        children_books = books_collector.get_books_for_children()
        assert "Book not for the children" not in children_books
