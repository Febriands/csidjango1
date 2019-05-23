from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = User
        fields = (
            'id', 'username',
        )


# from rest_framework import serializers
# from .models import Album

# class ArtistSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)

#     class Meta:
#         model = Artist
#         fields = (
#             'id', 'name',
#         )


# class AlbumSerializer(serializers.ModelSerializer):
#     artist = ArtistSerializer()
#     genres = serializers.SerializerMethodField()

#     def get_genres(self, album):
#         return ', '.join([str(genre) for genre in album.genres.all()])

#     class Meta:
#         model = Album
#         fields = (
#             'rank', 'name', 'year', 'artist_name', 'genres',
#         )