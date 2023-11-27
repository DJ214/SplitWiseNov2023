abcd
# Splitwise

## Architecture Overview

### Architecture Diagram

The expense-sharing system follows a three-tier architecture with the presentation layer, business logic layer, and data access layer.

```sql
+---------------------+        +-----------------------+        +------------------------+
|      Controller     |  <---  |      Service Layer    |  <---  |       Data Access      |
+---------------------+        +-----------------------+        +------------------------+
|   API Endpoints     |        |    Business Logic     |        |   Database Queries     |
+---------------------+        +-----------------------+        +------------------------+
            |                             |                                 |
            |                             |                                 |
            +-------------------------------------------------------------+
                                          |
                                          v
                                   +--------------+
                                   |    Models    |
                                   +--------------+
                                   | User         |
                                   | Expense      |
                                   | Transaction  |
                                   +--------------+


```

## Database Schema

### User Table

- `user_name` (Primary Key)
- `name`
- `email`
- `mobileNumber`

### Expense Table

- `amount` 
- `group`
- `created_by`
- `description` 
- `created_at` 
- `participants`

### Transaction Table

- `sender` 
- `receiver` 
- `amount`

### Group Table

- `name`
- `participants` 
- `admins`
- `description`

### ExpensePayingUser Table

- `expense`
- `user` 
- `amount`

### ExpenseOwingUser Table

- `expense` 
- `user` 
- `amount`



## API Endpoints

### User Management

- `POST /api/registeruser/` - Create a user
- `GET /api/registeruser/{userId}/` - Get user details
- `PUT /api/registeruser/{userId}/` - Update user details



## Class Structure

### BaseModel Class

```python
class BaseModel:
    id
    date_created
    last_modified
``` 

### User Class

```python
class User:
    name
    user_name
    email
    mobileNumber
    hashed_password
```
### Expense Class

```python
class Expense:
    amount
    group
    created_by
    description
    created_at
    participants
```
### Transaction Class

```python
class Transaction:
    sender
    receiver
    amount
```
### Group Class

```python
class Group:
    name
    participants
    admins
    description
```

### ExpensePayingUser Class

```python
class Group:
    expense
    user
    amount
    
```
### ExpenseOwingUser Class

```python
class Group:
    expense
    user
    amount
    
```
