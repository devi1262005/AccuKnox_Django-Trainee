# Q3. By default do django signals run in the same database transaction as the caller?

-- Yes, by default, django signals run in the same database transaction as the caller.

-- Django signals (like post_save) run in the same transaction as the code that triggers them (The caller).



![Output-Q3.1](https://raw.githubusercontent.com/devi1262005/AccuKnox_Django-Trainee/19b0fa2d245efa54e072c419fc92863c82a8d9d1/images/Output-Q3.1.png)

![Output-Q3.2](https://raw.githubusercontent.com/devi1262005/AccuKnox_Django-Trainee/19b0fa2d245efa54e072c419fc92863c82a8d9d1/images/Output-Q3.2.png)

-- These outputs show that the signal runs in the same thread as the code that triggered it.

-- All operations happen in the same MainThread as the caller.

-- Here the cart menu shows the CRUD operations happening within the database.

-- Due to transaction.atomic(), all database operations are part of same database transaction, which allow rollbacks (Updating, Deleting).
