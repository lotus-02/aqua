class SongNode:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next = None
        self.prev = None


class MusicPlaylist:
    def __init__(self):
        self.head = None
        self.current_song = None

    def add_song(self, title, artist):
        new_song = SongNode(title, artist)

        if self.head is None:
            self.head = new_song
            new_song.next = new_song
            new_song.prev = new_song
            self.current_song = new_song
            print(f"\nSuccess: First song '{title}' added!")
            return

        tail = self.head.prev

        new_song.prev = tail
        new_song.next = self.head

        tail.next = new_song
        self.head.prev = new_song

        print(f"\nSuccess: '{title}' added to playlist!")

    def remove_song(self, title):
        if not self.head:
            print("\nError: The playlist is already empty!")
            return

        current = self.head
        found = False

        while True:
            if current.title.lower() == title.lower():
                found = True
                break
            current = current.next
            if current == self.head:
                break

        if not found:
            print(f"\nError: song titled '{title}' not found in the playlist.")
            return

        if current.next == self.head and current.prev == self.head:
            self.head = None
            self.current_song = None
            print("The playlist is now completely empty.")
            return

        if current == self.head:
            self.head = current.next

        if current == self.current_song:
            self.current_song = current.next

        current.prev.next = current.next
        current.next.prev = current.prev
        print("Success: song has been successfully deleted.")

    def show_playlist(self):
        if not self.head:
            print("\nYour playlist is empty! Please add some songs first.")
            return

        print("\n=======YOUR PLAYLIST=======")
        current = self.head
        index = 1

        while True:
            status = " (Now playing)" if current == self.current_song else ""
            print(f"{index}.{current.title} - {current.artist}{status}")
            current = current.next
            index += 1
            if current == self.head:
                break

        print("===========================\n")

    def play_next(self):
        if not self.current_song:
            print("\nERROR: No song available to play!")
            return

        self.current_song = self.current_song.next
        print(f"\nNext pressed -> Now playing: '{self.current_song.title}' [{self.current_song.artist}]")

    def play_previous(self):
        if not self.current_song:
            print("\nERROR: No song available to play!")
            return

        self.current_song = self.current_song.prev
        print(f"\nPrevious pressed -> Now playing: '{self.current_song.title}' [{self.current_song.artist}]")

player = MusicPlaylist()
player.add_song("Koi mil gya","A.S")
player.add_song("Black Bone","H.S")
while True:
    print("\n--- MUSIC PLAYER MENU---")
    print("1. Add new song")
    print("2. Remove a song")
    print("3. View Entire playlist ")
    print("4. paly next track")
    print("5.play prev track")
    print("6. Exit player")

    choice = input("\n Select an Option(1-6):").strip()

    if choice == '1':
        title = input("Enter song Title:").strip()
        artist = input("Enter Artist Name").strip()
        if title and artist:
            player.add_song(title, artist)
        else:
            print("Error: feild Cannot be blank!")

    elif choice =='2':
        title = input("Enter the exact title of rhe song to remove: ").strip()
        if title:
            player.remove_song(title)
        else:
            print("Error: Title cannot be blank!")

    elif choice == '3':
        player.show_playlist()

    elif choice == '4':
        player.play_next()

    elif choice == '5':
        player.play_previous()

    elif choice == '6':
        print("\nThanks for using the music player. Goodbye!")
        break

    else:
        print("Error: Please select a valid option from 1 to 6.")



