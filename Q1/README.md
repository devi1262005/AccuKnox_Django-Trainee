Question 1: By default are django signals executed synchronously or asynchronously?

-- By default, Django signals are executed synchronously. 

-- This means that when a signal is sent, all connected receivers are executed one after the other in the same thread. 

-- If one receiver takes a long time to complete, the others must wait until it finishes.

-- Django does not provide built-in asynchronous signals. 

-- If one needs asynchronous execution, they can implement it with Celery, threading or async tasks.


OUTPUT:

![Output Q1](https://raw.githubusercontent.com/devi1262005/AccuKnox_Django-Trainee/093d9ae77fac90f267f225451992d06258e77f11/images/Output-Q1.png)


-- The output shows list1 being printed in one receiver, and list2 printed in other receiver

-- Since the two receivers are connected they are executed after one another

-- List2 waits for List1 to be completed, since they share the same thread.
