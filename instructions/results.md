### Server 1:
```Python
............
----------------------------------------------------------------------
Ran 12 tests in 4.801s

OK
```

### Server 2: 
```Python

FAIL: test_read_all_tasks (__main__.TestAPI)
FAIL: test_create_not_enough_data (__main__.TestAPI)
FAIL: test_create_task (__main__.TestAPI)
FAIL: test_read_one_task (__main__.TestAPI)
FAIL: test_update_task (__main__.TestAPI)

FAILED (failures=5)
```

### Server 3:
```Python
FAIL: test_delete_task (__main__.TestAPI)
FAIL: test_delete_task_fake (__main__.TestAPI)
FAIL: test_read_one_fake (__main__.TestAPI)
FAIL: test_update_task_fake (__main__.TestAPI)

FAILED (failures=4)
```

### Server 4:
```Python

FAIL: test_delete_task_invalid (__main__.TestAPI)
FAIL: test_read_current_user (__main__.TestAPI)

FAILED (failures=2)
```
