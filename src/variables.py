class Variables():
    def __init__(self):
        super().__init__()
        self.metadata = {}
        self.current_sync_row = None
        self.current_lyrics_list = None
        self.plain_lyrics = None
        self.synced_lyrics = None

variables = Variables()