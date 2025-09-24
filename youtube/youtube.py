from email.contentmanager import maintype

from pytubefix import YouTube


def main(link: str, location: str):
    yt = YouTube(link)
    print("Author: ", yt.author)
    print("Title: ", yt.title)
    print("Views: ", yt.views)
    yd = yt.streams.get_highest_resolution()
    yd.download(location)
    print('Download Done')


if __name__ == '__main__':
    link = ("https://www.youtube.com/watch?v=RhBl85uNigU&list=PLdV78aYad4w_mDimKJ9gJxpgetzAToNUH&index=3")
    location = 'D:/YoutubeDownloads'
    main(link, location)

