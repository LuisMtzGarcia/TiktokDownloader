import helpers

class TiktokDownloader():

    def __init__(self):
        # process to check if required files exist
        self.verify_storage_files()

        # Load tiktoks from storage to arrays
        self.downloaded_tiktoks = self.load_downloaded_tiktoks()
        return
    
    def verify_storage_files(self):
        storage_files = ['downloaded', 'failed', 'to_download']

        for file_name in storage_files:
            file_exists = helpers.storage_file_exists(file_name)
            if not file_exists:
                helpers.generate_file(file_name)
    
    def load_downloaded_tiktoks(self):
        file_name = 'downloaded'
        return helpers.load_txt_file(file_name)

    def main_process(self):
        # process to load tiktoks into in-memory array

        # Process to get full URL for Tiktok

        # Process to get download link for tiktok

        # Process to download tiktok

        # Process to add tiktok to either downloaded file, or failed file
        return

    def load_urls_to_memory(self):
        return

if __name__ == "__main__":
    downloader = TiktokDownloader()
