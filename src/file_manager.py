import os

class FileManager:
    def __init__(self, music_root_path: str) -> None:
        self.music_folder = music_root_path
        self.ignorefile_name = ".ignorefile"

        self.ignorefile_path = ""

        self.__check_ignorefile()

    def __check_ignorefile(self):
        ignorefile_path = os.path.join(self.music_folder, self.ignorefile_name)
        self.ignorefile_path = ignorefile_path
        if not os.path.exists(ignorefile_path):
            self.__create_ignore_file(ignorefile_path)

    def __create_ignore_file(self, file_path: str):
        try:
            with open(file_path, 'w') as file:
                file.write("")
        except OSError as err:
            print(err)

    def read_ignorefile_content(self) -> list[str]:
        ignored_list = []
        try:
            with open(self.ignorefile_path, 'r', encoding="utf-8") as file:
                lines = file.readlines()
                for path in lines:
                    ignored_list.append(path)
            return ignored_list
        except OSError as err:
            print(err)
            return []
    
    def set_new_ignore_song_by_path(self, song_path: str):
        current_list = self.read_ignorefile_content()
        try:
            with open(self.ignorefile_path, 'w') as file:
                for path in current_list:
                    file.write(path if path.endswith('\n') else path + '\n')
                file.write(song_path + '\n')    
        except OSError as err:
            print(err)