from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import os

class MetadataEditor:
    def __init__(self, files_root_path: str, ignore_file: list[str]) -> None:
        self.music_root_path = files_root_path
        self.ignorefile = ignore_file
        self.song_name_list = [] 
        self.__create_abs_path_by_file()

    def __create_abs_path_by_file(self):
        song_list = os.listdir(self.music_root_path)
        for song in song_list:
            if ".mp3" in song:
                song_file_path = os.path.join(self.music_root_path, song)
                if self.__check_edited_files(song_file_path) == False:
                    self.song_name_list.append(song_file_path)

    def __check_edited_files(self, incoming_path: str) -> bool:
        check = False
        for path in self.ignorefile:
            if incoming_path in path:
                check = True
        return check

    def get_meta_tags(self, song_path: str) -> dict[str, str]:
        song = MP3(song_path, ID3=EasyID3)
        metadata = {key: value[0] if isinstance(value, list) else value for key, value in song.items()}
        return metadata

    def get_length(self, song_path: str) -> int:
        song = MP3(song_path).info.length
        return song
    
    def set_value_tag(self, file_path: str, target_tag: str, input_value: str):
        audio = EasyID3(file_path)
        tag = target_tag
        audio[tag] = input_value
        audio.save()

    def set_album(self, file_path: str, new_album: str):
        try:
            audio = EasyID3(file_path)
        except Exception:
            from mutagen.id3 import ID3
            audio = EasyID3()
            audio.save(file_path)
            audio = EasyID3(file_path)
        audio["album"] = new_album
        audio.save()
    
    def add_to_ignorefile(self, song_path: str):
        ignore_path = os.path.join(self.music_root_path, ".ignorefile")
        if song_path in self.ignorefile:
            return  
        try:
            with open(ignore_path, "a", encoding="utf-8") as f:
                f.write(song_path + "\n")
        except OSError as err:
            print(f"Error al escribir en .ignorefile: {err}")
        self.ignorefile.append(song_path)