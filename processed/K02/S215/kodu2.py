from math import ceil

def get_posts_amount(line_length, max_post_distance):
    posts_between = ceil(line_length / max_post_distance)
    return posts_between + 1


line_length = int(input("Sisestage liini pikkus: "))
post_max_distance = int(input("Sisestage posti kaugus: "))

print(
    get_posts_amount(line_length, post_max_distance)
)

