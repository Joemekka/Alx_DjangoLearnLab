# Create a Book Record

## Command Used

```python
from bookshelf.models import Book

book = Book.objects.create(
    title="Django for Beginners",
    author="George Orwell",
    publication_year=2023
)
book
```
