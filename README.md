# Social Network

## Setup

1. Run the initialization script to set up the database:
   ```bash
   ./rebuild.sh
   ```

2. The database will be created and populated with sample data.

## Database Structure

The database consists of several tables that store different aspects of the social network:

- **Users Table**: Contains user information.
  - `user_id`: Unique identifier for each user.
  - `username`: Unique username for the user.
  - `email`: User's email address.
  - `password`: User's password (hashed).
  - `age`: User's age.

- **Accounts Table**: Links users to their social media accounts.
  - `account_id`: Unique identifier for each account.
  - `username`: Username for the account.
  - `user_id`: Foreign key linking to the Users table.

- **Follows Table**: Tracks follow relationships between accounts.
  - `follower_account_id`: The account that follows another account.
  - `followee_account_id`: The account being followed.

- **Posts Table**: Stores posts made by accounts.
  - `id`: Unique identifier for each post.
  - `account_id`: Foreign key linking to the Accounts table.
  - `message`: Content of the post.
  - `posted_at`: Timestamp of when the post was made.

- **Likes Table**: Records likes on posts.
  - `post_id`: Foreign key linking to the Posts table.
  - `account_id`: Foreign key linking to the Accounts table.

- **Blocks Table**: Manages blocked accounts.
  - `blocker_account_id`: The account that blocks another account.
  - `blocked_account_id`: The account that is blocked.

## Using the Queries

### Basic Queries

1. **Adding a User**:
   - Use the `add_user(db, username, email, password, age)` function to add a new user to the Users table.
   - Example:
     ```python
     add_user(db, 'john_doe', 'john@example.com', 'securepassword', 30)
     ```

2. **Creating an Account**:
   - Use the `add_account(db, username, user_id)` function to create a new account linked to a user.
   - Example:
     ```python
     add_account(db, 'johns_account', user_id)
     ```

3. **Following Another Account**:
   - Use the `follow_user(db, follower_username, followee_username)` function to establish a follow relationship.
   - Example:
     ```python
     follow_user(db, 'johns_account', 'jane_doe_account')
     ```

4. **Making a Post**:
   - Use the `add_post(db, account_username, message)` function to create a new post.
   - Example:
     ```python
     add_post(db, 'johns_account', 'Hello, world!')
     ```

5. **Liking a Post**:
   - Use the `like_post(db, post_id, account_username)` function to like a specific post.
   - Example:
     ```python
     like_post(db, 1, 'johns_account')
     ```

### Interesting Queries

1. **Viewing All Follows**:
   - Use the `print_all_follows(db)` function to display all follow relationships in the Follows table.
   - This will show you who is following whom.

2. **Viewing All Posts**:
   - Use the `print_all_posts(db)` function to display all posts made by accounts.
   - This will help you see the content shared by users.

3. **Getting a User's Feed**:
   - Use the `get_feed(db, account_username)` function to retrieve the posts from accounts that a user follows.
   - Example:
     ```python
     feed = get_feed(db, 'johns_account')
     ```

4. **Counting Total Accounts**:
   - Use the `count_total_accounts(db)` function to get the total number of accounts in the Accounts table.
   - This can help you understand the scale of your social network.

## Conclusion

Thanks for checking out myFace, a social media plaform by Analiese Rasmussen and Carter Robinson.