---

### 📄 delete.md

````md
# Delete a Book Record

## Command Used

```python
from bookshelf.models import Book

book = Book.objects.get(title="Advanced Django")
book.delete()

Book.objects.all()
```
````
