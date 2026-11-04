import csv
from pathlib import Path
from pprint import pprint

NUMERIC_COLUMNS = ['members', 'year_formed', 'monthly_listeners']


def read_artists(file_path):
    """Read the music artists data from a CSV file."""
    all_artists = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for artist in reader:
                all_artists.append(artist)
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    return all_artists


def filter_by_min_listeners(artists, minimum):
    """Return only the artists with at least `minimum` monthly listeners."""
    return [
        artist
        for artist in artists
        if int(artist['monthly_listeners']) >= minimum
    ]


def sort_artists_by(artists, column, reverse=True, top_n=5):
    """Sort the artists by a column and return the top N."""
    if column in NUMERIC_COLUMNS:
        key = lambda artist: int(artist[column])
    else:
        key = lambda artist: artist[column]

    sorted_artists = sorted(artists, key=key, reverse=reverse)
    return sorted_artists[:top_n]


def write_top_artists(file_path, artists):
    """Write a list of artist dictionaries to a CSV file."""
    fieldnames = list(artists[0].keys())
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for artist in artists:
            writer.writerow(artist)


def add_listeners_per_member(file_path):
    """Read the CSV, add a listeners_per_member column, and write it back."""
    artists = read_artists(file_path)
    for artist in artists:
        listeners = int(artist['monthly_listeners'])
        members = int(artist['members'])
        artist['listeners_per_member'] = round(listeners / members)
    write_top_artists(file_path, artists)


def main():
    data_dir = Path(__file__).parent / 'data'
    file_path = data_dir / 'music_artists.csv'
    artists = read_artists(file_path)

    print(f"All artists from {file_path.name}:\n")
    pprint(artists)

    popular = filter_by_min_listeners(artists, 10_000_000)
    print(f"\n{len(popular)} artists have over 10,000,000 monthly listeners.")

    # Let the user choose which column to sort by
    columns = list(artists[0].keys())
    print("\nAvailable columns to sort by:")
    for index, column in enumerate(columns):
        print(f"{index + 1}. {column}")

    choice = int(input("Enter the number of the column you want to sort by: ")) - 1
    selected_column = columns[choice]

    top_artists = sort_artists_by(artists, selected_column)
    print(f"\nTop 5 artists by {selected_column}:\n")
    for index, artist in enumerate(top_artists):
        rank = index + 1
        print(f"{rank}. {artist['band_name']} - {artist[selected_column]}")

    write_top_artists(data_dir / 'top_artists.csv', top_artists)
    print("\nSaved the top artists to data/top_artists.csv")

    add_listeners_per_member(file_path)
    print("Added a listeners_per_member column to data/music_artists.csv")


if __name__ == "__main__":
    main()