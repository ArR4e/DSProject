line_length = int(input('Enter line length (meters): '))
distance_between = int(input('Enter max distance between post (meters): '))

if line_length <= 0 or distance_between <=0:
    print('Values must be positive')
    exit()
if distance_between > line_length:
    print('Distance between posts is more than line lenght')
    exit()

if line_length % distance_between == 0:
    posts_count = int(line_length / distance_between + 1)
else:
    posts_count = line_length // distance_between + 2
   
print(f'{posts_count} posts are required')
