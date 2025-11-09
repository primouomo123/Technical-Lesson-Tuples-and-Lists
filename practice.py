user_data = [
    ("Rock", ["Metallica", "Guns N' Roses", "AC/DC"]),
    ("Pop", ["Taylor Swift", "Ed Sheeran", "BTS"]),
    ("Hip Hop", ["Drake", "Kendrick Lamar", "J. Cole"]),
    ("Rock", ["Led Zeppelin", "Pink Floyd", "The Who"]),
    ("Pop", ["Ariana Grande", "The Weeknd", "Olivia Rodrigo"]),
]

genre_counts = {}

for genre, _ in user_data:
    if genre in genre_counts:
        genre_counts[genre] += 1
    else:
        genre_counts[genre] = 1

most_popular_genre = max(genre_counts, key=genre_counts.get)
print("Most Popular Genre:", most_popular_genre)

target_artist = "BTS"
users_listening = []

for i, (_, artists) in enumerate(user_data):
    if target_artist in artists:
        users_listening.append(i)

if users_listening:
    print(f"Users listening to {target_artist}", users_listening)
else:
    print(f"No users listened to {target_artist} this week")