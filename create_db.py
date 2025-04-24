from flask import Flask
from models import Artist, Album, Song, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()

        artist = Artist(name='Twenty One Pilots')
        db.session.add(artist)

        albums = [
            Album(title='Twenty One Pilots', year='2009', artist=artist),
            Album(title='Vessel', year='2013', artist=artist),
            Album(title='Blurryface', year='2015', artist=artist),
            Album(title='Trench', year='2018', artist=artist),
            Album(title='Scaled and Icy', year='2021', artist=artist),
            Album(title='Clancy', year='2024', artist=artist)
        ]
        db.session.add_all(albums)
        db.session.commit()

        songs_data = [
            # Twenty One Pilots
            ('Implicit Demand For Proof', '4:51', 1, 'Twenty One Pilots'),
            ('Friend, Please', '4:12', 5, 'Twenty One Pilots'),
            ('Taxi Cab', '4:45', 12, 'Twenty One Pilots'),
            ('Isle Of Flightless Birds', '5:45', 13, 'Twenty One Pilots'),
            # Vessel
            ('Ode To Sleep', '5:08', 1, 'Vessel'),
            ('Screen', '3:49', 7, 'Vessel'),
            ('Migraine', '3:59', 3, 'Vessel'),
            ('The Run And Go', '3:49', 8, 'Vessel'),
            # Blurryface
            ('Heavydirtysoul', '3:54', 1, 'Blurryface'),
            ('Fairly Local', '3:27', 4, 'Blurryface'),
            ('The Judge', '4:57', 7, 'Blurryface'),
            ('Goner', '3:56', 14, 'Blurryface'),
            #Trench
            ('Jumpsuit', '3:58', 1, 'Trench'),
            ('Morph', '4:18', 3, 'Trench'),
            ('Neon Gravestones', '4:00', 7, 'Trench'),
            ('Leave the City', '4:40', 14, 'Trench'),
            # Scaled and Icy
            ('Choker', '3:43', 2, 'Scaled and Icy'),
            ('Shy Away', '2:55', 3, 'Scaled and Icy'),
            ('No Chances', '3:46', 10, 'Scaled and Icy'),
            ('Redecorate', '4:05', 11, 'Scaled and Icy'),
            #Clancy
            ('Overcompensate', '3:56', 1, 'Clancy'),
            ('Routines In the Night', '3:22', 5, 'Clancy'),
            ('Lavish', '2:38', 8, 'Clancy'),
            ('Navigating', '3:43', 9, 'Clancy'),
        ]

        title_to_album = {album.title: album for album in albums}
        songs = [Song(title=s[0], length=s[1], track_number=s[2], album=title_to_album[s[3]]) for s in songs_data]

        db.session.add_all(songs)
        db.session.commit()
