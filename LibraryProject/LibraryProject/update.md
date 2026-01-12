---

### 📄 update.md

````md
# Update a Book Record

## Command Used

```python
from bookshelf.models import Book

book = Book.objects.get(title="Django for Beginners")
book.title = "Advanced Django"
book.save()

book
```
````
