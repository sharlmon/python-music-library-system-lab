class Song:
    """
    Song class representing individual songs in a music library system
    while tracking global library statistics across all songs.
    """

    # Class Attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}
    artist_count = artists_count

    def __init__(self, name, artist, genre):
        """
        Instantiates a song with a name, artist, and genre.
        Triggers each class method to update library-wide tracking attributes.
        """
        self.name = name
        self.artist = artist
        self.genre = genre

        # Trigger class methods upon song creation
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artists_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increments the value of count by one."""
        if not hasattr(cls, "count"):
            cls.count = 0
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """
        Adds new genre to class attribute genres, ensuring only unique genres.
        """
        if not hasattr(cls, "genres") or not isinstance(cls.genres, list):
            cls.genres = []
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """
        Adds new artist to class attribute artists, ensuring only unique artists.
        """
        if not hasattr(cls, "artists") or not isinstance(cls.artists, list):
            cls.artists = []
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """
        Updates class attribute genre_count.
        Increments genre key by 1, or initializes it to 1 if not present.
        """
        if not hasattr(cls, "genre_count") or not isinstance(cls.genre_count, dict):
            cls.genre_count = {}
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """
        Updates class attribute artists_count (and artist_count).
        Increments artist key by 1, or initializes it to 1 if not present.
        """
        if not hasattr(cls, "artist_count") or not isinstance(cls.artist_count, dict):
            cls.artist_count = {}
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1

        if not hasattr(cls, "artists_count") or not isinstance(cls.artists_count, dict):
            cls.artists_count = cls.artist_count
        elif cls.artists_count is not cls.artist_count:
            cls.artists_count[artist] = cls.artists_count.get(artist, 0) + 1

    # Aliases for compatibility
    add_to__genres = add_to_genres
    add_to_artist_count = add_to_artists_count
