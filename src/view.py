from src.metada_editor import MetadataEditor
from src.file_manager import FileManager
from dotenv import load_dotenv
import flet as ft
import os

load_dotenv()

MUSIC_ROOT = os.getenv('MUSIC_BANK')
IGNOREFILE = os.getenv('IGNORE_GILE')

class ViewModel:
    def __init__(self) -> None:
        self.manager = FileManager(music_root_path=MUSIC_ROOT)
        self.ignore_songs = self.manager.read_ignorefile_content()
        self.meta = MetadataEditor(files_root_path=MUSIC_ROOT, ignore_file=self.ignore_songs)
        
        self.songs = self.meta.song_name_list
        self.current_index = 0

    def load_current_song(self, current_song_label, title, artist, album, date, duration):
        if self.current_index >= len(self.songs):
            current_song_label.value = "¡Todas las canciones editadas!"
            title.value = artist.value = album.value = date.value = duration.value = ""
            return
        song = self.songs[self.current_index]

        new_album = album.value 
        self.meta.set_album(song, new_album)
        
        metadata = self.meta.get_meta_tags(song)
        song_length = self.meta.get_length(song)
        
        current_song_label.value = os.path.basename(song)
        title.value = metadata.get('title', '')
        artist.value = metadata.get('artist', '')
        album.value = metadata.get('album', '')
        date.value = metadata.get('date', '')
        duration.value = song_length        

    def input_component(self, label: str) -> ft.TextField:
        return ft.TextField(label=label, width=300)

    def save_button(self, function) -> ft.Button:
        return ft.Button(text="Change Data", on_click=function)

    def main_view(self, page: ft.Page):
        page.title = "Metadata Editor"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.theme = ft.Theme(color_scheme_seed=ft.Colors.BLUE_ACCENT)
        page.window.width = 350
        page.window.height = 480
        page.window.resizable = False

        def on_save(e):
            if self.current_index >= len(self.songs):
                return

            song = self.songs[self.current_index]
            self.meta.set_value_tag(song, "title", title.value)
            self.meta.set_value_tag(song, "artist", artist.value)
            self.meta.set_value_tag(song, "album", album.value)
            self.meta.set_value_tag(song, "date", date.value)
            
            self.meta.add_to_ignorefile(song)

            self.current_index += 1
            album.value = ""
            self.load_current_song(current_song, title, artist, album, date, duration)
            page.update()

        current_song = ft.Text("Esperando...")
        title = self.input_component("Title")
        artist = self.input_component("Artist")
        album = self.input_component("Album")
        date = self.input_component("Date")
        duration = self.input_component("Duration")
        save_btn = self.save_button(function=on_save)

        self.load_current_song(current_song, title, artist, album, date, duration)

        page.add(
            ft.Column(
                [
                    current_song,
                    title,
                    artist,
                    album,
                    date,
                    duration,
                    save_btn
                ],
                horizontal_alignment = ft.CrossAxisAlignment.CENTER
            )
        )

    def start_flet(self):
        ft.app(self.main_view)