---

### 📄 retrieve.md

````md
# Retrieve a Book Record

## Command Used

```python
from bookshelf.models import Book

book = Book.objects.get(title="Django for Beginners")
book.title, book.author, book.publication_year=1984
```
````
