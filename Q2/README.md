Question 2: Do django signals run in the same thread as the caller?

-- Yes, django signals run in the same thread as the caller.

-- The code inside the caller like Book.objects.create() or Book.save() runs in the main thread(MainThread).

-- Django then fires the post_save signal.

-- All the receivers connected to the post_save are again executed in the MainThread, 
   which is the same thread as the caller function.
   
-- This behavior can be altered if someone uses async tasks with Celery, threading or async_task.

OUTPUT: 

![Output-Q2](https://github.com/devi1262005/AccuKnox_Django-Trainee/raw/c57c471ea55cf43de72e9bee2d9ff5bffac0be15/images/Output-Q2.png)


-- This output shows the receiver and caller being run in the same main thread.
