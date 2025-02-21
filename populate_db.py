import sqlite3
import random
from datetime import datetime, timedelta
from queries import *

"""
Populating the database with less random data, accounts, users, follows etc. from ChatGPT.
"""

def main():
    db = sqlite3.connect('social.db')
    with db:
        with open('schema.sql', 'r') as f:
            db.executescript(f.read())

        add_user(db, 'jane_doe', 'jane.doe@example.com', 'password123', 30)
        add_user(db, 'john_smith', 'john.smith@example.com', 'password456', 25)
        add_user(db, 'alice_jones', 'alice.jones@example.com', 'password789', 28)
        add_user(db, 'bob_brown', 'bob.brown@example.com', 'password101', 22)
        add_user(db, 'charlie_white', 'charlie.white@example.com', 'password123', 30)
        add_user(db, 'diana_black', 'diana.black@example.com', 'password456', 28)
        add_user(db, 'eric_green', 'eric.green@example.com', 'password789', 26)
        add_user(db, 'frank_red', 'frank.red@example.com', 'password101', 32)
        add_user(db, 'alice_smart', 'alice.smart@example.com', 'password202', 29)
        add_user(db, 'mike_bold', 'mike.bold@example.com', 'password303', 31)
        add_user(db, 'lucy_loud', 'lucy.loud@example.com', 'password404', 27)
        add_user(db, 'oliver_cool', 'oliver.cool@example.com', 'password505', 25)
        add_user(db, 'emma_clever', 'emma.clever@example.com', 'password606', 30)
        add_user(db, 'noah_brave', 'noah.brave@example.com', 'password707', 28)
        add_user(db, 'ava_kind', 'ava.kind@example.com', 'password808', 29)
        add_user(db, 'will_fresh', 'will.fresh@example.com', 'password909', 26)
        add_user(db, 'mia_quick', 'mia.quick@example.com', 'password1010', 27)
        add_user(db, 'ethan_calm', 'ethan.calm@example.com', 'password1111', 30)
        add_user(db, 'sophia_sharp', 'sophia.sharp@example.com', 'password1212', 29)
        add_user(db, 'jack_happy', 'jack.happy@example.com', 'password1313', 32)

        #getting 
        add_account(db, 'jane_doe_account1', get_user_id_by_username(db, 'jane_doe'))
        add_account(db, 'jane_doe_account2', get_user_id_by_username(db, 'jane_doe'))
        add_account(db, 'jane_doe_account3', get_user_id_by_username(db, 'jane_doe'))
        add_account(db, 'jane_doe_account4', get_user_id_by_username(db, 'jane_doe'))
        add_account(db, 'john_smith_account1', get_user_id_by_username(db, 'john_smith'))
        add_account(db, 'john_smith_account2', get_user_id_by_username(db, 'john_smith'))
        add_account(db, 'alice_jones_account1', get_user_id_by_username(db, 'alice_jones'))
        add_account(db, 'bob_brown_account1', get_user_id_by_username(db, 'bob_brown'))
        add_account(db, 'charlie_white_account1', get_user_id_by_username(db, 'charlie_white'))
        add_account(db, 'diana_black_account1', get_user_id_by_username(db, 'diana_black'))
        add_account(db, 'eric_green_account1', get_user_id_by_username(db, 'eric_green'))
        add_account(db, 'frank_red_account1', get_user_id_by_username(db, 'frank_red'))
        add_account(db, 'alice_smart_account1', get_user_id_by_username(db, 'alice_smart'))
        add_account(db, 'mike_bold_account1', get_user_id_by_username(db, 'mike_bold'))
        add_account(db, 'lucy_loud_account1', get_user_id_by_username(db, 'lucy_loud'))
        add_account(db, 'oliver_cool_account1', get_user_id_by_username(db, 'oliver_cool'))
        add_account(db, 'emma_clever_account1', get_user_id_by_username(db, 'emma_clever'))
        add_account(db, 'noah_brave_account1', get_user_id_by_username(db, 'noah_brave'))
        add_account(db, 'ava_kind_account1', get_user_id_by_username(db, 'ava_kind'))
        add_account(db, 'will_fresh_account1', get_user_id_by_username(db, 'will_fresh'))
        add_account(db, 'mia_quick_account1', get_user_id_by_username(db, 'mia_quick'))
        add_account(db, 'ethan_calm_account1', get_user_id_by_username(db, 'ethan_calm'))
        add_account(db, 'sophia_sharp_account1', get_user_id_by_username(db, 'sophia_sharp'))
        add_account(db, 'jack_happy_account1', get_user_id_by_username(db, 'jack_happy'))


        add_post(db, 'john_smith_account1', 'John here! Excited to share my thoughts.')
        add_post(db, 'alice_jones_account1', 'Alice loves coding and coffee!')
        add_post(db, 'bob_brown_account1', 'Bob is here to make new friends!')
        add_post(db, 'jane_doe_account1', 'Jane is ready to meet people!')
        add_post(db, 'jane_doe_account1', 'Update!')
        add_post(db, 'jane_doe_account1', 'Hello!')
        add_post(db, 'jane_doe_account2', 'Update!')
        add_post(db, 'jane_doe_account2', 'Hello!')
        #GPT added posts
        add_post(db, 'jane_doe_account1', 'Jane is ready to meet people!')
        add_post(db, 'jane_doe_account2', 'Jane loves to share her thoughts!')
        add_post(db, 'john_smith_account1', 'John here! Excited to share my thoughts.')
        add_post(db, 'john_smith_account2', 'John is enjoying the day!')
        add_post(db, 'alice_jones_account1', 'Alice loves coding and coffee!')
        add_post(db, 'bob_brown_account1', 'Bob is here to make new friends!')
        add_post(db, 'charlie_white_account1', 'Charlie is excited about hiking!')
        add_post(db, 'diana_black_account1', 'Diana is passionate about design and art!')
        add_post(db, 'eric_green_account1', 'Eric is learning to cook new recipes!')
        add_post(db, 'frank_red_account1', 'Frank enjoys biking through the city!')
        add_post(db, 'alice_smart_account1', 'Alice is exploring the world of AI!')
        add_post(db, 'mike_bold_account1', 'Mike is hitting the gym every day!')
        add_post(db, 'lucy_loud_account1', "Lucy can't stop binge-watching sitcoms!")
        add_post(db, 'oliver_cool_account1', 'Oliver is planning his next adventure!')
        add_post(db, 'emma_clever_account1', 'Emma just started a new coding project!')
        add_post(db, 'noah_brave_account1', 'Noah is training for a marathon!')
        add_post(db, 'ava_kind_account1', 'Ava is volunteering at the animal shelter!')
        add_post(db, 'will_fresh_account1', 'Will is trying his hand at photography!')
        add_post(db, 'mia_quick_account1', 'Mia is obsessed with puzzle games!')
        add_post(db, 'ethan_calm_account1', 'Ethan is learning guitar in his free time!')
        add_post(db, 'sophia_sharp_account1', 'Sophia is writing a new blog post!')
        add_post(db, 'jack_happy_account1', 'Jack is excited for the weekend camping trip!')


        # # Print all accounts
        print()
        print()
        print("================================================")
        print("================================================")
        count_total_accounts(db)
        print()
        print()
        print("================================================")
        print("================================================")
        # # # Print all posts
        print_all_posts(db)
        print()
        print()
        print("================================================")
        print("================================================")
        delete_post(db, 30)
        delete_post(db, 29)
        delete_post(db, 28)
        delete_post(db, 27)
        delete_post(db, 26)
        delete_post(db, 25)
        delete_post(db, 24)
        print()
        print()
        print("================================================")
        print("================================================")
        print_all_posts(db)
        print()
        print()
        print("================================================")
        print("================================================")
        # # # Print all follows
        # print_all_follows(db)

        like_post(db, 4, 'john_smith_account1') #John Smith likes Jane Doe's post, boosting her influence score
        like_post(db, 4, 'jack_happy_account1')
        like_post(db, 4, 'sophia_sharp_account1')
        like_post(db, 1, 'noah_brave_account1')
        like_post(db, 1, 'bob_brown_account1')
        like_post(db, 1, 'jane_doe_account4')
        like_post(db, 1, 'john_smith_account1')
        like_post(db, 2, 'alice_jones_account1')  # Alice likes John's post
        like_post(db, 3, 'bob_brown_account1')    # Bob likes Alice's post
        like_post(db, 5, 'charlie_white_account1') # Charlie likes Bob's post
        like_post(db, 6, 'diana_black_account1')   # Diana likes Charlie's post
        like_post(db, 7, 'eric_green_account1')    # Eric likes Diana's post
        like_post(db, 8, 'frank_red_account1')      # Frank likes Eric's post
        like_post(db, 9, 'alice_smart_account1')    # Alice Smart likes Frank's post
        like_post(db, 10, 'mike_bold_account1')     # Mike likes Alice Smart's post
        like_post(db, 11, 'lucy_loud_account1')      # Lucy likes Mike's post
        like_post(db, 12, 'oliver_cool_account1')    # Oliver likes Lucy's post

        block_user(db, 'jane_doe_account1', 'john_smith_account1')
        block_user(db, 'noah_brave_account1', 'john_smith_account1')
        block_user(db, 'frank_red_account1', 'noah_brave_account1')

        follow_user(db, 'john_smith_account1', 'jane_doe_account1')
        follow_user(db, 'jane_doe_account1', 'john_smith_account1')  # Jane follows John's account
        #follow_user(db, 'jane_doe_account1', 'alice_jones_account1')  # Jane follows Alice's account
        follow_user(db, 'john_smith_account1', 'bob_brown_account1')  # John follows Bob's account
        follow_user(db, 'john_smith_account1', 'charlie_white_account1')  # John follows Charlie's account
        follow_user(db, 'alice_jones_account1', 'diana_black_account1')  # Alice follows Diana's account
        follow_user(db, 'bob_brown_account1', 'eric_green_account1')  # Bob follows Eric's account
        follow_user(db, 'charlie_white_account1', 'frank_red_account1')  # Charlie follows Frank's account
        follow_user(db, 'diana_black_account1', 'alice_smart_account1')  # Diana follows Alice Smart's account
        follow_user(db, 'eric_green_account1', 'mike_bold_account1')  # Eric follows Mike's account
        follow_user(db, 'frank_red_account1', 'lucy_loud_account1')  # Frank follows Lucy's account
        follow_user(db, 'alice_smart_account1', 'oliver_cool_account1')  # Alice Smart follows Oliver's account
        follow_user(db, 'mike_bold_account1', 'emma_clever_account1')  # Mike follows Emma's account
        follow_user(db, 'lucy_loud_account1', 'noah_brave_account1')  # Lucy follows Noah's account
        follow_user(db, 'oliver_cool_account1', 'ava_kind_account1')  # Oliver follows Ava's account
        follow_user(db, 'emma_clever_account1', 'will_fresh_account1')  # Emma follows Will's account
        follow_user(db, 'noah_brave_account1', 'mia_quick_account1')  # Noah follows Mia's account
        follow_user(db, 'ava_kind_account1', 'ethan_calm_account1')  # Ava follows Ethan's account
        follow_user(db, 'will_fresh_account1', 'sophia_sharp_account1')  # Will follows Sophia's account
        follow_user(db, 'mia_quick_account1', 'jack_happy_account1')  # Mia follows Jack's account
        # print_all_follows(db)

        print()
        print()
        print("================================================")
        print("================================================")
        feed = get_feed(db, 'john_smith_account1')
        print("John's Feed With Blocked:")
        for post_id, username, message, posted_at in feed:
            print(f"{posted_at}: {message}")
        print()
        print()
        print("================================================")
        print("================================================")

        unblock_user(db, 'jane_doe_account1', 'john_smith_account1')
        follow_user(db, 'john_smith_account1', 'jane_doe_account1')

        print()
        print()
        print("================================================")
        print("================================================")
        feed = get_feed(db, 'john_smith_account1')
        print("John's Feed After Unblock:")
        for post_id, username, message, posted_at in feed:
            print(f"{posted_at}: {message}")
        print()
        print()
        print("================================================")
        print("================================================")

        print("Posts with Like Counts:")
        posts_with_likes = get_posts_with_likes(db)
        for post_id, message, posted_at, username, like_count in posts_with_likes:
            print(f"Post ID: {post_id}, Username: {username}, Message: {message}, Posted At: {posted_at}, Likes: {like_count}")
        print()
        print()
        print("================================================")
        print("================================================")
        follow_user(db, 'jane_doe_account1', 'alice_jones_account1')

        print("John's Recommended")
        recommended_posts = get_recommended_posts(db, 'john_smith_account1')
        for post in recommended_posts:
            print(f"Username: {post[1]}, Message: {post[2]}, Posted At: {post[3]}")
        print()
        print()
        print("================================================")
        print("================================================")

        get_most_influential_users(db)

        print()
        print()
        print("================================================")
        print("================================================")

if __name__ == "__main__":
     main()